from pydantic import BaseModel

# For create a user
class UserCommand(BaseModel):
    username: str
    password: str