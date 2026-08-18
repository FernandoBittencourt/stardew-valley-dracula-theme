#!/usr/bin/env python3
"""Generate Content Patcher UI patch JSON from tools/targets.json."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS_PATH = ROOT / "tools" / "targets.json"
OUTPUT_DIR = ROOT / "content" / "ui"


def main() -> None:
    targets = json.loads(TARGETS_PATH.read_text(encoding="utf-8"))
    grouped: dict[str, list[dict]] = defaultdict(list)

    for folder, entries in targets.items():
        if isinstance(entries, dict):
            items = entries.items()
        else:
            items = ((name, "RecolorMisc") for name in entries)

        for asset_name, config_key in items:
            rel_from = f"assets/ui/{folder}/{asset_name}.png"
            patch = {
                "Action": "Load",
                "Target": f"{folder}/{asset_name}",
                "FromFile": rel_from,
                "When": {
                    config_key: True,
                    f"HasFile:{rel_from}": True,
                },
                "LogName": f"Dracula UI — {folder}/{asset_name}",
            }
            grouped[config_key].append(patch)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for old in OUTPUT_DIR.glob("patches-*.json"):
        old.unlink()

    config_labels = {
        "RecolorCursor": "cursor",
        "RecolorDialog": "dialog",
        "RecolorHud": "hud",
        "RecolorFonts": "fonts",
        "RecolorMenuTiles": "menu-tiles",
        "RecolorTitleScreen": "title",
        "RecolorMisc": "misc",
    }

    for config_key, patches in sorted(grouped.items()):
        slug = config_labels.get(config_key, config_key.lower())
        out_path = OUTPUT_DIR / f"patches-{slug}.json"
        payload = {"Changes": patches}
        out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {out_path.relative_to(ROOT)} ({len(patches)} patches)")


if __name__ == "__main__":
    main()
