# Store your prompt templates here
PROMPT_TEMPLATES = {
    "general_query": """
    Answer the following question accurately and concisely:
    {question}
    """,
    
    "rag_query": """
    Using the following context, answer the question:
    
    Context:
    {context}
    
    Question:
    {question}
    """
}