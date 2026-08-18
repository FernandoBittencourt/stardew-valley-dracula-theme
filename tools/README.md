# Build UI textures (copyright-safe)

This repository **does not include** Stardew Valley artwork. ConcernedApe owns those assets.

To get Dracula UI textures legally:

1. **Own** Stardew Valley on Steam/GOG/etc.
2. **Extract** PNGs from **your** install (local use only).
3. **Run** `recolor_ui.py` to write files into `assets/ui/` (gitignored).
4. **Play** — Content Patcher loads your locally generated files.

Generated PNGs are derivative works for personal/non-commercial mod use. **Do not upload them to GitHub or redistribute them.**

## 1. Install Python deps

```powershell
pip install -r tools/requirements.txt
```

## 2. Unpack vanilla UI sprites (your PC only)

From your Stardew Valley folder, unpack XNB files you need. Example with [xnbcli](https://github.com/LeonBlade/xnbcli):

```powershell
$game = "C:\Program Files (x86)\Steam\steamapps\common\Stardew Valley"
$out  = "C:\path\to\stardew-valley-dracula-theme\tools\unpacked\LooseSprites"
New-Item -ItemType Directory -Force -Path $out | Out-Null

xnbcli unpack "$game\Content\LooseSprites\Cursors.xnb" -o $out
xnbcli unpack "$game\Content\LooseSprites\DialogBox.xnb" -o $out
xnbcli unpack "$game\Content\LooseSprites\daybg.xnb" -o $out
xnbcli unpack "$game\Content\LooseSprites\nightbg.xnb" -o $out
xnbcli unpack "$game\Content\LooseSprites\font_bold.xnb" -o $out
```

Keep `tools/unpacked/` local — it is gitignored.

## 3. Generate Dracula versions

```powershell
cd C:\path\to\stardew-valley-dracula-theme
python tools/recolor_ui.py --input tools/unpacked/LooseSprites
```

Priority targets: `Cursors`, `DialogBox`, `daybg`, `nightbg`, `font_bold`.

## 4. Test in-game

Copy/sync the mod folder to `Stardew Valley/Mods/[CP] Dracula UI`, run via SMAPI, select **Dracula** in Theme Manager.

Content Patcher applies texture `Load` patches only when the generated PNG exists (`HasFile`).

## Custom art (optional)

You may replace generated files with **original** pixel art in `assets/ui/`. Original assets you create can be contributed to this repo.
