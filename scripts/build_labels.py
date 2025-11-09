#!/usr/bin/env python3
from pathlib import Path
import re, csv, json
import yaml
from PIL import Image, ImageDraw, ImageFont
import qrcode
from urllib.parse import quote

# ----------------- Preset -----------------
PRESET = "large"   # "compact" or "large"

# --------------- Paths --------------------
ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "components"
OUT  = DOCS / "stickers"
FONTS_DIR = ROOT / "fonts"
OUT.mkdir(parents=True, exist_ok=True)

ASSIGNMENT_PATH = OUT / "assignment.json"   # persistent order of IDs

# ----------- Printer/layout ---------------
MAX_WIDTH = 384           # exact print width in dots for T02
QR_BORDER = 1

DPI = 203
LABEL_HEIGHT_MM = 25
LABEL_HEIGHT_PX = int(round(LABEL_HEIGHT_MM / 25.4 * DPI))  # ≈199 px

# Layout between labels
LABEL_GAP_PX = 8          # vertical gap between labels

# Dividers / guides
DRAW_H_DIVIDER = True     # 1px centered line in the gap
H_DIV_THICK    = 1

DRAW_SHEET_TOP_BOTTOM = True  # 1px line at very top and bottom of sheet

# Vertical cut bar (optional, off by default)
DRAW_VERTICAL_CUT_LINE = False
CUT_LINE_INSET = 6
CUT_LINE_WIDTH = 3

# Common paddings
PADDING_LEFT    = 8
TEXT_LEFT_GAP   = 14
TEXT_RIGHT_PAD  = 8
TOP_PADDING     = 2
BOTTOM_PADDING  = 2
MAX_INFO_LINES  = 5

# Per-preset sizing
if PRESET == "large":
    TITLE_FONT_SIZE  = 20
    LINE_FONT_SIZE   = 16
    SMALL_FONT_SIZE  = 13
    LINE_SPACING     = 20
    TITLE_SPACING    = 24
    TEXT_SCALE       = 3
else:
    TITLE_FONT_SIZE  = 17
    LINE_FONT_SIZE   = 15
    SMALL_FONT_SIZE  = 12
    LINE_SPACING     = 18
    TITLE_SPACING    = 22
    TEXT_SCALE       = 2


# -------- Short QR mode (uniform sizes) --------
SHORT_QR_MODE = True   # if True, generate docs/components/qr/<ID>/index.html redirects
QR_SHORT_PREFIX = "https://thibserot.github.io/electronics-catalog/qr/"
QR_STUB_ROOT = DOCS / "qr"

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
    """Parse YAML front-matter strictly at the start of the file.

    Supports optional UTF-8 BOM and CRLF line endings.
    Returns (front_matter_dict, body_text). If no front-matter is found,
    returns ({}, original_text).
    """
    if text.startswith("\ufeff"):
        text_wo_bom = text[1:]
        had_bom = True
    else:
        text_wo_bom = text
        had_bom = False

    if not (text_wo_bom.startswith("---\n") or text_wo_bom.startswith("---\r\n")):
        return {}, text

    lines = text_wo_bom.splitlines(keepends=True)
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

    yml_text = "".join(yml_lines)
    body = "".join(lines[i:])

    try:
        fm = yaml.safe_load(yml_text) or {}
        if not isinstance(fm, dict):
            fm = {}
    except Exception:
        fm = {}

    if had_bom:
        body = "\ufeff" + body

    return fm, body

def parse_printer_meta(text: str):
    m = PRINTER_META_RE.search(text)
    if not m:
        return {}
    raw = m.group(1)
    try:
        return yaml.safe_load(raw) or {}
    except Exception:
        return {}

def wrap_to_width(text: str, font, max_w, draw):
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

