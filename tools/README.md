# Build tools

Uses the same **local generation** model as [sqbr/Stardew-Valley-Mod-Tools](https://github.com/sqbr/Stardew-Valley-Mod-Tools) (author of Starry Blue UI).

## One command (Windows)

From the mod folder:

```powershell
.\setup.ps1
```

## Manual steps

```powershell
pip install -r tools/requirements.txt

# Point at your Stardew folder
python tools/unpack_assets.py --game "C:\Program Files (x86)\Steam\steamapps\common\Stardew Valley"

python tools/recolor_ui.py
```

Requires [xnbcli](https://github.com/LeonBlade/xnbcli) on PATH or at `tools/xnbcli/xnbcli.exe`.

## Maintain patch list

After editing `tools/targets.json`:

```powershell
python tools/generate_content.py
git add content/ui/
```

## Output locations

| Path | Contents |
|------|----------|
| `tools/unpacked/` | Vanilla PNGs from your game (gitignored) |
| `assets/ui/` | Dracula recolors (gitignored) |

**Never commit or upload** files in those folders.
