@echo off
echo.
echo 🏍️  WASTELAND RIDER - Starting Game...
echo =====================================
echo.

REM Try python3 first, then python
python3 game.py 2>nul
if %errorlevel% neq 0 (
    python game.py 2>nul
    if %errorlevel% neq 0 (
        echo ❌ Python not found! Please install Python from https://python.org
        echo    Make sure to check "Add to PATH" during installation.
        echo.
        pause
        exit /b 1
    )
)

echo.
echo Thanks for playing Wasteland Rider!
pause
