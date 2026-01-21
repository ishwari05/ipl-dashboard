# IPL Dashboard Update PowerShell Script
# This script runs the automated update for the IPL dashboard

Write-Host "Starting IPL Dashboard Update..." -ForegroundColor Green
Write-Host "Time: $(Get-Date)" -ForegroundColor Yellow

try {
    # Change to the IPL project directory
    Set-Location "C:\Users\Ishwari\Desktop\ipl"

    # Run the update script
    Write-Host "Running update script..." -ForegroundColor Cyan
    python scripts\update_data.py

    Write-Host "Update completed successfully!" -ForegroundColor Green
    Write-Host "Time: $(Get-Date)" -ForegroundColor Yellow

} catch {
    Write-Host "Error during update: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "Check the log file at data\update_log.txt for details" -ForegroundColor Yellow
}

Write-Host "Press any key to exit..."
$null = $host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")