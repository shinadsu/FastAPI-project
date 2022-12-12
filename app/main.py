from typing import Union


from fastapi import FastAPI
from app import auth
from .database import *
from . import bookses, users
import uvicorn




app = FastAPI(
    tags = ["Books"], # changing our list on docs 
)



@app.on_event("startup") # conecting to database 
async def startup():
    await database.connect()
    
    
@app.on_event("shutdown") # disconecting from database
async def startup():
    await database.disconnect()


app.include_router(bookses.router)
app.include_router(users.router)
app.include_router(auth.router)

if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8000)
