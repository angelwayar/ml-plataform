from sqlalchemy.orm import Session

from data.user.models.user import User
from domain.user.entities.user_entity import UserEntity
from domain.user.repositories.repository import Repository


class UserRepositoryImpl(Repository):

    def __init__(self, session: Session):
        self.session: Session = session

    def create(self, entity: UserEntity) -> UserEntity:
        user = User.from_entity(user=entity)
        # user = User(
        #     entity.username,
        #     entity.password,
        # )

        self.session.add(user)

        return user.to_entity()

    def findall(self):
        pass

    def find_by_id(self, id):
        pass

    def update(self, entity):
        pass

    def delete_by_id(self, id):
        pass

    def login(self, username: str, password: str) -> User:
        pass

    def logout(self):
        pass
