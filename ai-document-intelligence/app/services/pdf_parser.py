import fitz
from app.utils.logger import logger


def extract_text_from_pdf(file_path: str) -> str:
    try:
        text = ""

        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()

        return text

    except Exception as e:
        logger.error(f"Failed to extract text: {e}")
        return ""