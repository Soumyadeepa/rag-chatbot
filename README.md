# Agarwal RAG Chatbot

## Overview

This project is a Retrieval-Augmented Generation (RAG) chatbot built using FastAPI, LangChain, ChromaDB, HuggingFace Embeddings, Groq LLM, and React.

The chatbot answers user questions based exclusively on the provided Agarwal Constructions knowledge base PDF. Relevant document chunks are retrieved from a vector database and supplied to the language model as context before generating a response.

---

## Features

* PDF-based knowledge retrieval
* Document chunking and vector embeddings
* ChromaDB vector database
* HuggingFace sentence-transformer embeddings
* Groq Llama 3.3 70B model integration
* FastAPI backend API
* React (Vite) frontend
* Retrieval-Augmented Generation (RAG)
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

---

## Project Structure

```text
rag-chatbot/
│
├── backend/
│   ├── ingest.py
│   ├── main.py
│   ├── requirements.txt
│   ├── chroma_db/
│   └── knowledge/
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

Navigate to backend folder:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Run document ingestion:

```bash
python ingest.py
```

Start FastAPI server:

```bash
python -m uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

### Frontend Setup

Navigate to frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start frontend:

```bash
npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

## API Endpoints

### Health Check

**GET /**

Response:

```json
{
  "message": "RAG Chatbot Running"
}
```

### Chat Endpoint

**POST /chat**

Request:

```json
{
  "question": "Who founded Agarwal Constructions?"
}
```

Response:

```json
{
  "answer": "Generated answer from document context"
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
7. Retrieved context is sent to Groq Llama 3.3 70B.
8. The model generates a response using only the retrieved context.

---

## Environment Variables

Create a `.env` file in the backend directory:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## AI Usage Disclosure

AI tools including ChatGPT were used to assist with frontend generation, debugging, troubleshooting, and development support.

---

## Future Improvements

* Multi-document support
* Conversation memory
* User authentication
* Docker deployment
* Cloud-hosted vector database
* Streaming responses

---

## Author

Soumyadeepa Dutta
