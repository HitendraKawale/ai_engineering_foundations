import os
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AI Document Intelligence API")

os.makedirs("data/uploads", exist_ok=True)
os.makedirs("data/vector_db", exist_ok=True)

app.include_router(router)	
