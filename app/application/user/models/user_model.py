from pydantic import BaseModel

# For create a user
class UserCreateModel(BaseModel):
    username: str
    password: str
    
class UserResultModel(BaseModel):
    username: str