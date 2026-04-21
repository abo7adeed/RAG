# 🧠 Mini RAG App (Retrieval-Augmented Generation)
A simple and scalable implementation of a **RAG (Retrieval-Augmented Generation)** system that combines semantic search with Large Language Models (LLMs) to generate accurate, context-aware answers.

## 🚀 Features

- 📄 Load and process custom documents (TXT, PDF, etc.)
- 🔍 Semantic search using vector embeddings
- 🧠 Context-aware responses powered by LLMs
- ⚡ Fast retrieval using vector databases (FAISS / Chroma)
- 🛠️ Modular and easy to extend


## Requirements

- Python 3.8 Or later

### Install Python using MiniConda
1) Download and Install MiniConda From [here](https://www.anaconda.com/docs/getting-started/miniconda/main#quick-command-line-install)
2) Create a new environment using the following command:
```bash
$ conda create -n mini-rag python=3.8
```
3) Activate The environment
```bash
$ conda activate mini-rag
```
###(Optional) Setup you command line interface for better readability
```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

## Installation 
### Install the required packages
```bash
pip install -r requirements.txt
```
### Setup the environment variable
```bash
$ cp .env.example .env
```

Set your environment variable in the `.env` file. like `OPENAI_API_KEY` value.

##Run the FastAPI server
```bash
uvicorn main:app --reload --host 0.0.0.0
```

## POSTMAN Collections 
Download the POSTMAN collection from [/assets/mini-rag-app.postman_collection.json](/assets/mini-rag-app.postman_collection.json)