from abc import abstractmethod

from core.repositories.base_repository import BaseRepository
from domain.user.entities.user_entity import UserEntity


class Repository(BaseRepository[UserEntity]):

    @abstractmethod
    def get_user_by_username(self, username: str) -> str | None:
        raise NotImplementedError()

    @abstractmethod
    def authenticate_user(self, entity: UserEntity) -> UserEntity | None:
        raise NotImplementedError()

    @abstractmethod
    def logout(self):
        raise NotImplementedError()
