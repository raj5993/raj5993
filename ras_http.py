

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional

app = FastAPI()

BOOKS = []


class Book(BaseModel):
    id : UUID
    title : str = Field(min_length=1)
    author : str = Field(min_length=1, max_lenth=100)
    description : str = Field(title="Description of the book", max_legth=100,min_length=2)
    rating : int = Field(gt=-1, lt=101)

    class Config:
        schema_extra = {
            "example": {
                "id" : "019d7501-2cd6-4165-9694-e85b879d9cd6",
                "title": " Computer Science",
                "author" : "Codingwithroby",
                "description": "A very nice description of a book",
                "rating" : 75
            }
        }
#
# @app.get("/")
# async def read_all_books():
#     return BOOKS


# function append multiple books if not present
@app.get("/")
async def read_all_books(books_to_return: Optional[int] = None):
    if len(BOOKS) < 1:
        create_books_no_api()           # function append multiple books if not present
    if books_to_return  and len(BOOKS) >= books_to_return > 0:
        i = 1
        new_books = []
        while i <= books_to_return:
            new_books.append((BOOKS[i-1]))
            i += 1
        return new_books
    return BOOKS


@app.get("/book/{book_id}")
async def read_book(book_id: UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x



## below function we are creating book 1 at a time, instead of this  we are creating a different function
## calling that as well


@app.post("/")
async def create_book(book: Book):
    BOOKS.append(book)
    return book


@app.put("/{book_id}")
async def update_book(book_id: UUID, book: Book):
    counter = 0
    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            BOOKS[counter - 1] = book
            return BOOKS[counter - 1]


@app.delete("/{book_id}")
async def delete_book(book_id: UUID):
    counter = 0
    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            del BOOKS[counter - 1]
            return f'ID:{book_id} deleted Succesfully..!!'
    raise raise_item_cannot_be_found_exception()


def create_books_no_api():
    book1 = Book(id="019d7501-2cd6-4165-9694-e85b879d9cd5",
                title="Title 1", author="Author 1",
                description="Description 1", rating=1)
    book2 = Book(id="d1539c08-22cc-4d9e-bbc1-bfafb601e666",
                 title="Title 2", author="Author 2",
                 description="Description 2", rating=2)
    book3 = Book(id="38e32a8b-bf37-4893-9cea-0fbf718bf381",
                 title="Title 3", author="Author 3",
                 description="Description 3", rating=3)
    book4 = Book(id="44a970f1-adc4-4852-a6f4-9c819741ba59",
                 title="Title 4", author="Author 4",
                 description="Description 4", rating=4)
    BOOKS.append(book1)
    BOOKS.append(book2)
    BOOKS.append(book3)
    BOOKS.append(book4)


def raise_item_cannot_be_found_exception():
    return HTTPException(status_code=404, detail="Book Not Found",
                         headers={"X-Header-Error": "Nothing to be seen at the UUID"})




