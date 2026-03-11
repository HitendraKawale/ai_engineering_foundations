from app.services.embeddings import get_embedding
from app.services.vector_store import vector_store  # use the singleton
from app.services.llm_service import generate_answer
from app.utils.logger import logger

logger.info("RAG pipeline initialized and ready to process questions.")

def run_rag(question: str):

    query_embedding = get_embedding([question])[0]
    retrieved_chunks = vector_store.search(query_embedding, top_k=5)
    logger.info(f"Retrieved chunks: {retrieved_chunks}")

    context = "\n".join(retrieved_chunks)
    logger.info(f"Context length for LLM: {len(context)} characters")

    answer = generate_answer(question, context)
    logger.info(f"Generated answer: {answer}")

    return answer, retrieved_chunks
