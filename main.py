from fastapi import FastAPI
from langchain.chat_models import ChatOpenAI
import os

api = FastAPI()

@api.get("/ask")
def ask(q: str):
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        return {"error": "Missing OPENAI_API_KEY"}
    llm = ChatOpenAI(openai_api_key=key)
    return {"answer": llm.predict(q)}
