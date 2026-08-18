# UI assets (local build)

This folder holds **locally generated** PNGs. They are **not** in the Git repository.

## Why?

Stardew Valley sprites © ConcernedApe. We do not redistribute vanilla or recolored game art.

## How to populate

Run the build tool against PNGs extracted from **your** game install:

```powershell
pip install -r tools/requirements.txt
python tools/recolor_ui.py --input tools/unpacked/LooseSprites
```

Full steps: [`tools/README.md`](../../tools/README.md)

## Priority files

| Output | Game target |
|--------|-------------|
| `LooseSprites/Cursors.png` | Mouse cursor |
| `LooseSprites/DialogBox.png` | Dialogue boxes |
| `LooseSprites/daybg.png` | Day HUD bar |
| `LooseSprites/nightbg.png` | Night HUD bar |
| `LooseSprites/font_bold.png` | Large menu text |

## Original art

If you draw **original** UI replacements (not derived from vanilla), those may be committed — open a PR and note they are your own work.

Palette reference: [`palette.json`](../palette.json)
