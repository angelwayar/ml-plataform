from pydantic import BaseModel


class ImageResult(BaseModel):
    id: int
    image: str
