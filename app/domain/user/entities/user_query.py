from pydantic import BaseModel


class UserResult(BaseModel):
    username: str
