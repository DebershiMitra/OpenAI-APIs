from langchain.chat_models import ChatOpenAI
from .Retrieval_Engine import handle_query
import numpy as np
import os
from dotenv import load_dotenv
load_dotenv()

def generate_response(relevant_text, query):
    chat_model = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    prompt = f"Answer the question based on the following context:\n\n{relevant_text}\n\n--- Answer the question based on the above context: {query}"
    llm_response = chat_model.predict(prompt)
    return llm_response

