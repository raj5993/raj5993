
from fastapi import FastAPI
from pydantic  import BaseModel
from uuid import UUID


app = FastAPI()

BOOKS = []


class Book(BaseModel):
    id : UUID
    title : str
    author : str
    description : str
    rating : str


@app.get("/")
async def read_all_books():
    return BOOKS

@app.post("/post_data")
async def create_book(book : Book):
    BOOKS.append(book)
    return BOOKS