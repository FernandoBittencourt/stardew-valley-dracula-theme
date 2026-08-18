# Installation

Follow the same flow as popular UI recolors (Starry Blue UI, Garden Variety UI), with one extra step: **generate textures from your game** instead of downloading ConcernedApe-derived PNGs from the internet.

## Requirements

| Mod | Link |
|-----|------|
| SMAPI | https://smapi.io/ |
| Content Patcher | Nexus #1915 |
| Theme Manager | Nexus #14525 |
| Generic Mod Config Menu | Nexus #5098 (optional, recommended) |

Stardew Valley **1.6+**

## Quick install

1. Download or clone this repo.
2. Rename the folder to **`[CP] Dracula UI`** (Nexus naming convention).
3. Place it in `Stardew Valley/Mods/`.
4. Run **`setup.ps1`** once (Windows) or follow [`tools/README.md`](../tools/README.md) on other OS.
5. Launch the game through SMAPI.
6. In **Theme Manager**, select theme **`Dracula`**.
7. Run `retheme` in the SMAPI console if colors look stale.

## Theme Manager

If you do not use GMCM for Theme Manager, add to `Mods/Theme Manager/config.json`:

```json
"StardewTheme": "Dracula"
```

(Uses the `Name` field from `theme.json`.)

## Texture toggles (GMCM)

After setup, open **Dracula UI** in Generic Mod Config Menu to enable/disable:

- Cursor, dialog, HUD, menu tiles, title screen, misc UI
- Font atlases (off by default; Theme Manager handles most text)

## Updating

1. Pull/download the new mod version.
2. Re-run `setup.ps1` (regenerates textures from your game).
3. Delete old generated PNGs first if the target list changed.

## Legal note

See [`LEGAL.md`](../LEGAL.md). You must **own** Stardew Valley. Generated PNGs stay on your PC.
