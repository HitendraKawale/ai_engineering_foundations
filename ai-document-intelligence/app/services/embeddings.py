from sentence_transformers import SentenceTransformer   
import numpy as np
from typing import List

# Load the pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')


def get_embedding(chunks: List[str]):
    """Generate embeddings for the given text chunks using SentenceTransformer."""
    embedding = model.encode(chunks, batch_size=32)
    return np.array(embedding, dtype="float32") 