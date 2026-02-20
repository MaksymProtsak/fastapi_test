from typing import Optional, List

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/list_items")
def len_item(items: List[int] = Query(), q: Optional[str] = None):
    return {"items_len": len(items), "q": q}
