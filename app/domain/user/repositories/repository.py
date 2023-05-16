from abc import abstractmethod
from domain.user.entities.user_entity import UserEntity
from core.repositories.base_repository import BaseRepository

class Repository(BaseRepository[UserEntity]):

    @abstractmethod
    def login(self, username: str, password: str) -> UserEntity:
        raise NotImplementedError()

    @abstractmethod
    def logout(self):
        raise NotImplementedError()