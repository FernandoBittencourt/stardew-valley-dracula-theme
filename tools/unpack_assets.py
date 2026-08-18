#!/usr/bin/env python3
"""Unpack UI XNB files from the player's Stardew Valley install using xnbcli."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS_PATH = ROOT / "tools" / "targets.json"


def load_targets() -> dict[str, list[str]]:
    data = json.loads(TARGETS_PATH.read_text(encoding="utf-8"))
    result: dict[str, list[str]] = {}
    for folder, entries in data.items():
        result[folder] = list(entries.keys()) if isinstance(entries, dict) else list(entries)
    return result


def find_xnbcli() -> str | None:
    for name in ("xnbcli", "xnbcli.exe"):
        path = shutil.which(name)
        if path:
            return path
    local = ROOT / "tools" / "xnbcli" / "xnbcli.exe"
    if local.is_file():
        return str(local)
    return None


def unpack_one(xnbcli: str, xnb_path: Path, out_dir: Path) -> bool:
    out_dir.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        [xnbcli, "unpack", str(xnb_path), str(out_dir)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(result.stderr or result.stdout, file=sys.stderr)
        return False
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Unpack UI XNBs from your Stardew Valley folder.")
    parser.add_argument(
        "--game",
        type=Path,
        required=True,
        help="Stardew Valley game folder (contains Content/)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "tools" / "unpacked",
        help="Output root for unpacked PNGs",
    )
    args = parser.parse_args()

    content = args.game / "Content"
    if not content.is_dir():
        print(f"Content folder not found: {content}", file=sys.stderr)
        return 1

    xnbcli = find_xnbcli()
    if not xnbcli:
        print(
            "xnbcli not found. Install from https://github.com/LeonBlade/xnbcli\n"
            "Place xnbcli.exe in tools/xnbcli/ or add it to PATH.",
            file=sys.stderr,
        )
        return 1

    targets = load_targets()
    unpacked = 0
    missing: list[str] = []

    for folder, names in targets.items():
        for name in names:
            xnb_path = content / folder / f"{name}.xnb"
            if not xnb_path.is_file():
                missing.append(f"{folder}/{name}.xnb")
                continue
            out_dir = args.output / folder
            if unpack_one(xnbcli, xnb_path, out_dir):
                print(f"OK  {xnb_path.relative_to(args.game)}")
                unpacked += 1

    if unpacked == 0:
        print("Nothing unpacked.", file=sys.stderr)
        return 1

    if missing:
        print(f"Missing ({len(missing)}): {', '.join(missing[:8])}" + ("..." if len(missing) > 8 else ""))

    print(f"\nUnpacked {unpacked} file(s) to {args.output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
