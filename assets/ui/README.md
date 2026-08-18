# UI assets

Place recolored or redesigned PNG files here, mirroring Stardew Valley content paths.

## Priority targets (v0.1)

| File | Game target | Notes |
|------|-------------|-------|
| `LooseSprites/Cursors.png` | Mouse cursor atlas | High visibility |
| `LooseSprites/DialogBox.png` | NPC dialogue boxes | Core UI |
| `LooseSprites/font_bold.png` | Large menu text | Works with Theme Manager `-1` color |
| `LooseSprites/daybg.png` | Day HUD background | Top bar |
| `LooseSprites/nightbg.png` | Night HUD background | Top bar |

## Palette

Use values from [`palette.json`](../palette.json). Follow the same philosophy as [dracula/minecraft](https://github.com/dracula/minecraft):

- Dark panels on `#282a36` / `#44475a`
- Primary text `#f8f8f2`
- Accents: purple hover, cyan links, green health, orange stamina

## Extracting vanilla assets

1. Install [SMAPI](https://smapi.io/) and run the game once.
2. Use [xNB Node](https://github.com/LeonBlade/xnbcli) or unpack tools from the modding wiki.
3. Export from `Stardew Valley/Content/LooseSprites/` as reference.
4. Edit in Aseprite, Photoshop, or similar — **do not redistribute raw vanilla files**.

## Enable in-game

Set `EnableTextureOverrides` to `true` in Generic Mod Config Menu (or `config.json`) once PNGs exist in this folder.
