from fastapi import APIRouter, UploadFile, File
import os 

from app.services.pdf_parser import extract_text_from_pdf

router = APIRouter()

UPLOAD_DIR = "data/uploads"

@router.post("/upload-pdf/")
def health_check():
    return {"message": "API is working!"}

@router.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    #Save the uploaded file to the server
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Extract text from the uploaded PDF
    extracted_text = extract_text_from_pdf(file_path)

    return {
        "filename": file.filename,
        "extracted_text": extracted_text,
        "text_length": len(extracted_text)
    }