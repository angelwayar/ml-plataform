from typing import TYPE_CHECKING

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.core.models.base_model import BaseEntity
from app.domain.user.entities.user_entity import UserEntity
from app.data.pixToPix.models.image import Image

# if TYPE_CHECKING:
#     from app.data.pixToPix.models.image import Image


class User(BaseEntity):
    __tablename__ = 'users'

    username: Mapped[str] = Column(String(20), unique=True)
    password: Mapped[str] = Column(String(20))

    images: Mapped[list['Image']] = relationship('Image', back_populates='owner', uselist=True)

    def to_entity(self) -> UserEntity:
        return UserEntity(
            id=self.id,
            username=self.username,
            password=self.password
        )

    @staticmethod
    def from_entity(user: UserEntity) -> 'User':
        return User(
            id=user.id,
            username=user.username,
            password=user.password,
        )
