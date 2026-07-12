#!/usr/bin/env bash

set -e

echo "========================================="
echo "          Starting Ollama-Web-Access"
echo "========================================="

# Check virtual environment
if [ ! -d "env" ]; then
    echo "Virtual environment not found."
    echo "Run ./install.sh first."
    exit 1
fi

source env/bin/activate

# Check Ollama
if ! command -v ollama >/dev/null 2>&1; then
    echo "Ollama is not installed."
    echo "Visit https://ollama.com/download"
    exit 1
fi

# Start Ollama if it isn't already running
if ! pgrep -x "ollama" >/dev/null; then
    echo "Starting Ollama..."
    ollama serve >/dev/null 2>&1 &
    sleep 3
fi

echo "Launching Ollama-Web-Access..."

python gradio_app.py