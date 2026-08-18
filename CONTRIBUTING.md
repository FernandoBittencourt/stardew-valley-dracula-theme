# Contributing

Thank you for helping build the Stardew Valley Dracula UI theme.

## Goals

Match the philosophy of [dracula/minecraft](https://github.com/dracula/minecraft):

1. **UI and HUD only** — no farm/world retextures in the base theme.
2. **Cohesive redesign** — not only hue-shift; prefer clean, readable panels.
3. **Accessibility** — maintain contrast (light text on dark panels).
4. **Compatibility** — optional patches for mods that add UI (GMCM, Better Crafting, etc.).

## Getting started

1. Fork and clone this repo.
2. Copy the folder into `Stardew Valley/Mods/[CP] Dracula UI`.
3. Install SMAPI, Content Patcher, Theme Manager, and optionally GMCM.
4. Select the **Dracula** theme in Theme Manager.
5. Use `retheme` in the SMAPI console after editing `theme.json`.

## What to work on

### Colors (`theme.json`)

Adjust `ColorVariables`, test in-game, screenshot before/after. Reference [Theme Manager built-in patches](https://github.com/KhloeLeclair/StardewMods/blob/main/ThemeManager/assets/patches/).

### Textures (`assets/ui/`)

1. Read [`assets/ui/README.md`](assets/ui/README.md).
2. Add PNGs under the matching path.
3. Register targets in `content/ui/*.json` if adding new files.
4. Set `EnableTextureOverrides` to `true` to test.

### Mod compatibility

Add new JSON files under `content/compat/` with `When: { "HasMod": "Author.ModId" }` patches.

## Pull requests

- One feature per PR when possible.
- Include screenshots for visual changes.
- Note Stardew Valley version tested (e.g. 1.6.15).

## Code of conduct

Be respectful. This project follows the spirit of the [Dracula Theme](https://github.com/dracula/dracula-theme) community.
