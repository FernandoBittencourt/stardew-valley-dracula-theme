# Dracula UI for Stardew Valley

Dark UI theme for [Stardew Valley](https://www.stardewvalley.net/), inspired by [Dracula Theme](https://draculatheme.com) and scoped like [dracula/minecraft](https://github.com/dracula/minecraft): **interface only**.

![Status](https://img.shields.io/badge/status-alpha-orange)
![SDV](https://img.shields.io/badge/Stardew%20Valley-1.6+-green)
![License](https://img.shields.io/badge/license-MIT-blue)

Install the mod folder as **`[CP] Dracula UI`** in `Stardew Valley/Mods/` (standard Content Patcher naming).

## Features

| Layer | Tool | Notes |
|-------|------|-------|
| Text, bars, HUD colors | Theme Manager | Select theme **Dracula** |
| UI textures | Content Patcher | 27 asset groups, GMCM toggles |
| Setup | `setup.ps1` | Generates PNGs from **your** game copy |

Same **player experience** as Nexus UI recolors, without **redistributing** ConcernedApe artwork. See [`LEGAL.md`](LEGAL.md).

## Quick start

1. Install [SMAPI](https://smapi.io/), [Content Patcher](https://www.nexusmods.com/stardewvalley/mods/1915), [Theme Manager](https://www.nexusmods.com/stardewvalley/mods/14525).
2. Clone/download → rename to **`[CP] Dracula UI`** → place in `Mods/`.
3. Run **`setup.ps1`** once (requires [xnbcli](https://github.com/LeonBlade/xnbcli) + Python).
4. Launch via SMAPI → Theme Manager → **Dracula** → `retheme` if needed.

Full guide: [`docs/INSTALL.md`](docs/INSTALL.md)

## GMCM options

Toggle texture groups (cursor, dialog, HUD, menu tiles, title screen, fonts, misc) — same idea as Dark Mode UI / Garden Variety UI configs.

## Project layout

```
manifest.json          SMAPI manifest + stardew:theme
theme.json             Theme Manager colors
content.json           ConfigSchema + includes
content/ui/            Generated Load patches (27 targets)
i18n/                  GMCM labels (en, pt)
assets/ui/             Generated PNGs (gitignored)
tools/                 unpack + recolor + patch generator
setup.ps1              One-click Windows setup
```

## For mod authors

Based on sqbr's [Stardew-Valley-Mod-Tools](https://github.com/sqbr/Stardew-Valley-Mod-Tools) workflow (Starry Blue UI, Blue UI). Edit `tools/targets.json`, then:

```powershell
python tools/generate_content.py
```

## Contributing

[`CONTRIBUTING.md`](CONTRIBUTING.md) · [`LEGAL.md`](LEGAL.md)

## Links

- [Dracula Theme](https://draculatheme.com)
- [Dracula for Minecraft](https://github.com/dracula/minecraft)
- [Theme Manager guide](https://github.com/KhloeLeclair/StardewMods/blob/main/ThemeManager/author-guide.md)
- [UI recolor tutorial](https://stardewmodding.wiki.gg/wiki/Tutorial:_Making_a_UI_Recolor)

## License

MIT — [`LICENSE`](LICENSE). Stardew Valley © ConcernedApe.
