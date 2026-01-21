@echo off
REM IPL Dashboard Update Batch Script
REM This script activates the Python environment and runs the update

echo Starting IPL Dashboard Update...
echo %DATE% %TIME%

REM Change to the IPL project directory
cd /d "C:\Users\Ishwari\Desktop\ipl"

REM Run the update script
python scripts\update_data.py

echo Update completed at %DATE% %TIME%
echo.

pause