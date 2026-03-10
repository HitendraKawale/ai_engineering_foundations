import requests
import json


import requests

def generate_answer(question, context):
    """
    Sends the question + context to Ollama Mistral model and returns the answer.
    Truncates context if too long, handles HTTP errors gracefully.
    """
    # Limit context to prevent oversized prompts
    limit = 4000
    context = context[:limit]

    prompt = f"""
You are a helpful assistant.
Answer the question using ONLY the context below.
If multiple facts are relevant, mention all of them.

Context:
{context}

Question:
{question}

Provide a clear and complete answer.

Answer:
"""

    try:
        response = requests.post(
            "http://ollama:11434/api/generate",
            json={
                "model": "mistral:latest",  
                "prompt": prompt
            },
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        answer = data.get("response", "").strip()

        if not answer:
            return "No answer returned — check that the model received the prompt correctly."
        return answer

    except requests.exceptions.RequestException as e:
        return f"LLM API request failed: {e}"
    except ValueError as e:
        return f"Failed to parse LLM response: {e}"