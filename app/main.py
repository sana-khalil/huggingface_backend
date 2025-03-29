from fastapi import FastAPI
from pydantic import BaseModel
import os
from app.routes import nlp_routes
from app.services.huggingface_service import sentiment
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="FastAPI Hugging Face NLP")

class TextRequest(BaseModel):
    text: str

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development purposes)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI NLP API"}

@app.post("/sentiment")
def sentiment_analysis(request: TextRequest):
    text = request.text
    result = sentiment(text)
    return {"text": text, "sentiment": result}
