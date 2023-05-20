from sqlalchemy.orm import Session

from app.core.utils.hashing import Hasher
from app.data.user.models.user import User
from app.domain.user.entities.user_entity import UserEntity
from app.domain.user.repositories.repository import Repository


class UserRepositoryImpl(Repository):

    def __init__(self, session: Session):
        self.session: Session = session

    def get_user_by_username(self, username: str) -> str | None:
        username_exists = self.session.query(User).filter(User.username == username).first()
        if username_exists is None:
            return None
        return username_exists.username

    def authenticate_user(self, entity: UserEntity) -> User | None:
        user: User | None = self.session.query(User).filter(User.username == entity.username).first()

        if user is None:
            return None
        if not Hasher.verify_password(entity.password, user.password):
            return None

        return user

    def logout(self):
        pass

    def create(self, entity: UserEntity) -> UserEntity:
        user = User.from_entity(user=entity)
        self.session.add(user)

        return user.to_entity()

    def findall(self):
        pass

    def find_by_id(self, id: int):
        pass

    def update(self, entity):
        pass

    def delete_by_id(self, id: int):
        pass
