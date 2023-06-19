from fastapi import FastAPI
from pydantic import BaseModel
from summarizer import Summarizer
from transformers import pipeline
import os

app = FastAPI()
exstractive_model = Summarizer()
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

abstractive_summarizer = pipeline('summarization')


class Data(BaseModel):
    body: str

@app.post("/extractive/", status_code=200)
async def exstractive_summary(data: Data):
    result = exstractive_model(data.body, ratio=0.2)
    full = ''.join(result)
    return {'summary': full}


@app.post("/abstractive/", status_code=200)
async def abstractive_summary(data: Data):
    result = abstractive_summarizer(data.body)[0]['summary_text']
    return {'summary': result}
    