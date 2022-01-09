from typing import Optional
from fastapi import FastAPI
from enum import Enum

app = FastAPI()

BOOKS = {
    'book_1':{'title':'Title_one','Author':'Author_name'},
    'book_2':{'title':'Title_two','Author':'Author_two'},
    'book_3':{'title':'Title_three','Author':'Author_three'},
    'book_4':{'title':'Title_four','Author':'Author_four'},
    'book_5':{'title':'Title_five','Author':'Author_five'},
}


class DirectionName(str,Enum):
    north="North"
    south="South"
    east="East"
    west="West"

@app.get('/')
async def first_api(skip_book: Optional[str] = None):
    if skip_book:
        new_books=BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return  BOOKS


@app.get('/all_book}')
async def first_api():
    return BOOKS


@app.get('/{book_name}')
async def first_api(book_name: str):
    return BOOKS[book_name]


@app.post("/create")
async def create_book(book_title,book_author):
    current_book_id = 0
    if len(BOOKS) > 0:
        for book in BOOKS:
            x = int(book.split('_')[-1])
            if x>current_book_id:
                current_book_id = x
    BOOKS[f'book_{current_book_id + 1}']= {'title':book_title,'author':book_author}
    return BOOKS[f'book_{current_book_id + 1}']


@app.put("/{book_name}")
async def update_book(book_name: str, book_title:str, book_author:str):
    book_information = {'title':book_title, 'author':book_author}
    BOOKS[book_name]=book_information
    return book_information

@app.delete("/{delete_book_name")
async def delete_book(book_name):
    del BOOKS[book_name]
    return f'Book_{book_name}  deleted..'


'''

@app.get("/direction/{drection_name}")
async def get_direction(drection_name : DirectionName):
    if drection_name == DirectionName.north:
        return {"Direction":drection_name, "Sub":"Up"}
    if drection_name == DirectionName.south:
        return {"Direction":drection_name, "Sub":"Down"}
    if drection_name == DirectionName.east:
        return {"Direction":drection_name, "Sub":"Right"}
    return {"Direction":drection_name, "Sub":"Left"}


'''


'''
@app.get('/books')          # path parameter
async def get_book_details():
    return BOOKS



@app.get('/books/{book_title}')          # path parameter
async def read_book(book_title):
    return {'book_title':book_title}


@app.get('/books/{book_id}')          # path parameter
async def read_book(book_id:int):
    return {'book_title':book_id}

'''