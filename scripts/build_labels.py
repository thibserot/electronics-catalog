#!/usr/bin/env python3
"""
Build QR labels for each component page (T02-friendly).
- QR left (sharp), wrapped text right (hi-DPI then LANCZOS downscale).
- Title aligns to TOP of QR; code aligns to BOTTOM of QR (same total height).
- Title shows NAME only; footer shows CODE; URL only inside QR.
- Output: docs/stickers/<ID>.png and docs/stickers/index.csv
"""

from pathlib import Path
import re, csv, yaml
import qrcode
from PIL import Image, ImageDraw, ImageFont

# ---------------- Paths ----------------
ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT  = DOCS / "stickers"
FONTS_DIR = ROOT / "fonts"
OUT.mkdir(parents=True, exist_ok=True)

# ------------- Printer/layout ----------
MAX_WIDTH = 384          # T02 (58mm). Use 576 for 80mm printers.
QR_BOX_SIZE = 3          # smaller QR leaves more room for text; raise to 4 if needed
QR_BORDER   = 1

# Logical (pre-2x) text layout
TITLE_FONT_SIZE = 18
LINE_FONT_SIZE  = 16
SMALL_FONT_SIZE = 13
LINE_SPACING    = 20
TITLE_SPACING   = 24
TEXT_COL_WIDTH  = 260     # width of text column in final pixels
PADDING_LEFT    = 8
TEXT_LEFT_GAP   = 14
TEXT_RIGHT_PAD  = 8
TOP_PADDING     = 4       # small breathing room above title
BOTTOM_PADDING  = 4       # small breathing room below code
MAX_INFO_LINES  = 4       # total wrapped lines allowed (excludes title). Extra text gets ellipsis.

# --------- Optional metadata block -----
PRINTER_META_RE = re.compile(
    r"<!--\s*printer_meta:(.*?)-->\s*<!--\s*/printer_meta\s*-->",
    re.S
)

# ---------------- Fonts ----------------
def load_font(path: Path, size: int):
    try:
        return ImageFont.truetype(str(path), size)
    except Exception:
        return None

FONT_BOLD   = load_font(FONTS_DIR / "DejaVuSans-Bold.ttf", TITLE_FONT_SIZE) or ImageFont.load_default()
FONT_REG_16 = load_font(FONTS_DIR / "DejaVuSans.ttf",      LINE_FONT_SIZE)  or ImageFont.load_default()
FONT_REG_13 = load_font(FONTS_DIR / "DejaVuSans.ttf",      SMALL_FONT_SIZE) or ImageFont.load_default()

# --------------- Helpers ---------------
def parse_front_matter(text: str):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            yml = text[3:end+1]
            body = text[end+4:]
            return yaml.safe_load(yml) or {}, body
    return {}, text

def parse_printer_meta(text: str):
    m = PRINTER_META_RE.search(text)
    if not m:
        return {}
    raw = m.group(1)
    try:
        return yaml.safe_load(raw) or {}
    except Exception:
        return {}

def wrap_to_width(text: str, font: ImageFont.FreeTypeFont, max_w: int, draw: ImageDraw.ImageDraw):
    """Greedy wrap by measuring with the actual font; returns list of lines."""
    words = text.split()
    if not words:
        return []
    lines, cur = [], words[0]
    for w in words[1:]:
        test = cur + " " + w
        if draw.textlength(test, font=font) <= max_w:
            cur = test
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines

