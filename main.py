from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

load_dotenv()

app = FastAPI()

# Request model
class ChatRequest(BaseModel):
    question: str

# Embedding model
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load ChromaDB
db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding
)

# Load Groq
llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

@app.get("/")
def home():
    return {"message": "RAG Chatbot Running"}

@app.post("/chat")
def chat(request: ChatRequest):

    question = request.question

    # Retrieve top 3 relevant chunks
    docs = db.similarity_search(
        question,
        k=3
    )

    # Create context
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
Answer ONLY from the provided context.

If the answer is not present in the context,
say:
"I could not find that information in the document."

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }