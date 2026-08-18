# Dracula UI — first-time setup (Windows)
# Generates texture files from YOUR Stardew Valley install (not included in this repo).

$ErrorActionPreference = "Stop"
$ModRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ModRoot

Write-Host ""
Write-Host "=== Dracula UI setup ===" -ForegroundColor Magenta
Write-Host "This reads assets from your own game copy. Nothing is uploaded or redistributed."
Write-Host ""

function Find-StardewPath {
    $candidates = @(
        "$env:ProgramFiles(x86)\Steam\steamapps\common\Stardew Valley",
        "$env:ProgramFiles\Steam\steamapps\common\Stardew Valley",
        "$env:LOCALAPPDATA\Programs\Stardew Valley"
    )
    foreach ($path in $candidates) {
        if (Test-Path (Join-Path $path "Content")) { return $path }
    }
    return $null
}

$GamePath = $env:STARDEW_PATH
if (-not $GamePath) { $GamePath = Find-StardewPath }

if (-not $GamePath -or -not (Test-Path (Join-Path $GamePath "Content"))) {
    $GamePath = Read-Host "Stardew Valley folder (contains Content/)"
}

if (-not (Test-Path (Join-Path $GamePath "Content"))) {
    Write-Error "Invalid path: $GamePath"
}

Write-Host "Game: $GamePath" -ForegroundColor Cyan

Write-Host "`n[1/3] Python dependencies..." -ForegroundColor Yellow
python -m pip install -r tools/requirements.txt --quiet

Write-Host "`n[2/3] Unpack UI XNBs (xnbcli required)..." -ForegroundColor Yellow
python tools/unpack_assets.py --game $GamePath
if ($LASTEXITCODE -ne 0) {
    Write-Host "`nxnbcli missing? Download: https://github.com/LeonBlade/xnbcli" -ForegroundColor Red
    Write-Host "Or unpack manually to tools/unpacked/ and re-run only recolor:" -ForegroundColor Red
    Write-Host "  python tools/recolor_ui.py" -ForegroundColor Gray
    exit 1
}

Write-Host "`n[3/3] Apply Dracula palette..." -ForegroundColor Yellow
python tools/recolor_ui.py
if ($LASTEXITCODE -ne 0) { exit 1 }

Write-Host ""
Write-Host "Done! Next steps:" -ForegroundColor Green
Write-Host "  1. Copy this folder to Stardew Valley/Mods as [CP] Dracula UI"
Write-Host "  2. Launch via SMAPI"
Write-Host "  3. Theme Manager -> select theme 'Dracula'"
Write-Host "  4. (Optional) Generic Mod Config Menu -> toggle texture groups"
Write-Host ""
