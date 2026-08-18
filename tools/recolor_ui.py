#!/usr/bin/env python3
"""
Generate Dracula-themed UI PNGs from the player's own Stardew Valley install.

Same approach as sqbr/Stardew-Valley-Mod-Tools (Starry Blue UI, etc.): read vanilla
sprites from YOUR unpacked Content folder and write recolored files locally.
Nothing is redistributed via GitHub/Nexus source repos.
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
TARGETS_PATH = ROOT / "tools" / "targets.json"


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


def load_target_folders() -> dict[str, list[str]]:
    data = json.loads(TARGETS_PATH.read_text(encoding="utf-8"))
    result: dict[str, list[str]] = {}
    for folder, entries in data.items():
        if isinstance(entries, dict):
            result[folder] = list(entries.keys())
        else:
            result[folder] = list(entries)
    return result


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

    if saturation > 0.35 and lightness > 0.12 and lightness < 0.92:
        if hue < 0.08 or hue > 0.95:
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


def resolve_input_file(input_root: Path, folder: str, name: str) -> Path | None:
    folder_path = input_root / folder
    for ext in (".png", ".PNG"):
        candidate = folder_path / f"{name}{ext}"
        if candidate.is_file():
            return candidate
    return None


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build Dracula UI PNGs from your unpacked Stardew Valley Content."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=ROOT / "tools" / "unpacked",
        help="Root of unpacked Content (contains LooseSprites/, Maps/, etc.)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "assets" / "ui",
        help="Output root (default: assets/ui)",
    )
    parser.add_argument(
        "--only",
        nargs="*",
        default=None,
        help="Optional asset names to limit processing",
    )
    args = parser.parse_args()

    if not args.input.is_dir():
        print(f"Input folder not found: {args.input}", file=sys.stderr)
        return 1

    palette = load_palette()
    target_folders = load_target_folders()
    only = set(args.only) if args.only else None

    processed = 0
    skipped: list[str] = []

    for folder, names in target_folders.items():
        for name in names:
            if only and name not in only:
                continue

            source = resolve_input_file(args.input, folder, name)
            if source is None:
                skipped.append(f"{folder}/{name}")
                continue

            out_dir = args.output / folder
            out_dir.mkdir(parents=True, exist_ok=True)
            out_path = out_dir / f"{name}.png"

            recolored = recolor_image(Image.open(source), palette)
            recolored.save(out_path)
            print(f"OK  {folder}/{source.name} -> {out_path.relative_to(ROOT)}")
            processed += 1

    if processed == 0:
        print("No PNGs processed. Run .\\setup.ps1 first.", file=sys.stderr)
        return 1

    if skipped:
        print(f"Skipped ({len(skipped)}): {', '.join(skipped[:12])}" + ("..." if len(skipped) > 12 else ""))

    print(f"\nDone. {processed} file(s) written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