def render_text_panel(title: str, info_lines: list[str], code: str, height: int) -> Image.Image:
    """
    Render the right-hand text panel to EXACTLY 'height' pixels tall (so it matches the QR).
    Do the text at 2x scale for smooth downsampling.
    """
    SCALE = 2
    w_hi = TEXT_COL_WIDTH * SCALE
    h_hi = height * SCALE

    img_hi = Image.new("L", (w_hi, h_hi), 255)
    d = ImageDraw.Draw(img_hi)

    # Double-sized fonts for hi-res render
    font_title = load_font(FONTS_DIR / "DejaVuSans-Bold.ttf", TITLE_FONT_SIZE * SCALE) or FONT_BOLD
    font_line  = load_font(FONTS_DIR / "DejaVuSans.ttf",      LINE_FONT_SIZE  * SCALE) or FONT_REG_16
    font_small = load_font(FONTS_DIR / "DejaVuSans.ttf",      SMALL_FONT_SIZE * SCALE) or FONT_REG_13

    x = 0
    y = TOP_PADDING * SCALE

    # Title at TOP
    d.text((x, y), title, fill=0, font=font_title)
    y += TITLE_SPACING * SCALE

    # Wrap each info line to width, then cap total lines
    wrapped = []
    for line in info_lines or []:
        wrapped += wrap_to_width(line, font_line, w_hi, d)
        if len(wrapped) >= MAX_INFO_LINES:
            wrapped = wrapped[:MAX_INFO_LINES]
            # append ellipsis to last line if we truncated
            if len(wrapped[-1]) > 3:
                wrapped[-1] = wrapped[-1].rstrip(".") + "..."
            break

    for ln in wrapped:
        d.text((x, y), ln, fill=0, font=font_line)
        y += LINE_SPACING * SCALE

    # Footer code at BOTTOM
    code_y = h_hi - (SMALL_FONT_SIZE * SCALE) - (BOTTOM_PADDING * SCALE)
    d.text((x, code_y), code, fill=0, font=font_small)

    # Downscale to final size with LANCZOS for smooth text
    img = img_hi.resize((TEXT_COL_WIDTH, height), Image.LANCZOS)
    return img

def make_label_png(title: str, lines: list[str], url: str, code: str, out_path: Path):
    """
    Compose final label: QR (native sharp) + text panel with top/bottom alignment to QR.
    """
    # Build QR at native pixel size (kept sharp)
    qr = qrcode.QRCode(border=QR_BORDER, box_size=QR_BOX_SIZE)
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("L")

    # Text panel height EXACTLY equals QR height
    text_panel = render_text_panel(title, lines, code, qr_img.height)

    # Compose with same height
    W = PADDING_LEFT + qr_img.width + TEXT_LEFT_GAP + text_panel.width + TEXT_RIGHT_PAD
    H = qr_img.height

    img = Image.new("L", (W, H), 255)
    # QR aligned to TOP
    img.paste(qr_img, (PADDING_LEFT, 0))
    # Text panel aligned to TOP and BOTTOM matches QR by construction
    text_x = PADDING_LEFT + qr_img.width + TEXT_LEFT_GAP
    img.paste(text_panel, (text_x, 0))

    # Cap width for printer; global downscale with LANCZOS (QR stays readable)
    if img.width > MAX_WIDTH:
        scale = MAX_WIDTH / img.width
        new_h = int(img.height * scale)
        img = img.resize((MAX_WIDTH, new_h), Image.LANCZOS)

    img.save(out_path)

# ----------------- Main ----------------
def main():
    rows = []
    for md in sorted(DOCS.glob("*.md")):
        if md.name.lower() == "index.md":
            continue

        text = md.read_text(encoding="utf-8")
        fm, _ = parse_front_matter(text)
        meta = parse_printer_meta(text)

        comp_id   = (fm.get("id")   or md.stem).strip()
        comp_name = (fm.get("name") or md.stem).strip()
        short     = (fm.get("short") or "").strip()
        use       = (fm.get("use")   or "").strip()

        # Default URL points to your GitHub Pages username
        url = (meta.get("qr_url")
               or fm.get("qr_url")
               or f"https://thibserot.github.io/electronics-catalog/{md.stem}/").strip()

        title = (meta.get("title") or comp_name).strip()

        # Info lines: meta.lines overrides derived lines
        lines = meta.get("lines")
        if not lines:
            lines = []
            if short:
                lines.append(short)
            if use:
                lines.append(f"Use: {use}")

        out_png = OUT / f"{comp_id}.png"
        make_label_png(title, lines, url, code=comp_id, out_path=out_png)

        rows.append({
            "id": comp_id,
            "name": comp_name,
            "url": url,
            "label_png": str(out_png.relative_to(DOCS))
        })
        print(f"Built {out_png}")

    # Inventory CSV
    csv_path = OUT / "index.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["id","name","url","label_png"])
        w.writeheader()
        w.writerows(rows)
    print(f"Wrote {csv_path}")

if __name__ == "__main__":
    main()

