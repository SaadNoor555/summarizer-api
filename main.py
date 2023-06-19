from fastapi import FastAPI
from pydantic import BaseModel
from summarizer import Summarizer

app = FastAPI()
model = Summarizer()

class Data(BaseModel):
    body: str

@app.post("/extractive/", status_code=200)
async def extractive_summary(data: Data):
    result = model(data.body, ratio=0.2)
    full = ''.join(result)
    return {'summary': full}
    