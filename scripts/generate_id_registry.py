#!/usr/bin/env python3
from pathlib import Path
import re, yaml, datetime
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
COMPONENTS = DOCS / "components"
OUT_DIR = COMPONENTS / "stickers"
OUT_DIR.mkdir(parents=True, exist_ok=True)

CATEGORY_TITLES = {
    "TS":  "Temperature sensors (DS18B20, PT100, MAX31865, etc.)",
    "ENV": "Environmental sensors (BME280/BMP280, SHT4x, TSL2561…)",
    "PS":  "Power supplies/chargers/regulators (buck, LDO, TP4056…)",
    "MC":  "Microcontrollers / dev boards (ESP32, RP2040…)",
    "RF":  "Radios / comms (LoRa, nRF24, ESP-Now modules…)",
    "IO":  "I/O expanders / ADC / DAC / level shifting",
    "AC":  "Actuators (fans, motors, servos, relays, MOSFET boards)",
    "CN":  "Connectors / cables / adapters",
    "PA":  "Passive Components (resistors, capacitors, potentiometers, trim pots)",
    "OT":  "Other / misc",
}

ID_RE = re.compile(r"^([A-Z]{2,3})(\d{3})$")

def parse_front_matter(text: str):
    if text.startswith("\ufeff"):
        text = text[1:]
    if not text.startswith("---"):
        return {}, text
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return {}, text
    yml_lines = []
    i = 1
    while i < len(lines):
        if lines[i].strip() == "---":
            i += 1
            break
        yml_lines.append(lines[i])
        i += 1
    else:
        return {}, text
    body = "".join(lines[i:])
    try:
        fm = yaml.safe_load("".join(yml_lines)) or {}
        if not isinstance(fm, dict):
            fm = {}
    except Exception:
        fm = {}
    return fm, body

def build_page_url(md: Path) -> str:
    rel = md.relative_to(DOCS).with_suffix("")
    if md.name.lower() == "index.md":
        rel_url = f"{rel.parent.as_posix()}/"
    else:
        rel_url = f"{rel.as_posix()}/"
    return "https://thibserot.github.io/electronics-catalog/" + quote(rel_url, safe="/")

def fallback_id_for(md: Path, fm: dict) -> str:
    fid = (fm.get("id") or "").strip() if isinstance(fm, dict) else ""
    if fid:
        return fid
    return md.stem.upper()

def parse_id(comp_id: str):
    m = ID_RE.match(comp_id)
    if not m:
        return None, None, None, False
    cat = m.group(1)
    num = int(m.group(2))
    hund = (num // 100) % 10
    is_anchor = (num % 100 == 0)
    return cat, num, hund, is_anchor

def next_number(used_nums):
    for n in range(1, 1000):
        if n not in used_nums:
            return f"{n:03d}"
    return None

def next_in_family(used_nums, hund):
    base = hund * 100
    if base not in used_nums:
        return f"{base:03d}"
    for off in range(0, 100):
        n = base + off
        if n not in used_nums:
            return f"{n:03d}"
    return None

def main():
    all_md = sorted(COMPONENTS.rglob("*.md"))
    items = []
    warnings = []

    for md in all_md:
        try:
            text = md.read_text(encoding="utf-8")
        except Exception as e:
            warnings.append(f"read-error: {md}: {e}")
            continue
        fm, _ = parse_front_matter(text)

        comp_id = fallback_id_for(md, fm)
        cat, num, hund, is_anchor = parse_id(comp_id)
        if cat is None:
            warnings.append(f"skip-nonstandard-id: {comp_id} at {md}")
            continue

        name = (fm.get("name") or "").strip() if isinstance(fm, dict) else ""
        if not name:
            name = (md.parent.name if md.name.lower()=="index.md" else md.stem)

        items.append({
            "id": comp_id,
            "name": name,
            "category": cat,
            "number": num,
            "hundreds": hund,
            "is_family_anchor": is_anchor and (md.name.lower() == "index.md"),
            "url": build_page_url(md),
            "source": str(md.relative_to(DOCS))
        })

    # Build anchors map first (only valid if anchor file is index.md)
    anchors = set()
    anchor_name = {}
    for it in items:
        if it["is_family_anchor"]:
            fam_key = f'{it["category"]}{it["hundreds"]}xx'
            anchors.add(fam_key)
            anchor_name[fam_key] = it["name"]

    # Families: only create if anchor exists
    families = {}
    used_by_cat = {}

    for it in items:
        cat, num, hund = it["category"], it["number"], it["hundreds"]
        used_by_cat.setdefault(cat, set()).add(num)
        fam_key = f"{cat}{hund}xx"
        if fam_key not in anchors:
            continue  # ignore non-anchored families
        fam = families.setdefault(fam_key, {
            "key": fam_key,
            "anchor": f"{cat}{hund}00",
            "alias": anchor_name.get(fam_key),
            "members": []
        })
        fam["members"].append(it["id"])

    # sort family members
    def id_num(cid):
        m = ID_RE.match(cid)
        return int(m.group(2)) if m else 0
    for fam in families.values():
        fam["members"] = sorted(fam["members"], key=id_num)

    # categories: build for ALL predefined categories
    categories = {}
    for cat_code, cat_title in CATEGORY_TITLES.items():
        nums = sorted(used_by_cat.get(cat_code, set()))
        next_any = next_number(set(nums)) if nums else "001"
        # next_by_family ONLY for families that exist (anchors present) under this cat
        next_by_family = {}
        # compute hundreds present that have anchors
        fams_in_cat = [fk for fk in anchors if fk.startswith(cat_code)]
        # we still need used numbers for candidate computation
        used = set(nums)
        for fk in sorted(fams_in_cat):
            # derive hundreds digit from fk (last two before 'xx')
            try:
                hund = int(fk[len(cat_code)])
            except Exception:
                continue
            cand = next_in_family(used, hund)
            if cand:
                next_by_family[fk] = f"{cat_code}{cand}"

        categories[cat_code] = {
            "title": cat_title,
            "count": len(nums),
            "used_numbers": nums,
            "next_any": f"{cat_code}{next_any}" if next_any else None,
            "next_by_family": next_by_family
        }

    generated_at = datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z"

    full_payload = {
        "generated_at": generated_at,
        "ids": sorted(items, key=lambda x: (x["category"], x["number"])),
        "categories": categories,
        "families": families,
        "warnings": warnings
    }
    full_path = OUT_DIR / "id_registry.yaml"
    full_path.write_text(yaml.safe_dump(full_payload, sort_keys=False, allow_unicode=True), encoding="utf-8")

    simple_payload = {
        "generated_at": generated_at,
        "categories": {k: {
            "title": v["title"],
            "count": v["count"],
            "next_any": v["next_any"],
            "next_by_family": v["next_by_family"],
        } for k, v in categories.items()},
        "families": {k: {
            "anchor": v["anchor"],
            "alias": v["alias"],
            "members": v["members"],
        } for k, v in families.items()},
    }
    simple_path = OUT_DIR / "id_registry_simple.yaml"
    simple_path.write_text(yaml.safe_dump(simple_payload, sort_keys=False, allow_unicode=True), encoding="utf-8")

    print(f"[ok] Wrote {full_path.relative_to(Path.cwd())}")
    print(f"[ok] Wrote {simple_path.relative_to(Path.cwd())}")

if __name__ == "__main__":
    main()
