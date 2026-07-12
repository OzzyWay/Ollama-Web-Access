#!/usr/bin/env bash

set -e

echo "========================================="
echo "        Ollama-Web-Access Installer"
echo "========================================="

# Check Python
if ! command -v python3 >/dev/null 2>&1; then
    echo "Python 3 is not installed."
    exit 1
fi

echo "[1/6] Creating virtual environment..."

python3 -m venv env

echo "[2/6] Activating virtual environment..."

source env/bin/activate

echo "[3/6] Upgrading pip..."

python -m pip install --upgrade pip

echo "[4/6] Installing Python packages..."

pip install -r requirements.txt

echo "[5/6] Checking Ollama..."

if ! command -v ollama >/dev/null 2>&1; then
    echo
    echo "Ollama is not installed."
    echo
    echo "Install it from:"
    echo "https://ollama.com/download"
    echo
    exit 1
fi

echo "[6/6] Downloading models..."

ollama pull gemma3
ollama pull llama3.2:3b

echo
echo "========================================="
echo "Installation complete!"
echo "========================================="
echo
echo "Run:"
echo
echo "./run.sh"
echo
echo "Then open your browser and go to:"
echo "http://localhost:7860"
echo "Add more models by installing through Ollama"