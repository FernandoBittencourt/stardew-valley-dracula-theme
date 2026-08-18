#!/usr/bin/env python3
"""
Generate Dracula-themed UI PNGs from the player's own Stardew Valley install.

This script never ships ConcernedApe assets in the repository. You must own the
game and point --input at PNGs extracted from YOUR copy (see tools/README.md).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Missing dependency: pip install -r tools/requirements.txt", file=sys.stderr)
    raise SystemExit(1)

ROOT = Path(__file__).resolve().parents[1]
PALETTE_PATH = ROOT / "assets" / "palette.json"

# Relative paths under LooseSprites/ (no extension)
UI_TARGETS = [
    "Cursors",
    "DialogBox",
    "font_bold",
    "font_colored",
    "daybg",
    "nightbg",
    "ChatButtons",
    "JournalIcons",
]


def load_palette() -> dict[str, tuple[int, int, int]]:
    data = json.loads(PALETTE_PATH.read_text(encoding="utf-8"))
    out: dict[str, tuple[int, int, int]] = {}
    for key, value in data.items():
        if key.startswith("#") or not isinstance(value, str):
            continue
        hex_color = value.lstrip("#")
        out[key] = (
            int(hex_color[0:2], 16),
            int(hex_color[2:4], 16),
            int(hex_color[4:6], 16),
        )
    return out


def rgb_to_hsl(r: int, g: int, b: int) -> tuple[float, float, float]:
    r_f, g_f, b_f = r / 255.0, g / 255.0, b / 255.0
    max_c = max(r_f, g_f, b_f)
    min_c = min(r_f, g_f, b_f)
    lightness = (max_c + min_c) / 2.0
    if max_c == min_c:
        return 0.0, 0.0, lightness

    delta = max_c - min_c
    saturation = delta / (2.0 - max_c - min_c) if lightness > 0.5 else delta / (max_c + min_c)

    if max_c == r_f:
        hue = (g_f - b_f) / delta + (6.0 if g_f < b_f else 0.0)
    elif max_c == g_f:
        hue = (b_f - r_f) / delta + 2.0
    else:
        hue = (r_f - g_f) / delta + 4.0
    hue /= 6.0
    return hue, saturation, lightness


def pick_dracula_color(
    r: int,
    g: int,
    b: int,
    palette: dict[str, tuple[int, int, int]],
) -> tuple[int, int, int]:
    hue, saturation, lightness = rgb_to_hsl(r, g, b)

    # Preserve saturated accent pixels (icons, hearts, stamina, etc.)
    if saturation > 0.35 and lightness > 0.12 and lightness < 0.92:
        if hue < 0.08 or hue > 0.95 or (0.0 <= hue < 0.02):
            return palette["red"]
        if 0.08 <= hue < 0.18:
            return palette["orange"]
        if 0.18 <= hue < 0.32:
            return palette["yellow"]
        if 0.32 <= hue < 0.48:
            return palette["green"]
        if 0.48 <= hue < 0.58:
            return palette["cyan"]
        if 0.58 <= hue < 0.72:
            return palette["purple"]
        if 0.72 <= hue < 0.88:
            return palette["pink"]
        return palette["purple"]

    # Low-sat UI chrome: map luminance to Dracula surfaces / text
    if lightness >= 0.82:
        return palette["foreground"]
    if lightness >= 0.58:
        return palette["comment"]
    if lightness >= 0.34:
        return palette["currentLine"]
    return palette["background"]


def recolor_image(image: Image.Image, palette: dict[str, tuple[int, int, int]]) -> Image.Image:
    rgba = image.convert("RGBA")
    pixels = rgba.load()
    width, height = rgba.size

    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            if a == 0:
                continue
            nr, ng, nb = pick_dracula_color(r, g, b, palette)
            pixels[x, y] = (nr, ng, nb, a)

    return rgba


def resolve_input_file(input_dir: Path, name: str) -> Path | None:
    for ext in (".png", ".PNG"):
        candidate = input_dir / f"{name}{ext}"
        if candidate.is_file():
            return candidate
    return None


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build Dracula UI PNGs from your own unpacked Stardew LooseSprites."
    )
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="Folder with vanilla PNGs extracted from YOUR game (e.g. tools/unpacked/LooseSprites)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "assets" / "ui" / "LooseSprites",
        help="Output folder (default: assets/ui/LooseSprites)",
    )
    parser.add_argument(
        "--only",
        nargs="*",
        default=None,
        help="Optional subset of asset names (e.g. Cursors DialogBox)",
    )
    args = parser.parse_args()

    if not args.input.is_dir():
        print(f"Input folder not found: {args.input}", file=sys.stderr)
        return 1

    palette = load_palette()
    args.output.mkdir(parents=True, exist_ok=True)

    targets = args.only if args.only else UI_TARGETS
    processed = 0
    skipped: list[str] = []

    for name in targets:
        source = resolve_input_file(args.input, name)
        if source is None:
            skipped.append(name)
            continue

        out_path = args.output / f"{name}.png"
        image = Image.open(source)
        recolored = recolor_image(image, palette)
        recolored.save(out_path)
        print(f"OK  {source.name} -> {out_path.relative_to(ROOT)}")
        processed += 1

    if processed == 0:
        print(
            "No PNGs processed. Extract LooseSprites from your game copy first — see tools/README.md",
            file=sys.stderr,
        )
        return 1

    if skipped:
        print(f"Skipped (not found): {', '.join(skipped)}")

    print(f"\nDone. {processed} file(s) written. Launch the game — Content Patcher loads them automatically.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
