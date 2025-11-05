#!/usr/bin/env python3
"""
Build QR labels for each component page (T02-friendly), and also pack multiple
labels into tall 'sheets' you can print at once (<= 50mm x 150mm).

Tweaks:
- Vertical cut bar is now OPTIONAL and defaults to OFF.
- Draw a single horizontal divider centered in each gap between labels.
- Keep 8 px gap; divider is precisely centered in that gap.
"""

from pathlib import Path
import re
import csv
import yaml
from PIL import Image, ImageDraw, ImageFont
import qrcode

# ----------------- Preset -----------------
PRESET = "large"   # "compact" or "large"

# --------------- Paths --------------------
ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "components"
OUT  = DOCS / "stickers"
FONTS_DIR = ROOT / "fonts"
OUT.mkdir(parents=True, exist_ok=True)

# ----------- Printer/layout ---------------
# T02 width: 58mm class paper, printable width ~384 dots at 203 dpi (≈48mm).
MAX_WIDTH = 384
QR_BORDER = 1

# Cut/packing settings
DPI = 203
SHEET_MAX_HEIGHT_MM = 150        # tallest you can configure
SHEET_MAX_H = int(round(SHEET_MAX_HEIGHT_MM / 25.4 * DPI))   # ≈1200 px

# Gap between stacked labels so you don’t cut into a QR
LABEL_GAP_PX = 8

# Horizontal divider (centered in the gap)
DRAW_H_DIVIDER = True
H_DIV_THICK = 1                   # 1 px looks crisp on T02

# Vertical cut bar (optional guide near the right edge)
DRAW_VERTICAL_CUT_LINE = False     # default off (you can set True if you want it)
CUT_LINE_INSET = 6                 # px from right edge (avoid clipping)
CUT_LINE_WIDTH = 3                 # width of the vertical bar

# Common paddings
PADDING_LEFT    = 8
TEXT_LEFT_GAP   = 14
TEXT_RIGHT_PAD  = 8
TOP_PADDING     = 4
BOTTOM_PADDING  = 4
MAX_INFO_LINES  = 5

# Per-preset sizing
if PRESET == "large":
    QR_BOX_SIZE      = 4
    TITLE_FONT_SIZE  = 20
    LINE_FONT_SIZE   = 16
    SMALL_FONT_SIZE  = 13
    LINE_SPACING     = 20
    TITLE_SPACING    = 24
    TEXT_SCALE       = 3
else:  # compact
    QR_BOX_SIZE      = 3
    TITLE_FONT_SIZE  = 17
    LINE_FONT_SIZE   = 15
    SMALL_FONT_SIZE  = 12
    LINE_SPACING     = 18
    TITLE_SPACING    = 22
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
    """Return (front_matter_dict, body_text)."""
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n?(.*)\Z', text, re.S)
    if m:
        yml = m.group(1)
        body = m.group(2)
        try:
            return yaml.safe_load(yml) or {}, body
        except Exception:
            return {}, text
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

def render_text_panel(title: str, info_lines, code: str, height: int, width: int) -> Image.Image:
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

    # ---- Title at TOP, allow up to 2 lines with ellipsis ----
    TITLE_MAX_LINES = 2
    title_lines = wrap_to_width(title, font_title, w_hi, d)
    if len(title_lines) > TITLE_MAX_LINES:
        title_lines = title_lines[:TITLE_MAX_LINES]
        if len(title_lines[-1]) > 3:
            while d.textlength(title_lines[-1] + "...", font=font_title) > w_hi and len(title_lines[-1]) > 1:
                title_lines[-1] = title_lines[-1][:-1]
            title_lines[-1] += "..."

    for tl in title_lines:
        d.text((x, y), tl, fill=0, font=font_title)
        y += TITLE_SPACING * SCALE

    # ---- Body lines (wrapped, capped) ----
    wrapped = []
    for line in info_lines or []:
        wrapped += wrap_to_width(line, font_line, w_hi, d)
        if len(wrapped) >= MAX_INFO_LINES:
            wrapped = wrapped[:MAX_INFO_LINES]
            if len(wrapped[-1]) > 3:
                while d.textlength(wrapped[-1] + "...", font=font_line) > w_hi and len(wrapped[-1]) > 1:
                    wrapped[-1] = wrapped[-1][:-1]
                wrapped[-1] += "..."
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

