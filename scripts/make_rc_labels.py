#!/usr/bin/env python3
"""
Generate resistor & capacitor label images for a Phomemo T02-style printer.

- Resistor input: values in ohms (e.g. 4700 -> "4.7 kΩ").
- Capacitor input: values in microfarads (µF) (e.g. 4.7 -> "4.7 µF").
- Output: two PNGs (2 values per row, no headers), sized for a 384px-wide printer.
"""

import argparse
import os
from typing import List, Tuple

from PIL import Image, ImageDraw, ImageFont


# ---------- Formatting helpers ----------

def format_resistor(ohms: float) -> str:
    abs_val = abs(ohms)
    if abs_val >= 1_000_000:
        v = ohms / 1_000_000
        unit = "MΩ"
    elif abs_val >= 1_000:
        v = ohms / 1_000
        unit = "kΩ"
    else:
        v = ohms
        unit = "Ω"

    if v == int(v):
        return f"{int(v)} {unit}"
    else:
        return f"{v:.2f}".rstrip("0").rstrip(".") + f" {unit}"


def format_capacitor(uf: float) -> str:
    if uf == int(uf):
        return f"{int(uf)} µF"
    else:
        return f"{uf:.2f}".rstrip("0").rstrip(".") + " µF"


def chunk_two(values: List[str]) -> List[Tuple[str, str]]:
    pairs = []
    for i in range(0, len(values), 2):
        left = values[i]
        right = values[i + 1] if i + 1 < len(values) else ""
        pairs.append((left, right))
    return pairs


# ---------- Font helper ----------

def get_font(font_path: str, font_size: int) -> ImageFont.FreeTypeFont:
    if font_path:
        return ImageFont.truetype(font_path, font_size)

    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans.ttf",
        "C:\\Windows\\Fonts\\arial.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, font_size)

    print("Warning: using PIL default font (Ω/µ may not render). "
          "Specify --font for better results.")
    return ImageFont.load_default()


# ---------- Image generation ----------

def build_two_column_label(
    values: List[float],
    formatter,
    out_path: str,
    label_width: int = 384,
    margin: int = 8,
    col_gap: int = 4,
    row_gap: int = 16,      # NEW: extra pixels between lines
    font_path: str = None,
    font_size: int = 32,
):
    if not values:
        print(f"No values for {out_path}, skipping.")
        return

    formatted = [formatter(v) for v in values]
    pairs = chunk_two(formatted)

    font = get_font(font_path, font_size)

    # Measure text height, then add row_gap
    tmp_img = Image.new("L", (label_width, 100), "white")
    tmp_draw = ImageDraw.Draw(tmp_img)
    bbox = tmp_draw.textbbox((0, 0), "Ag", font=font)
    text_height = bbox[3] - bbox[1]
    line_height = text_height + row_gap

    num_lines = max(len(pairs), 1)
    height = margin * 2 + line_height * num_lines

    img = Image.new("L", (label_width, height), "white")
    draw = ImageDraw.Draw(img)

    col_width = (label_width - 2 * margin - col_gap) / 2
    y = margin

    for left, right in pairs:
        # Left cell centered in left half
        if left:
            bbox = draw.textbbox((0, 0), left, font=font)
            text_w = bbox[2] - bbox[0]
            x_left = int(round(margin + (col_width - text_w) / 2))
            draw.text((x_left, y), left, fill="black", font=font)

        # Right cell centered in right half
        if right:
            bbox = draw.textbbox((0, 0), right, font=font)
            text_w = bbox[2] - bbox[0]
            x_base = margin + col_width + col_gap
            x_right = int(round(x_base + (col_width - text_w) / 2))
            draw.text((x_right, y), right, fill="black", font=font)

        y += line_height

    img.save(out_path)
    print(f"Saved {out_path} ({label_width}x{height})")


# ---------- CLI ----------

def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate resistor & capacitor label images for a thermal printer."
    )
    parser.add_argument(
        "--resistors", "-r",
        nargs="*",
        type=float,
        default=[],
        help="Resistor values in ohms (e.g. 10 22 47 100 4700 10000).",
    )
    parser.add_argument(
        "--capacitors", "-c",
        nargs="*",
        type=float,
        default=[],
        help="Capacitor values in microfarads (µF) (e.g. 0.1 0.22 4.7 10 100).",
    )
    parser.add_argument(
        "--output-prefix", "-o",
        default="rc_labels",
        help="Prefix for output files (default: rc_labels).",
    )
    parser.add_argument(
        "--width",
        type=int,
        default=384,
        help="Label width in pixels (default: 384 for T02).",
    )
    parser.add_argument(
        "--font-size",
        type=int,
        default=32,
        help="Font size (default: 32).",
    )
    parser.add_argument(
        "--font",
        type=str,
        default=None,
        help="Path to a .ttf font (e.g. /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf).",
    )
    parser.add_argument(
        "--row-gap",
        type=int,
        default=20,
        help="Extra vertical spacing (pixels) between rows (default: 16).",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    if not args.resistors and not args.capacitors:
        print("No values provided, using example sets.")
        args.resistors = [10, 22, 47, 100, 220, 330, 470, 1000, 2200, 4700, 10000]
        args.capacitors = [0.1, 0.22, 0.47, 1.0, 2.2, 4.7, 10, 22, 47, 100]

    if args.resistors:
        out_res = f"{args.output_prefix}_resistors.png"
        build_two_column_label(
            values=args.resistors,
            formatter=format_resistor,
            out_path=out_res,
            label_width=args.width,
            font_path=args.font,
            font_size=args.font_size,
            row_gap=args.row_gap,
        )

    if args.capacitors:
        out_cap = f"{args.output_prefix}_capacitors.png"
        build_two_column_label(
            values=args.capacitors,
            formatter=format_capacitor,
            out_path=out_cap,
            label_width=args.width,
            font_path=args.font,
            font_size=args.font_size,
            row_gap=args.row_gap,
        )


if __name__ == "__main__":
    main()

