from fastapi import FastAPI
from agent import get_response

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Agent Running"}

@app.get("/ask")
def ask(q: str):
    response = get_response(q)
    return {"response": response}