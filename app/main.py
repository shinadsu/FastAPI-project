from fastapi import FastAPI, status
from .database import *
from .database import *
from . import bookses, users
import uvicorn



app = FastAPI()



@app.on_event("startup") # conecting to database 
async def startup():
    await database.connect()
    
    
@app.on_event("shutdown") # disconecting from database
async def startup():
    await database.disconnect()


app.include_router(bookses.router)
app.include_router(users.router)

if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8000)