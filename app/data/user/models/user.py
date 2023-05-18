from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, relationship

from core.models.base_model import BaseEntity
from domain.user.entities.user_entity import UserEntity


class User(BaseEntity):
    __tablename__ = 'users'

    username: Mapped[str] = Column(String(20), unique=True)
    password: Mapped[str] = Column(String(20))

    images = relationship('Image', back_populates='user')

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
