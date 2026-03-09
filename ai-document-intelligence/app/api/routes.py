from fastapi import APIRouter, UploadFile, File
from app.services.chunking import chunk_text
import os 
from app.services.embeddings import get_embedding
from app.services.pdf_parser import extract_text_from_pdf
from app.services.vector_store import VectorStore

router = APIRouter()

UPLOAD_DIR = "data/uploads"

@router.post("/upload-pdf/")
def health_check():
    return {"message": "API is working!"}

vector_store = VectorStore(384)  # Initialize the vector store

@router.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    #Save the uploaded file to the server
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Extract text from the uploaded PDF
    extracted_text = extract_text_from_pdf(file_path)

    # Chunk the extracted text
    chunks = chunk_text(extracted_text)

    # Get embeddings for each chunk
    embeddings = get_embedding(chunks)

    # Store the chunks and embeddings in the vector store
    vector_store.add_embeddings(embeddings, chunks)
    
    return {
        "filename": file.filename,
        "extracted_text": extracted_text,
        "text_length": len(extracted_text), 
        "num_chunks": len(chunks),
        "embedding_dimensions": len(embeddings[0]),
        "stored_vectors": len(vector_store.text_chunks)
    }