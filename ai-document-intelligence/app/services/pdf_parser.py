import fitz


def extract_text_from_pdf(file_path: str) -> str:
    # Open the PDF file
    document = fitz.open(file_path)
    # Initialize an empty string to hold the extracted text
    extracted_text = ""
    
    for page in document:
        extracted_text += page.get_text()
        
    document.close()
    return extracted_text
    
