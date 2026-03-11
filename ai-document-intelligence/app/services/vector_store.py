# app/services/vector_store.py
import faiss
import numpy as np
import pickle
import os

class VectorStore:
    def __init__(self, dimension: int, index_path="data/faiss.index", meta_path="data/meta.pkl"):
        self.dimension = dimension
        self.index_path = index_path
        self.meta_path = meta_path

        if os.path.exists(self.index_path) and os.path.exists(self.meta_path):
            self.index = faiss.read_index(self.index_path)
            with open(self.meta_path, "rb") as f:
                self.text_chunks = pickle.load(f)
        else:
            self.index = faiss.IndexFlatIP(dimension)
            self.text_chunks = []

    def add_embeddings(self, embeddings, chunks):
        embeddings = np.array(embeddings).astype('float32')
        faiss.normalize_L2(embeddings)
        self.index.add(embeddings)
        self.text_chunks.extend(chunks)
        self.save()

    def search(self, query_embedding: np.ndarray, top_k: int = 5):
        if len(self.text_chunks) == 0:
            return []
        k = min(top_k, len(self.text_chunks))
        query_embedding = np.array(query_embedding).astype('float32').reshape(1, -1)
        faiss.normalize_L2(query_embedding)
        distances, indices = self.index.search(query_embedding, k)
        results = []
        for idx in indices[0]:
            if idx < len(self.text_chunks):
                results.append(self.text_chunks[idx])
        return results
    
    def save(self):
        faiss.write_index(self.index, self.index_path)
        with open(self.meta_path, "wb") as f:
            pickle.dump(self.text_chunks, f)


# Singleton instance to share across app
VECTOR_DIM = 384
vector_store = VectorStore(dimension=VECTOR_DIM)