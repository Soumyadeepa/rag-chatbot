# Agarwal RAG Chatbot

## Overview

This project is a Retrieval-Augmented Generation (RAG) chatbot built using FastAPI, LangChain, ChromaDB, HuggingFace Embeddings, Groq LLM, and React.

The chatbot answers user questions using information from a company knowledge base PDF. Instead of relying solely on the language model's training data, the application retrieves relevant document chunks from a vector database and provides them as context to the LLM before generating a response.

The system is designed to provide document-grounded answers while reducing hallucinations through Retrieval-Augmented Generation (RAG).

---

## Features

* PDF-based knowledge retrieval
* Document chunking and vector embeddings
* Retrieval-Augmented Generation (RAG)
* ChromaDB vector database
* HuggingFace sentence-transformer embeddings
* Groq Llama 3.3 70B model integration
* FastAPI backend API
* React (Vite) frontend
* Context-based response generation
* Hallucination prevention through document-grounded answers

---

## Architecture

Knowledge Base PDF

↓

LangChain PDF Loader

↓

Text Chunking

↓

HuggingFace Embeddings

↓

ChromaDB Vector Store

↓

Retriever

↓

Groq Llama 3.3 70B

↓

FastAPI Backend

↓

React Frontend

---

## Tech Stack

### Backend

* Python
* FastAPI
* LangChain
* ChromaDB
* HuggingFace Embeddings
* Groq API

### Frontend

* React
* Vite
* JavaScript
* Axios

---

## Project Structure

```text
rag-chatbot/
│
├── backend/
│   ├── main.py
│   ├── ingest.py
│   ├── requirements.txt
│   ├── chroma_db/
│   └── knowledge/
│       └── agarwal.pdf
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── package-lock.json
│
├── README.md
└── .gitignore
```

---

## Setup Instructions

### Backend Setup

Navigate to the backend folder:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Document Ingestion

Run the ingestion script to load the PDF, generate embeddings, and populate ChromaDB.

```bash
python ingest.py
```

This creates the local ChromaDB vector store used during retrieval.

---

## Start Backend

```bash
python -m uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

## Frontend Setup

Navigate to the frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the frontend:

```bash
npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

## API Endpoints

### GET /

Health check endpoint.

Response:

```json
{
  "message": "RAG Chatbot Running"
}
```

### POST /chat

Request:

```json
{
  "question": "Who founded Agarwal Constructions?"
}
```

Response:

```json
{
  "answer": "Generated response based on document context"
}
```

---

## How RAG Works

1. The knowledge base PDF is loaded.
2. The document is split into smaller chunks.
3. Chunks are converted into vector embeddings.
4. Embeddings are stored in ChromaDB.
5. User questions are converted into embeddings.
6. Similar document chunks are retrieved.
7. Retrieved context is sent to the Groq Llama 3.3 70B model.
8. The model generates a response using only the retrieved context.

---

## Environment Variables

Create a `.env` file in the backend directory:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## AI Usage Disclosure

AI tools, including ChatGPT, were used during development for:

* Frontend generation
* Debugging support
* Development assistance
* Troubleshooting
* Documentation assistance

This aligns with the assignment requirement encouraging the use of AI tools during development.

---

## Future Improvements

* Multi-document support
* Conversation memory
* User authentication
* Docker deployment
* Cloud-hosted vector database
* Streaming responses
* Chat history persistence

---

## Author

Soumyadeepa Dutta
