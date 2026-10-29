# Ollama Local Chatbot

A simple Q&A chatbot built using **LangChain, Ollama, and Streamlit**. It runs a local LLM to generate responses without requiring a hosted LLM API.

## Features

- Local LLM inference using Ollama
- Interactive Streamlit interface
- Configurable temperature and maximum response tokens
- LangChain prompt templates and output parsing


Demo

Watch the 50-second demonstration featuring the question "What is Generative AI?" and explore how changing temperature and maximum response tokens affects response generation.

[Watch the Chatbot Demo](assets/chatbot_demo.mp4)

## Tech Stack

Python · LangChain · Ollama · Streamlit

## Setup and Usage

**1. Install [Ollama](https://ollama.com/) and Python.**

**2. Download the model:**

```bash
ollama pull llama3.2:3b
```

**3. Clone this repository and enter the project directory:**

```bash
git clone https://github.com/YOUR_USERNAME/ollama-local-chatbot.git
cd ollama-local-chatbot
```

**4. Install dependencies:**

```bash
pip install -r requirements.txt
```

**5. Run the application:**

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal.

## Note

Ollama must be installed and running locally, and the required model must be downloaded. No API key is required.