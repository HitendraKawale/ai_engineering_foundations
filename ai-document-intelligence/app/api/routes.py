from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
import os

from app.services.chunking import chunk_text
from app.services.embeddings import get_embedding
from app.services.pdf_parser import extract_text_from_pdf
from app.services.vector_store import vector_store
from app.services.llm_service import generate_answer
from app.services.rag_pipeline import run_rag 
from app.models.schemas import QuestionRequest, QueryResponse
from app.core.config import UPLOAD_DIR
from app.utils.logger import logger

router = APIRouter()


# Initialize vector store once
#VECTOR_DIM = 384  # Dimension of OpenAI embeddings
#vector_store = VectorStore(VECTOR_DIM)


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
    logger.info(f"Saved file to {file_path}")

    # Extract text
    extracted_text = extract_text_from_pdf(file_path)
    logger.info(f"Extracted text length: {len(extracted_text)}")
    if len(extracted_text.strip()) == 0:
        logger.warning(
            "PDF text extraction returned empty string. "
            "Check if it's a scanned PDF."
        )

    # Chunk text
    chunks = chunk_text(extracted_text)
    logger.info(f"Number of chunks created: {len(chunks)}")
    if not chunks:
        logger.warning("[WARNING] No chunks were created. Check chunking logic.")

    # Generate embeddings
    embeddings = get_embedding(chunks)
    logger.info(f"Number of embeddings generated: {len(embeddings)}")

    # Store in vector DB
    vector_store.add_embeddings(embeddings, chunks)
    logger.info(f"Total vectors stored in vector store: {len(vector_store.text_chunks)}")

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
    answer, chunks = run_rag(question)

    return {
        "question": question,
        "answer": answer,
        "retrieved_chunks": chunks
    }