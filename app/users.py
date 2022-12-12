from fastapi import APIRouter
from .database import  *
from .schemas import *
from passlib.hash import pbkdf2_sha256






router = APIRouter(
    tags = ["User"], # changing our list on docs
)


@router.post("/users/", response_model=userschema) # create user on server 
async def user(user: userschemain):
    hashed_password = pbkdf2_sha256.hash(user.password)
    
    query = User.insert().values(
    username = user.username, 
    password = hashed_password
    )
    
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id, 
            'message': 'User Created!'}
