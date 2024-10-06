from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json

app = FastAPI()
from fastapi import FastAPI

app = FastAPI()

model = SentenceTransformer('all-MiniLM-L6-v2')

class Titles(BaseModel):
    reference: str
    other: list[str]

@app.post("/similar-title/")
def find_similar_title(data: Titles):
    reference_embedding = model.encode([data.reference])
    other_embeddings = model.encode(data.other)
    similarities = cosine_similarity(reference_embedding, other_embeddings)
    print(similarities)
    most_similar_idx = np.argmax(similarities)
    print(most_similar_idx, data.other[most_similar_idx])
    top_result = data.other[most_similar_idx]
    return {"top_result": top_result}

@app.post("/process-input/")
def process_input():
    with open("input.json") as f:
        data = json.load(f)
        result = find_similar_title(Titles(**data))
    return result