from pydantic import BaseModel


class ImageCommand(BaseModel):
    image: str
