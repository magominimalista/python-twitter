from typing import List

import uvicorn
from fastapi import FastAPI

from src.responses import TrendItem
from src.services import get_trends_from_mongo, save_trends

app = FastAPI()


@app.get("/trends", response_model=List[TrendItem])
def get_trends_route():
    return get_trends_from_mongo()


@app.post("/save_trends/")
def save_trends_route():
    # Implementação da função save_trends aqui
    return {"status": "success"}


if __name__ == "__main__":

    trends = get_trends_from_mongo()

    if not trends:
        save_trends()
    uvicorn.run(app, host="0.0.0.0", port=8000)
