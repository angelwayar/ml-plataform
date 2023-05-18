from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from app.core.models.base_model import BaseEntity
from app.domain.pixToPix.entities.image import ImageEntity


class Image(BaseEntity):
    __tablename__: str = 'images'

    image_base: Mapped[str] = Column(String)
    user_id: Mapped[int] = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='images')

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
            image_base=image.image
        )
