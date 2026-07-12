@echo off

echo =========================================
echo          WebLLM Installer
echo =========================================

python -m venv env

call env\Scripts\activate

python -m pip install --upgrade pip

pip install -r requirements.txt

where ollama >nul 2>nul

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Ollama is not installed.
    echo Download it from:
    echo https://ollama.com/download
    pause
    exit /b
)

ollama pull gemma3
ollama pull llama3.2:3b

echo.
echo Installation complete.
echo.
echo Activate with:
echo env\Scripts\activate
echo.
echo Then run:
echo python gradio_app.py
echo and open your browser to http://localhost:7860
echo.
echo Add more models by installing through Ollama

pause