#!/usr/bin/env python3
"""
build_registry_page.py
----------------------
Reads docs/components/stickers/id_registry_simple.yaml and generates
docs/registry/index.md with two human-friendly tables:
- Categories (with next suggestions)
- Families (only anchored families)

Run this after generate_id_registry.py.
"""

from pathlib import Path
import sys, yaml, datetime

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SRC  = DOCS / "components" / "stickers" / "id_registry_simple.yaml"
OUTD = DOCS / "registry"
OUTD.mkdir(parents=True, exist_ok=True)
OUT  = OUTD / "index.md"

def fmt_next_by_family(nbf: dict) -> str:
    if not nbf:
        return ""
    parts = [f"{k} → `{v}`" for k, v in sorted(nbf.items())]
    return "<br/>".join(parts)

def main():
    if not SRC.exists():
        print(f"[error] Missing {SRC}. Run generate_id_registry.py first.", file=sys.stderr)
        sys.exit(1)

    data = yaml.safe_load(SRC.read_text(encoding="utf-8")) or {}
    categories = data.get("categories", {})
    families   = data.get("families", {})
    gen_at     = data.get("generated_at", "")

    # Build Categories table
    cat_lines = []
    cat_lines.append("| Code | Title | Count | Next ID | Next by family |")
    cat_lines.append("|---|---|---:|---|---|")
    for code in sorted(categories.keys()):
        c = categories[code] or {}
        next_any = c.get("next_any", "") or ""
        nbf = fmt_next_by_family(c.get("next_by_family", {}) or {})
        title = c.get("title","")
        count = c.get("count",0)
        cat_lines.append(f"| `{code}` | {title} | {count} | `{next_any}` | {nbf} |")

    # Build Families table
    fam_lines = []
    fam_lines.append("| Family | Alias | Anchor | Members |")
    fam_lines.append("|---|---|---|---|")
    for key in sorted(families.keys()):
        f = families[key] or {}
        alias = f.get("alias") or ""
        anch  = f.get("anchor") or ""
        members = f.get("members") or []
        members_str = ", ".join(f"`{m}`" for m in members)
        fam_lines.append(f"| `{key}` | {alias} | `{anch}` | {members_str} |")

    content = f"""---
title: ID Registry
hide:
  - toc
---

# Component ID Registry

_This page is generated from `components/stickers/id_registry_simple.yaml`._  
**Generated:** {gen_at or datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z"}

## Categories
{"\n".join(cat_lines)}

## Families
{"\n".join(fam_lines)}

"""
    OUT.write_text(content, encoding="utf-8")
    print(f"[ok] Wrote {OUT.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
