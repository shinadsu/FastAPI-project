
from .database import *
from fastapi import APIRouter, HTTPException
from .schemas import *
from fastapi import status

router = APIRouter( # changing our list on docs 
    tags = ["Auth"] 
)


@router.post('/login') # login router
async def authentificate(request: loginschema):
    query = User.select().where(User.c.username == request.username)
    query2 = User.select().where(User.c.password == request.password)
    
    context = {
        'myuser': await database.fetch_one(query),
        'myuser2': await database.fetch_one(query2)
    }
        
    
    if not context['myuser'] or not context['myuser2']:    
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found or your password is incorrect')
    return {'message:', 'Got it! You are authentificated'}
   

# Надо бы сделать логинку по JWT https://fastapi.tiangolo.com/ru/tutorial/security/oauth2-jwt/?h=jwt

        
        
