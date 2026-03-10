import requests
import json

def generate_answer(question, context):

    prompt = f"""
you are a helpful assistant.
Answer the question using ONLY the context below.
If multiple facts are relevant, mention all of them in your answer

Context:
{context}

Question:
{question}

provide a clear and complete answer

Answer:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt
        },
        timeout=30
    )

    answer = ""

    for line in response.text.strip().split("\n"):
        data = json.loads(line)
        if "response" in data:
            answer += data["response"]

    return answer.strip()