def make_label_png(title: str, lines, url: str, code: str, out_path: Path) -> Image.Image:
    """
    Compose final label: QR (native sharp) + text panel with top/bottom alignment to QR.
    The text column width is computed so the final width equals MAX_WIDTH.
    Returns the PIL image (and saves it).
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
    return img

def pack_sheets(label_paths):
    """
    Read individual label PNGs (all MAX_WIDTH wide, variable heights),
    stack them top-to-bottom into sheets not exceeding SHEET_MAX_H.
    Draw a centered horizontal divider in each gap (optional).
    Returns metadata rows for the sheets.csv.
    """
    sheets_meta = []
    sheet_index = 1

    def flush_sheet(labels_for_sheet):
        nonlocal sheet_index
        if not labels_for_sheet:
            return
        total_h = sum(img.height for img in labels_for_sheet) + LABEL_GAP_PX * max(0, len(labels_for_sheet) - 1)
        sheet = Image.new("L", (MAX_WIDTH, total_h), 255)
        d = ImageDraw.Draw(sheet)
        y = 0
        for i, im in enumerate(labels_for_sheet):
            sheet.paste(im, (0, y))
            y += im.height
            if LABEL_GAP_PX and i < len(labels_for_sheet) - 1:
                # centered horizontal divider
                if DRAW_H_DIVIDER:
                    y_mid = y + LABEL_GAP_PX // 2
                    y0 = max(0, min(total_h - 1, y_mid - H_DIV_THICK // 2))
                    y1 = max(0, min(total_h - 1, y0 + H_DIV_THICK - 1))
                    d.rectangle([0, y0, MAX_WIDTH - 1, y1], fill=0)
                y += LABEL_GAP_PX

        # Optional vertical cut bar near the right edge
        if DRAW_VERTICAL_CUT_LINE:
            x0 = max(0, min(MAX_WIDTH - 1, MAX_WIDTH - CUT_LINE_INSET))
            x1 = max(0, min(MAX_WIDTH - 1, x0 + CUT_LINE_WIDTH - 1))
            d.rectangle([x0, 0, x1, total_h - 1], fill=0)

        out_name = f"sheet_{sheet_index:03d}.png"
        out_path = OUT / out_name
        sheet.save(out_path)
        sheets_meta.append({
            "sheet": out_name,
            "height_px": total_h,
            "labels": len(labels_for_sheet),
        })
        sheet_index += 1

    # Load images and group by height budget
    pending_imgs = []
    for p in label_paths:
        try:
            pending_imgs.append(Image.open(p).convert("L"))
        except Exception:
            continue

    cur_labels = []
    cur_h = 0
    for im in pending_imgs:
        need_h = im.height + (LABEL_GAP_PX if cur_labels else 0)
        if cur_h + need_h <= SHEET_MAX_H:
            cur_labels.append(im)
            cur_h += need_h
        else:
            flush_sheet(cur_labels)
            cur_labels = [im]
            cur_h = im.height

    flush_sheet(cur_labels)
    return sheets_meta

# ----------------- Main ------------------
def main():
    rows = []
    built_paths = []

    for md in sorted(DOCS.glob("*.md")):
        if md.name.lower() == "index.md":
            continue

        text = md.read_text(encoding="utf-8")
        fm, _ = parse_front_matter(text)
        meta = parse_printer_meta(text)

        comp_id   = (fm.get("id")   or md.stem).strip()
        comp_name = (fm.get("name") or "").strip()
        short     = (fm.get("short") or "").strip()
        use       = (fm.get("use")   or "").strip()

        # Default URL points to your GitHub Pages username
        url = (meta.get("qr_url")
               or fm.get("qr_url")
               or f"https://thibserot.github.io/electronics-catalog/components/{md.stem}/").strip()

        # Title preference: meta.title > fm.name > md.stem
        title = (meta.get("title") or comp_name or md.stem).strip()

        # Info lines: meta.lines overrides derived lines
        lines = meta.get("lines")
        if not lines:
            lines = []
            if short:
                lines.append(short)
            if use:
                lines.append(use)

        out_png = OUT / f"{comp_id}.png"
        img = make_label_png(title, lines, url, code=comp_id, out_path=out_png)
        built_paths.append(out_png)

        rows.append({
            "id": comp_id,
            "name": comp_name or md.stem,
            "url": url,
            "label_png": str(out_png.relative_to(DOCS))
        })
        print(f"Built {out_png} ({img.width}x{img.height})")

    # Inventory CSV for individual labels
    csv_path = OUT / "index.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["id","name","url","label_png"])
        w.writeheader()
        w.writerows(rows)
    print(f"Wrote {csv_path}")

    # ---- Build sheets (<=50mm x 150mm at 203 dpi) ----
    sheets_meta = pack_sheets(built_paths)
    if sheets_meta:
        sheets_csv = OUT / "sheets.csv"
        with open(sheets_csv, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["sheet","height_px","labels"])
            w.writeheader()
            w.writerows(sheets_meta)
        print(f"Wrote {sheets_csv}")

if __name__ == "__main__":
    main()
