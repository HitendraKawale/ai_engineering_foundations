# app/services/llm_service.py

import subprocess

def generate_answer(question: str, context: str) -> str:
    """
    Generate answer using local Ollama Mistral via CLI.
    """

    context = context[:4000]

    prompt = f"""
You are a helpful assistant.
Answer the question using ONLY the context below.

Context:
{context}

Question:
{question}

Answer:
"""

    try:
        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return f"Ollama error: {result.stderr}"

        return result.stdout.strip()

    except Exception as e:
        return f"LLM CLI call failed: {e}"