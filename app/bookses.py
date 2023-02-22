from fastapi import FastAPI, status, APIRouter
from app.database import *
from app.schemas import *
from typing import List


router = APIRouter(
    tags = ["Books"], # changing our list on docs
)


@router.get('/book/{id}') # geting book from id
async def getbook(id:int):
    query = bookses.select().where(bookses.columns.id == id)
    return await database.fetch_all(query)


@router.post("/postbook/") # posting book on server 
async def create_note(book: mainbook):
    query = bookses.insert().values(text=book.text, completed=book.completed, description = book.description)
    last_record_id = await database.execute(query)
    return {**book.dict(), "id": last_record_id}


@router.put('/editpost/{id}/') # editing book on server
async def update_book(book: mainbook, id:int):
    query = bookses.update().where(bookses.columns.id == id).values(text = book.text, completed=book.completed, description = book.description )
    await database.execute(query)
    return {**book.dict(), "id": id}


@router.get("/GetAllBooks/") # geting all bokses
async def read_books():
    query = bookses.select()
    return await database.fetch_all(query)


@router.delete('/deletebook')
async def delete_books(id: int):
    query = bookses.delete().where(bookses.columns.id == id)
    await database.execute(query)
    return {"message: ""the data is deleted"}





