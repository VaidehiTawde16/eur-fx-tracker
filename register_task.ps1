# Registers a Windows Scheduled Task that refreshes + pushes the FX data every
# Monday and Friday. If the PC is OFF at the scheduled time, it runs as soon as the PC is
# next turned on (StartWhenAvailable) — so it never silently skips a Mon/Fri.
#
# Run this ONCE, in PowerShell (no admin needed for a user task):
#     powershell -ExecutionPolicy Bypass -File register_task.ps1

$script = "C:\Vaidehi Job\projects\eur-fx-tracker\update_and_push.ps1"

$action = New-ScheduledTaskAction -Execute "powershell.exe" `
    -Argument "-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$script`""

# Weekly on Monday & Friday at 10:00. Change -At to whatever time you like.
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday,Friday -At 10:00am

# StartWhenAvailable = run the missed task once the PC comes back on.
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 10) -DontStopIfGoingOnBatteries

Register-ScheduledTask -TaskName "EUR-FX-Tracker" -Action $action -Trigger $trigger `
    -Settings $settings -Description "Mon/Fri ECB euro FX refresh + git push" -Force

Write-Host "Task 'EUR-FX-Tracker' registered. Test it now with:  Start-ScheduledTask -TaskName EUR-FX-Tracker"
