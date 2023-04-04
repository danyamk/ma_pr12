from fastapi import FastAPI, HTTPException
from app.document import Document

documents: list[Document] = [
    Document(0, 'FirstD', 'HKJHDBKNLM'),
    Document(1, 'SecondD', 'hjbjkbkjbkjbjbjhvhcgxdfftgyhujknjbhvg')
]

app = FastAPI()


@app.get("/v1/docs")
async def get_docs():
    return documents

@app.get("/v1/docs/{id}")
async def get_docs_id(id: int):
    result = [item for item in documents if item.id == id]
    if len(result) > 0:
        return result[0]
    raise HTTPException(status_code=404, detail="Item not found")