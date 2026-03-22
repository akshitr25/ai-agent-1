from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from agent import get_response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (fine for now)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI Agent Running"}

@app.get("/ask")
def ask(q: str):
    response = get_response(q)
    return {"response": response}