from abc import abstractmethod
from typing import Tuple

from core.usecases.use_case import BaseUseCase
from domain.user.entities.user_command import UserCommand
from domain.user.entities.user_entity import UserEntity
from domain.user.entities.user_query import UserResult
from app.domain.user.errors.user_exception import UserAlreadyExistsError
from domain.user.repositories.unit_of_work import UnitOfWork


class CreateUserUseCase(BaseUseCase[Tuple[UserCommand], UserResult]):
    unit_of_work: UnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[UserCommand]) -> UserResult:
        raise NotImplementedError()


class CreateUserUseCaseImpl(CreateUserUseCase):

    def __init__(self, unit_of_work: UnitOfWork):
        self.unit_of_work = unit_of_work

    def __call__(self, args: Tuple[UserCommand]) -> UserResult:
        data, = args

        user = UserEntity(
            id=None,
            **data.dict()
        )
        username_exists = self.unit_of_work.repository.get_user_by_username(
            username=user.username
        )
        if username_exists is not None:
            raise UserAlreadyExistsError()

        try:
            self.unit_of_work.repository.create(entity=user)
        except Exception as _e:
            self.unit_of_work.rollback()
            raise

        self.unit_of_work.commit()

        return UserResult(username=user.username)
