@echo off
set /p commit_message=Enter commit message: 
if "%commit_message%"=="" (
    echo Commit message cannot be empty. Aborting.
    exit /b 1
)
git add .
git commit -m "%commit_message%"
git push origin main
timeout /t 5 /nobreak >nul