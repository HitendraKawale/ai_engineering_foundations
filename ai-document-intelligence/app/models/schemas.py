from pydantic import BaseModel
from typing import List, Optional

class QuestionRequest(BaseModel):
    question: str

class QuestionResponse(BaseModel):
    question: str
    answer: str
    retrieved_chunks: List[str]

class UploadResponse(BaseModel):
    message: str
    file_name: str