#!/usr/bin/env python3
import os, re, csv, sys, io
from pathlib import Path
import yaml
import qrcode
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT  = ROOT / "docs" / "stickers"
OUT.mkdir(exist_ok=True)

PRINTER_META_RE = re.compile(r"<!--\s*printer_meta:(.*?)-->\s*<!--\s*/printer_meta\s*-->", re.S)

def parse_front_matter(text):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            yml = text[3:end+1]
            body = text[end+4:]
            return yaml.safe_load(yml) or {}, body
    return {}, text

def parse_printer_meta(text):
    m = PRINTER_META_RE.search(text)
    if not m: return {}
    raw = m.group(1)
    # allow YAML inside the comment
    try: return yaml.safe_load(raw) or {}
    except Exception: return {}

def make_label_png(title, lines, url, out_path):
    # QR
    qr = qrcode.QRCode(border=1, box_size=4)
    qr.add_data(url); qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("L")
    # canvas
    W = qr_img.width + 280
    H = max(qr_img.height, 150)
    img = Image.new("L", (W, H), 255)
    img.paste(qr_img, (10, (H - qr_img.height)//2))
    d = ImageDraw.Draw(img)
    x = qr_img.width + 24; y = 12
    d.text((x, y), title, fill=0); y += 26
    for line in (lines or [])[:3]:
        d.text((x, y), line, fill=0); y += 20
    # small URL line at bottom (optional)
    d.text((x, H-20), url, fill=0)
    img.save(out_path)

rows = []
for md in sorted(DOCS.glob("*.md")):
    if md.name == "index.md": continue
    text = md.read_text(encoding="utf-8")
    fm, body = parse_front_matter(text)
    meta = parse_printer_meta(text)

    id_   = fm.get("id", "")
    name  = fm.get("name", md.stem)
    short = fm.get("short", "")
    use   = fm.get("use", "")
    url   = (meta.get("qr_url") or fm.get("qr_url") or
             f"https://<yourname>.github.io/electronics-catalog/{md.stem}/")

    title = meta.get("title") or f"{name} ({id_ or md.stem})"
    lines = meta.get("lines") or [short, f"Use: {use}"] if (short or use) else []

    out_png = OUT / f"{id_ or md.stem}.png"
    make_label_png(title, lines, url, out_png)

    rows.append({
        "id": id_ or md.stem,
        "name": name,
        "url": url,
        "label_png": str(out_png.relative_to(ROOT))
    })
    print(f"Built {out_png}")

# inventory CSV
with open(OUT / "index.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["id","name","url","label_png"])
    w.writeheader(); w.writerows(rows)
print("Wrote stickers/index.csv")

