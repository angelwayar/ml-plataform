from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from app.core.models.base_model import BaseEntity
from app.domain.pixToPix.entities.image import ImageEntity


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
            user_id=self.user_id,
            image_base=self.image_base
        )

    @staticmethod
    def from_entity(image: ImageEntity) -> 'Image':
        return Image(
            id=image.id,
            user_id=image.user_id,
            image_base=image.image_base
        )
