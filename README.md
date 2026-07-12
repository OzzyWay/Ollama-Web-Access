# Ollama-Web-Access

> A fully local AI assistant with intelligent web retrieval powered by Ollama.

Ollama-Web-Access combines local large language models with Retrieval-Augmented Generation (RAG) to answer questions using both built-in knowledge and live information from the web. Instead of searching the internet for every request, Ollama-Web-Access first determines whether a web search is actually necessary, making responses faster while reducing unnecessary requests.

Everything runs locally, including the language models.

---

## Features

* Local-first AI using Ollama
* Intelligent search routing with a lightweight language model
* Automatic web search only when needed
* HTML extraction and cleaning
* Semantic chunking of webpage content
* Embedding-based retrieval using Sentence Transformers
* Local RAG pipeline
* Gradio web interface
* Modular and easy to extend
* Cross-platform support (Linux and Windows)

---

## How It Works

```text
                User
                  │
                  ▼
          Search Router (SLM)
          Decides if a search is needed
                  │
         ┌────────┴────────┐
         │                 │
         ▼                 ▼
   Local Knowledge     Web Search
         │                 │
         │          Download HTML
         │                 │
         │          Extract Text
         │                 │
         │          Semantic Chunking
         │                 │
         │          Embedding Search
         └────────┬────────┘
                  ▼
            Ollama LLM
                  │
                  ▼
             Final Response
```
---

## Requirements

* Python 3.10 or newer
* Ollama
* Internet connection (only when web retrieval is used)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/Ollama-Web-Access.git
cd Ollama-Web-Access
```

### Linux

```bash
chmod +x install.sh
./install.sh
```

### Windows

Double-click:

```text
install.bat
```

or run:

```cmd
install.bat
```

The installer will:

* Create a Python virtual environment
* Install all required Python packages
* Verify Ollama is installed
* Download the required models

---

## Running

### Linux

```bash
./run.sh
```

### Windows

```cmd
run.bat
```

The launcher will:

* Activate the virtual environment
* Start Ollama automatically (if necessary)
* Launch the Gradio interface

---

## Example Questions

These usually **do not** require a web search:

* Explain recursion.
* What is binary search?
* How does TCP work?
* Write a Python function to sort a list.

These typically **do** trigger web retrieval:

* Latest NVIDIA news
* Bitcoin price today
* Weather in London
* Who won today's Formula 1 race?
* Current CEO of OpenAI

---

## Technologies Used

* Ollama
* Gradio
* Sentence Transformers
* Beautiful Soup
* Requests
* NumPy
* scikit-learn

---

## Roadmap

* Conversation memory
* Multi-page retrieval
* Streaming responses
* Source citations
* Vector database support (FAISS, Chroma, Qdrant)
* PDF and document support
* Image retrieval
* Additional search providers
* Model configuration through the UI

---

## Contributing

Contributions are welcome.

If you'd like to improve Ollama-Web-Access:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

Bug reports, feature requests, and suggestions are also appreciated.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

Ollama-Web-Access is built using several outstanding open-source projects:

* Ollama
* Gradio
* Sentence Transformers
* Beautiful Soup
* Requests
* NumPy
* scikit-learn

A huge thanks to the developers and communities behind these projects.
