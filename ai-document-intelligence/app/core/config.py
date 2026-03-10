import os

UPLOAD_DIR = "data/uploads"
VECTOR_DB_PATH = "data/faiss.index"
META_PATH = "data/meta.pkl"

os.makedirs(UPLOAD_DIR, exist_ok=True)
