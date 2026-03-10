import os
from fastapi import FastAPI
from app.api.routes import router
from app.core.config import UPLOAD_DIR, VECTOR_DIR

app = FastAPI(title="AI Document Intelligence API")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(VECTOR_DIR, exist_ok=True)

app.include_router(router)	
