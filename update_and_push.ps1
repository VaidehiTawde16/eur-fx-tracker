# Refresh ECB euro reference rates and push the update. Built for unattended (scheduled) runs.
$ErrorActionPreference = "Stop"
$repo = "C:\Vaidehi Job\projects\eur-fx-tracker"
$py   = "C:\Vaidehi Job\projects\.venv\Scripts\python.exe"   # venv with pandas + matplotlib

Set-Location $repo
& $py "fetch_and_update.py"

git add -A
$changes = git status --porcelain
if ($changes) {
    $date = Get-Date -Format "yyyy-MM-dd"
    git commit -m "chore: refresh ECB euro reference rates ($date)"
    git push
    Write-Host "Pushed FX update for $date"
} else {
    Write-Host "No changes to commit"
}
