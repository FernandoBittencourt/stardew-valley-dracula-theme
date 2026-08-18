# Dracula UI for Stardew Valley

Dark UI theme for [Stardew Valley](https://www.stardewvalley.net/), inspired by the [Dracula Theme](https://draculatheme.com) and following the same scope as [dracula/minecraft](https://github.com/dracula/minecraft): **interface only**, not world textures.

![Status](https://img.shields.io/badge/status-alpha-orange)
![SDV](https://img.shields.io/badge/Stardew%20Valley-1.6+-green)
![License](https://img.shields.io/badge/license-MIT-blue)

## What it changes

| Layer | Tool | Status |
|-------|------|--------|
| Text, bars, HUD colors | [Theme Manager](https://www.nexusmods.com/stardewvalley/mods/14525) | **Ready** |
| Menu textures, cursor, dialogue boxes | [Content Patcher](https://www.nexusmods.com/stardewvalley/mods/1915) | **Build locally** (see below) |

The world (farms, NPCs, items on the ground) stays vanilla.

## Requirements

- [SMAPI](https://smapi.io/)
- [Content Patcher](https://www.nexusmods.com/stardewvalley/mods/1915)
- [Theme Manager](https://www.nexusmods.com/stardewvalley/mods/14525)
- Stardew Valley **1.6+**

Optional: [Generic Mod Config Menu](https://www.nexusmods.com/stardewvalley/mods/5098) for in-game settings.

## Installation

1. Install SMAPI, Content Patcher, and Theme Manager.
2. Download this repository (Code → Download ZIP) or clone it.
3. Copy the folder into `Stardew Valley/Mods/` and rename it to `[CP] Dracula UI` (optional but recommended).
4. Launch the game through SMAPI.
5. Open **Theme Manager** (via GMCM or `config.json`) and select **Dracula**.
6. If colors look stale, open the SMAPI console and run: `retheme`

### UI textures (copyright-safe)

This repo **does not ship** Stardew artwork. To apply Dracula textures:

1. Extract UI PNGs from **your** game copy (see [`tools/README.md`](tools/README.md)).
2. Run `python tools/recolor_ui.py --input tools/unpacked/LooseSprites`.
3. Launch the game — Content Patcher loads generated files from `assets/ui/` automatically.

Do **not** commit or redistribute generated PNGs.

## Dracula palette

| Name | Hex | Usage |
|------|-----|-------|
| Background | `#282a36` | Panels |
| Current Line | `#44475a` | Borders, shadows |
| Foreground | `#f8f8f2` | Primary text |
| Purple | `#bd93f9` | Hover, selection |
| Cyan | `#8be9fd` | Links, XP |
| Green | `#50fa7b` | Health |
| Orange | `#ffb86c` | Stamina |
| Pink | `#ff79c6` | Quest highlights |
| Red | `#ff5555` | Errors |
| Yellow | `#f1fa8c` | Money |

Full list: [`assets/palette.json`](assets/palette.json).

## Project structure

```
manifest.json      → mod metadata + Theme Manager hook
theme.json         → Dracula color variables (Theme Manager)
content.json       → Content Patcher entry point
content/ui/        → texture patch definitions
assets/ui/         → locally generated PNGs (gitignored)
tools/recolor_ui.py → build script (uses your game files)
assets/palette.json
```

## Distribution

Stardew Valley does **not** support Steam Workshop for game mods. Planned channels:

- GitHub Releases (this repo)
- Nexus Mods (future)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Help is welcome with UI pixel art, compatibility patches for popular mods, and 1.6+ testing.

## Related

- [Dracula Theme](https://draculatheme.com)
- [Dracula for Minecraft](https://github.com/dracula/minecraft)
- [Theme Manager author guide](https://github.com/KhloeLeclair/StardewMods/blob/main/ThemeManager/author-guide.md)

## License

MIT — see [LICENSE](LICENSE). Dracula palette by [Dracula Theme](https://draculatheme.com) (MIT).

Stardew Valley © ConcernedApe. This is a non-commercial fan mod.
