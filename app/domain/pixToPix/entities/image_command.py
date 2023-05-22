from pydantic import BaseModel


class ImageCommand(BaseModel):
    owner_id: int
    image_base: str


class ImageUpdateCommand(BaseModel):
    is_deleted: bool
