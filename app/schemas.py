from pydantic import BaseModel

class mainbook(BaseModel):
    text: str
    description: str
    completed: bool
    
class userschema(BaseModel):
    id: int
    username: str
    

class userschemain(BaseModel):
    username: str
    password: str
        
class loginschema(BaseModel):
    username: str
    password: str
    
