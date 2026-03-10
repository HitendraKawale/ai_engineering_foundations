from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
import os

from app.services.chunking import chunk_text
from app.services.embeddings import get_embedding
from app.services.pdf_parser import extract_text_from_pdf
from app.services.vector_store import VectorStore
from app.services.llm_service import generate_answer
from app.services.rag_pipeline import run_rag 
from app.services.schemas import QuestionRequest, QueryResponse
from app.core.config import UPLOAD_DIR

router = APIRouter()


# Initialize vector store once
vector_store = VectorStore(384)


# Request model for question endpoint
class QuestionRequest(BaseModel):
    question: str


# Health check
@router.get("/")
def health_check():
    return {"message": "API is working!"}


# Upload PDF endpoint
@router.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Extract text
    extracted_text = extract_text_from_pdf(file_path)

    # Chunk text
    chunks = chunk_text(extracted_text)

    # Generate embeddings
    embeddings = get_embedding(chunks)

    # Store in vector DB
    vector_store.add_embeddings(embeddings, chunks)

    return {
        "filename": file.filename,
        "text_length": len(extracted_text),
        "num_chunks": len(chunks),
        "stored_vectors": len(vector_store.text_chunks)
    }


# Query endpoint
@router.post("/query/", response_model=QueryResponse)
async def query_documents(request: QuestionRequest):

    question = request.question

    # Convert question to embedding
    query_embedding = get_embedding([question])[0]

    # Retrieve relevant chunks
    chunks = vector_store.search(query_embedding, top_k=3)

    # Combine chunks into context
    context = "\n".join(chunks)

    # Ask the local LLM
    answer = generate_answer(question, context)

    return {
        "question": question,
        "answer": answer,
        "retrieved_chunks": chunks
    }