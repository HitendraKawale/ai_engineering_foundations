from app.services.embeddings import get_embedding
from app.services.vector_store import VectorStore
from app.services.llm_service import generate_answer
from app.utils.logger import logger

vector_store = VectorStore(dimension=384)

def run_rag(question: str):
    
    # 1 generate embedding for question
    query_embedding = get_embedding([question])[0]

    # 2 retrieve relevant chunks
    retrieved_chunks = vector_store.search(query_embedding, top_k=5)

    # 3 combine context
    context = "\n".join(retrieved_chunks)

    # 4 generate answer
    answer = generate_answer(question, context)

    return answer, retrieved_chunks

#logger
logger.info("RAG pipeline initialized and ready to process questions.")
logger.info(f"retrieved_chunks: {retrieved_chunks}")