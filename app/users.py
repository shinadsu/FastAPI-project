## not ended file

from fastapi import FastAPI, status, APIRouter
from app.database import  *
from app.schemas import *
from typing import List

router = APIRouter()


@router.post("/users/", response_model=userschema) # posting user on server 
async def user(user: userschemain):
    query = User.insert().values(
    username = user.username, 
    password = user.password
    )
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


#TODO не законченный файл, так как нет роутера логинки :(