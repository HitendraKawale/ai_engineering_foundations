import requests
import json


import requests

def generate_answer(question, context):
   
    limit = 4000  
    context = context[:limit]

    prompt = f"""
You are a helpful assistant.
Answer the question using ONLY the context below.
If multiple facts are relevant, mention all of them in your answer.

Context:
{context}

Question:
{question}

Provide a clear and complete answer.

Answer:
"""

    try:
        response = requests.post(
            "http://ollama:11434/completions",
            json={
                "model": "mistral",
                "prompt": prompt
            },
            timeout=30
        )

        # Check for HTTP errors
        response.raise_for_status()

        # Parse JSON directly
        data = response.json()

        # Extract the answer safely
        answer = data.get("response", "").strip()

        # Fallback if empty
        if not answer:
            answer = "No answer returned — check that the model received the prompt correctly."

        return answer

    except requests.exceptions.RequestException as e:
        return f"LLM API request failed: {e}"
    except ValueError as e:
        return f"Failed to parse LLM response: {e}"