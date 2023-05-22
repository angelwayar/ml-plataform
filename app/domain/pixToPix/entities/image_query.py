from pydantic import BaseModel

from app.domain.pixToPix.entities.image import ImageEntity


class ImageResult(BaseModel):
    id: int
    image: str
    is_deleted: bool

    class Config(object):
        orm_mode = True

    @classmethod
    def from_entity(cls, entity: ImageEntity) -> 'ImageResult':
        return cls(
            id=entity.id,
            image=entity.image_base,
            is_deleted=entity.is_deleted,
        )
