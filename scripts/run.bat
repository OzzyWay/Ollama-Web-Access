@echo off

echo =========================================
echo          Starting Ollama-Web-Access
echo =========================================

if not exist env (
    echo Virtual environment not found.
    echo Run install.bat first.
    pause
    exit /b
)

call env\Scripts\activate

where ollama >nul 2>nul

if %ERRORLEVEL% NEQ 0 (
    echo Ollama is not installed.
    echo Download it from:
    echo https://ollama.com/download
    pause
    exit /b
)

tasklist | findstr /I "ollama.exe" >nul

if %ERRORLEVEL% NEQ 0 (
    start "" ollama serve
    timeout /t 3 >nul
)

python gradio_app.py


echo.
echo Open your browser at http://localhost:7860
pause