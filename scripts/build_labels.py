#!/usr/bin/env python3
"""
Build QR labels for each component page (T02-friendly).
- Final width is exactly MAX_WIDTH to avoid blurry global rescaling.
- Presets: 'compact' or 'large' (bigger QR + fonts).
- QR left (sharp), wrapped text right (hi-DPI then LANCZOS downscale).
- Title aligns to TOP of QR; code aligns to BOTTOM of QR.
- Title shows NAME only; footer shows CODE; URL only inside QR.
- Output: docs/stickers/<ID>.png and docs/stickers/index.csv
"""

from pathlib import Path
import re, csv, yaml
import qrcode
from PIL import Image, ImageDraw, ImageFont

# ----------------- Preset -----------------
PRESET = "large"   # "compact" or "large"

# --------------- Paths --------------------
ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT  = DOCS / "stickers"
FONTS_DIR = ROOT / "fonts"
OUT.mkdir(parents=True, exist_ok=True)

# ----------- Printer/layout ---------------
MAX_WIDTH = 384          # T02 (58mm). Use 576 for 80mm printers.
QR_BORDER = 1

# Common paddings
PADDING_LEFT    = 8
TEXT_LEFT_GAP   = 14
TEXT_RIGHT_PAD  = 8
TOP_PADDING     = 4
BOTTOM_PADDING  = 4
MAX_INFO_LINES  = 5

# Per-preset sizing
if PRESET == "large":
    # Larger QR and fonts; text rendered at higher DPI for smoothness
    QR_BOX_SIZE      = 4
    TITLE_FONT_SIZE  = 22
    LINE_FONT_SIZE   = 18
    SMALL_FONT_SIZE  = 14
    LINE_SPACING     = 22
    TITLE_SPACING    = 26
    TEXT_SCALE       = 3   # hi-DPI text render factor
else:  # compact
    QR_BOX_SIZE      = 3
    TITLE_FONT_SIZE  = 18
    LINE_FONT_SIZE   = 16
    SMALL_FONT_SIZE  = 13
    LINE_SPACING     = 20
    TITLE_SPACING    = 24
    TEXT_SCALE       = 2

# --------- Optional metadata block --------
PRINTER_META_RE = re.compile(
    r"<!--\s*printer_meta:(.*?)-->\s*<!--\s*/printer_meta\s*-->",
    re.S
)

# ---------------- Fonts -------------------
def load_font(path: Path, size: int):
    try:
        return ImageFont.truetype(str(path), size)
    except Exception:
        return None

FONT_BOLD   = load_font(FONTS_DIR / "DejaVuSans-Bold.ttf", TITLE_FONT_SIZE) or ImageFont.load_default()
FONT_REG_16 = load_font(FONTS_DIR / "DejaVuSans.ttf",      LINE_FONT_SIZE)  or ImageFont.load_default()
FONT_REG_13 = load_font(FONTS_DIR / "DejaVuSans.ttf",      SMALL_FONT_SIZE) or ImageFont.load_default()

# --------------- Helpers ------------------
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

def render_text_panel(title: str, info_lines: list[str], code: str, height: int, width: int) -> Image.Image:
    """
    Render the right-hand text panel to EXACTLY the QR height and the
    computed text column width. Text is drawn at TEXT_SCALE and downsampled
    with LANCZOS to stay smooth on thermal paper.
    """
    SCALE = TEXT_SCALE
    w_hi = width * SCALE
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
    img = img_hi.resize((width, height), Image.LANCZOS)
    return img

def make_label_png(title: str, lines: list[str], url: str, code: str, out_path: Path):
    """
    Compose final label: QR (native sharp) + text panel with top/bottom alignment to QR.
    The text column width is computed so the final image width equals MAX_WIDTH.
    """
    # Build QR at native pixel size (kept sharp)
    qr = qrcode.QRCode(border=QR_BORDER, box_size=QR_BOX_SIZE)
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("L")

    # Compute text column width so total width == MAX_WIDTH (no final scaling)
    fixed = PADDING_LEFT + qr_img.width + TEXT_LEFT_GAP + TEXT_RIGHT_PAD
    text_col_w = max(120, MAX_WIDTH - fixed)  # keep a sane minimum width

    # Render text panel to the exact QR height and computed width
    text_panel = render_text_panel(title, lines, code, qr_img.height, text_col_w)

    # Compose exactly MAX_WIDTH wide
    W = MAX_WIDTH
    H = qr_img.height
    img = Image.new("L", (W, H), 255)
    img.paste(qr_img, (PADDING_LEFT, 0))
    text_x = PADDING_LEFT + qr_img.width + TEXT_LEFT_GAP
    img.paste(text_panel, (text_x, 0))

    img.save(out_path)

# ----------------- Main ------------------
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
                lines.append(use)

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

