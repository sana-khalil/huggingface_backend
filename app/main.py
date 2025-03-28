from fastapi import FastAPI
from app.routes import nlp_routes
from app.services.huggingface_service import sentiment

app = FastAPI(title="FastAPI Hugging Face NLP")

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI NLP API"}

@app.post("/sentiment")
def sentiment_analysis(text: str):
    result = sentiment(text)
    return {"text": text, "sentiment": result}
