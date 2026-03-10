from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
import os

from app.services.chunking import chunk_text
from app.services.embeddings import get_embedding
from app.services.pdf_parser import extract_text_from_pdf
from app.services.vector_store import VectorStore
from app.services.llm_service import generate_answer
from app.services.rag_pipeline import run_rag 
from app.models.schemas import QuestionRequest, QueryResponse
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
    print(f"[DEBUG] Saved file to {file_path}")

    # Extract text
    extracted_text = extract_text_from_pdf(file_path)
    print(f"[DEBUG] Extracted text length: {len(extracted_text)}")
    if len(extracted_text.strip()) == 0:
        print("[WARNING] PDF text extraction returned empty string. Check if it's a scanned PDF.")

    # Chunk text
    chunks = chunk_text(extracted_text)
    print(f"[DEBUG] Number of chunks created: {len(chunks)}")
    if not chunks:
        print("[WARNING] No chunks were created. Check chunking logic.")

    # Generate embeddings
    embeddings = get_embedding(chunks)
    print(f"[DEBUG] Number of embeddings generated: {len(embeddings)}")

    # Store in vector DB
    vector_store.add_embeddings(embeddings, chunks)
    print(f"[DEBUG] Total vectors stored in vector store: {len(vector_store.text_chunks)}")

    return {
        "filename": file.filename,
        "text_length": len(extracted_text),
        "num_chunks": len(chunks),
        "stored_vectors": len(vector_store.text_chunks)
    }



# Query endpoint with debug logs
@router.post("/query/", response_model=QueryResponse)
async def query_documents(request: QuestionRequest):
    question = request.question
    print(f"[DEBUG] Received question: {question}")

    # Convert question to embedding
    try:
        query_embedding = get_embedding([question])[0]
        print(f"[DEBUG] Query embedding dimension: {len(query_embedding)}")
    except Exception as e:
        print(f"[ERROR] Failed to get query embedding: {e}")
        return {
            "question": question,
            "answer": "Error generating query embedding.",
            "retrieved_chunks": []
        }

    # Retrieve relevant chunks from vector store
    try:
        chunks = vector_store.search(query_embedding, top_k=3)
        print(f"[DEBUG] Retrieved chunks ({len(chunks)}): {chunks}")
    except Exception as e:
        print(f"[ERROR] Vector store search failed: {e}")
        return {
            "question": question,
            "answer": "Error retrieving relevant chunks from vector store.",
            "retrieved_chunks": []
        }

    # If no chunks found, return informative message
    if not chunks:
        print("[DEBUG] No relevant chunks found.")
        return {
            "question": question,
            "answer": "No answer returned — check that PDF was uploaded and vector store is populated.",
            "retrieved_chunks": []
        }

    # Combine chunks into context
    limit = 4000
    context = "\n".join(chunks)
    context = context[:limit]
    print(f"[DEBUG] Context length: {len(context)} characters")

    # Generate answer using LLM
    try:
        answer = generate_answer(question, context)
        if not answer.strip():
            print("[DEBUG] LLM returned empty answer.")
            answer = "No answer returned — LLM could not generate response."
    except Exception as e:
        print(f"[ERROR] LLM generation failed: {e}")
        answer = "Error generating answer from LLM."

    return {
        "question": question,
        "answer": answer,
        "retrieved_chunks": chunks
    }