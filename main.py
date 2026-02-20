from typing import Optional

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/list_items/{items}")
def read_item(items: list, q: Optional[str] = None):
    return {"item_id": len(items), "q": q}