def render_text_panel(title, info_lines, code, height, width):
    """Render text within EXACT height. Top-aligned, no overflow."""
    SCALE = TEXT_SCALE
    w_hi = width * SCALE
    h_hi = height * SCALE
    img_hi = Image.new("L", (w_hi, h_hi), 255)
    d = ImageDraw.Draw(img_hi)

    font_title = load_font(FONTS_DIR / "DejaVuSans-Bold.ttf", TITLE_FONT_SIZE * SCALE) or FONT_BOLD
    font_line  = load_font(FONTS_DIR / "DejaVuSans.ttf",      LINE_FONT_SIZE  * SCALE) or FONT_REG_16
    font_small = load_font(FONTS_DIR / "DejaVuSans.ttf",      SMALL_FONT_SIZE * SCALE) or FONT_REG_13

    def line_h(kind="line"):
        return {
            "title": TITLE_SPACING * SCALE,
            "line":  LINE_SPACING * SCALE,
            "small": (SMALL_FONT_SIZE * SCALE)
        }[kind]

    def ellipsize(txt, font, max_w):
        if d.textlength(txt, font=font) <= max_w:
            return txt
        if len(txt) <= 1:
            return txt
        t = txt
        while d.textlength(t + "...", font=font) > max_w and len(t) > 1:
            t = t[:-1]
        return t + "..."

    # Prepare wrapped lines
    title_wrapped = wrap_to_width(title, font_title, w_hi, d) or [""]
    title_wrapped = title_wrapped[:2]
    if title_wrapped:
        title_wrapped[-1] = ellipsize(title_wrapped[-1], font_title, w_hi)

    info_wrapped = []
    for ln in info_lines or []:
        info_wrapped += wrap_to_width(ln, font_line, w_hi, d)
    info_wrapped = info_wrapped[:MAX_INFO_LINES]

    top_pad  = TOP_PADDING * SCALE
    foot_h   = line_h("small") + (BOTTOM_PADDING * SCALE)

    # Compute space
    y = top_pad
    for _ in title_wrapped:
        y += line_h("title")

    remaining = max(0, h_hi - y - foot_h)
    can_fit = max(0, remaining // line_h("line"))
    info_wrapped = info_wrapped[:can_fit]

    # Draw
    img_hi = Image.new("L", (w_hi, h_hi), 255)
    d = ImageDraw.Draw(img_hi)
    y = top_pad
    for t in title_wrapped:
        d.text((0, y), t, fill=0, font=font_title)
        y += line_h("title")
    for ln in info_wrapped:
        d.text((0, y), ln, fill=0, font=font_line)
        y += line_h("line")

    code_y = h_hi - (SMALL_FONT_SIZE * SCALE) - (BOTTOM_PADDING * SCALE)
    d.text((0, code_y), code, fill=0, font=font_small)

    return img_hi.resize((width, height), Image.LANCZOS)

def compute_qr_for_height(data: str, target_h: int, border: int):
    # Probe for module count
    probe = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L, border=border, box_size=1)
    probe.add_data(data)
    probe.make(fit=True)
    modules = probe.modules_count + 2 * border
    # Choose integer box size so total height <= target_h
    box = max(3, min(10, target_h // modules))  # clamp for readability
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L, border=border, box_size=box)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("L")
    return img

def make_label_png(title, lines, url, code, out_path):
    # Build QR sized to fit the fixed label height
    qr_img = compute_qr_for_height(url, LABEL_HEIGHT_PX, QR_BORDER)

    # Text width
    fixed = PADDING_LEFT + qr_img.width + TEXT_LEFT_GAP + TEXT_RIGHT_PAD
    text_col_w = max(120, MAX_WIDTH - fixed)

    # Text panel *exactly* same height as QR
    text_panel = render_text_panel(title, lines, code, qr_img.height, text_col_w)

    # Compose exactly MAX_WIDTH x LABEL_HEIGHT_PX
    W = MAX_WIDTH
    H = LABEL_HEIGHT_PX
    img = Image.new("L", (W, H), 255)

    # Top-align both blocks so text never exceeds QR vertically
    qr_y = 0
    text_y = 0

    img.paste(qr_img, (PADDING_LEFT, qr_y))
    text_x = PADDING_LEFT + qr_img.width + TEXT_LEFT_GAP
    img.paste(text_panel, (text_x, text_y))

    img.save(out_path)
    return img


def ensure_redirect_stub(comp_id: str, target_url: str):
    d = QR_STUB_ROOT / comp_id
    d.mkdir(parents=True, exist_ok=True)
    html = f"""<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="refresh" content="0; url={target_url}">
    <title>{comp_id}</title>
  </head>
  <body>
    <p>Redirecting to <a href="{target_url}">{target_url}</a></p>
  </body>
</html>"""
    (d / "index.html").write_text(html, encoding="utf-8")


def load_assignment():
    if ASSIGNMENT_PATH.exists():
        try:
            data = json.loads(ASSIGNMENT_PATH.read_text(encoding="utf-8"))
            if isinstance(data, dict) and "order" in data and isinstance(data["order"], list):
                return data["order"]
        except Exception:
            pass
    return []

def save_assignment(order):
    ASSIGNMENT_PATH.write_text(json.dumps({"order": order}, indent=2), encoding="utf-8")

def build_order(comp_ids):
    prev = load_assignment()
    keep = [cid for cid in prev if cid in comp_ids]
    new  = sorted([cid for cid in comp_ids if cid not in prev])
    order = keep + new
    save_assignment(order)
    return order

def pack_sheets_stable(id_to_img, order):
    from PIL import Image

    img_map = {cid: Image.open(path).convert("L") for cid, path in id_to_img.items()}
    seq = [cid for cid in order if cid in img_map]

    sheets_meta = []
    positions = []

    sheet_index = 1
    i = 0
    while i < len(seq):
        chunk = seq[i:i+4]
        images = [img_map[cid] for cid in chunk]
        total_h = sum(im.height for im in images) + LABEL_GAP_PX * max(0, len(images) - 1)
        sheet = Image.new("L", (MAX_WIDTH, total_h), 255)
        d = ImageDraw.Draw(sheet)
        y = 0
        for pos, (cid, im) in enumerate(zip(chunk, images), start=1):
            sheet.paste(im, (0, y))
            y += im.height
            if pos < len(images):
                if DRAW_H_DIVIDER:
                    y_mid = y + LABEL_GAP_PX // 2
                    y0 = max(0, min(total_h - 1, y_mid - H_DIV_THICK // 2))
                    y1 = max(0, min(total_h - 1, y0 + H_DIV_THICK - 1))
                    d.rectangle([0, y0, MAX_WIDTH - 1, y1], fill=0)
                y += LABEL_GAP_PX
        if DRAW_SHEET_TOP_BOTTOM:
            d.rectangle([0, 0, MAX_WIDTH - 1, 0], fill=0)
            d.rectangle([0, total_h - 1, MAX_WIDTH - 1, total_h - 1], fill=0)
        if DRAW_VERTICAL_CUT_LINE:
            x0 = max(0, min(MAX_WIDTH - 1, MAX_WIDTH - CUT_LINE_INSET))
            x1 = max(0, min(MAX_WIDTH - 1, x0 + CUT_LINE_WIDTH - 1))
            d.rectangle([x0, 0, x1, total_h - 1], fill=0)

        out_name = f"sheet_{sheet_index:03d}.png"
        out_path = OUT / out_name
        sheet.save(out_path)

        sheets_meta.append({"sheet": out_name, "height_px": total_h, "labels": len(images)})
        for pos, cid in enumerate(chunk, start=1):
            positions.append({"sheet": out_name, "position": pos, "id": cid})

        sheet_index += 1
        i += len(chunk)

    with open(OUT / "sheet_positions.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["sheet","position","id"])
        w.writeheader()
        w.writerows(positions)

    return sheets_meta

# ----------------- URL helpers -----------------
def build_page_url(md: Path) -> str:
    rel = md.relative_to(DOCS).with_suffix('')
    if md.name.lower() == "index.md":
        rel_url = f"components/{rel.parent.as_posix()}/"
    else:
        rel_url = f"components/{rel.as_posix()}/"
    return "https://thibserot.github.io/electronics-catalog/" + quote(rel_url, safe="/")

def fallback_id_for(md: Path, fm: dict) -> str:
    fid = (fm.get("id") or "").strip() if isinstance(fm, dict) else ""
    if fid:
        return fid
    rel = md.relative_to(DOCS).with_suffix('')
    if md.name.lower() == "index.md":
        folder = rel.parent.name.strip() or "index"
        unique = str(rel).replace("/", "_")
        return f"{folder}__{unique}"
    return md.stem

def main():
    rows = []
    id_to_path = {}

    all_md_files = sorted(DOCS.rglob("*.md"))

    for md in all_md_files:
        text = md.read_text(encoding="utf-8")
        fm, _ = parse_front_matter(text)
        meta = parse_printer_meta(text)

        if isinstance(fm, dict) and fm.get("no_label") is True:
            continue

        comp_id   = fallback_id_for(md, fm)
        comp_name = (fm.get("name") or "").strip() if isinstance(fm, dict) else ""
        short     = (fm.get("short") or "").strip() if isinstance(fm, dict) else ""
        use       = (fm.get("use")   or "").strip() if isinstance(fm, dict) else ""

        full_url = (meta.get("qr_url") if meta else None) or (fm.get("qr_url") if isinstance(fm, dict) else None) or build_page_url(md)
        url = full_url
        if SHORT_QR_MODE:
            ensure_redirect_stub(comp_id, full_url)
            url = QR_SHORT_PREFIX + comp_id + "/"
        title = (meta.get("title") if meta else None) or comp_name or (md.stem if md.name.lower() != "index.md" else md.parent.name)

        lines = (meta.get("lines") if meta else None)
        if not lines:
            lines = []
            if short: lines.append(short)
            if use:   lines.append(use)

        out_png = OUT / f"{comp_id}.png"
        make_label_png(title, lines, url, code=comp_id, out_path=out_png)
        id_to_path[comp_id] = out_png

        rows.append({
            "id": comp_id,
            "name": comp_name or (md.parent.name if md.name.lower()=="index.md" else md.stem),
            "url": url,
            "label_png": str(out_png.relative_to(DOCS))
        })

    with open(OUT / "index.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["id","name","url","label_png"])
        w.writeheader()
        w.writerows(rows)

    order = build_order(sorted(id_to_path.keys()))
    sheets_meta = pack_sheets_stable(id_to_path, order)
    if sheets_meta:
        with open(OUT / "sheets.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["sheet","height_px","labels"])
            w.writeheader()
            w.writerows(sheets_meta)

if __name__ == "__main__":
    main()
