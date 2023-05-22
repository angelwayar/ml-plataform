from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from app.core.models.base_model import BaseEntity
from app.domain.pixToPix.entities.image import ImageEntity
from app.domain.pixToPix.entities.image_query import ImageResult


# TODO: Puede que se tenga un problema cuando se quiera hacer un GetAll de las imagenes por la relacion
# from app.data.user.models.user import User

# if TYPE_CHECKING:
#     from app.data.user.models.user import User


class Image(BaseEntity):
    __tablename__ = 'images'

    image_base: Mapped[str] = Column(String)
    owner_id: Mapped[int] = Column(Integer, ForeignKey('users.id'))

    owner: Mapped['User'] = relationship('User', back_populates='images', uselist=False)

    def to_entity(self):
        return ImageEntity(
            id=self.id,
            owner_id=self.owner_id,
            image_base=self.image_base
        )

    def to_read_model(self) -> ImageResult:
        return ImageResult(
            id=self.id,
            image=self.image_base
        )

    @staticmethod
    def from_entity(image: ImageEntity) -> 'Image':
        return Image(
            id=image.id,
            owner_id=image.owner_id,
            image_base=image.image_base,
            is_deleted=image.is_deleted
            updated_at=image.updated_at,
        )
