import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_completion(prompt: str) -> str:
    """Get completion from OpenAI API"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def get_rag_completion(query: str, context: str) -> str:
    """Get RAG-based completion using context"""
    prompt = f"Context: {context}\n\nQuery: {query}"
    return get_completion(prompt)