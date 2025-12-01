# Mini-Rag

Mini-RAG is a lightweight, easy-to-understand implementation of a Retrieval-Augmented Generation (RAG) system designed for question answering. It provides a clean and minimal codebase suitable for learning, experimentation, and integrating RAG into your own projects. The setup is intentionally simple, making it ideal for beginners and advanced users who want a clear reference implementation without unnecessary complexity.

## Tools & Technologies Used

Mini-RAG is built using a clean, modular architecture and relies on modern tools to ensure scalability, maintainability, and high performance.

### 1. LLM Providers (OpenAI & Cohere)
The system supports multiple Large Language Model backends:
- **OpenAI** — used for embeddings and text generation.
- **Cohere** — supported as an alternative provider for generation or embeddings.

This flexibility allows you to switch providers easily through environment variables without changing your codebase.

### 2. MongoDB
Used as the primary database for:
- Storing documents  
- Metadata  
- Vector references  
- Query logs and experiment tracking  

MongoDB’s flexible schema makes it well-suited for RAG workloads.

### 3. Qdrant Vector Database
Qdrant is used to store and search embeddings efficiently.  
Key features leveraged:
- Fast approximate nearest-neighbor search  
- Payload filtering  
- High performance for large-scale vector collections  

This forms the core of the retrieval step in the RAG pipeline.

### 4. MVC Pattern
The project follows a clean **Model–View–Controller (MVC)** architecture:
- **Models** define data entities and schemas  
- **Controllers** handle business logic and request processing  
- **Views / Routers** expose API endpoints via FastAPI  

This pattern ensures clear separation of concerns and easier extendability.

### 5. Clean Code Principles
Mini-RAG is structured with maintainability in mind:
- Modular and readable code  
- Consistent naming conventions  
- Type hints across the codebase  
- Reusable service layers  
- Clear folder structure  

This makes the project easy to navigate, modify, and scale.


## Requirements

- Python 3.8 or later

#### Install Python using MiniConda

1) Download and install MiniConda from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)
2) Create a new environment using the following command:
```bash
$ conda create -n mini-rag python=3.8
```
3) Activate the environment:
```bash
$ conda activate mini-rag
```

## Installation

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.

## Run Docker Compose Services

```bash
$ cd docker
$ cp .env.example .env
```

- update `.env` with your credentials



```bash
$ cd docker
$ sudo docker compose up -d
```

## Run the FastAPI server

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

## POSTMAN Collection

Download the POSTMAN collection from [/assets/mini-rag.postman_collection.json](/assets/mini-rag.postman_collection.json)