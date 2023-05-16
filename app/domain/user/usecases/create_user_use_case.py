from abc import abstractmethod
from typing import cast, Tuple

from domain.user.entities.user_entity import UserEntity
from domain.user.entities.user_query import UserResult
from domain.user.entities.user_command import UserCommand
from core.usecases.use_case import BaseUseCase
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

        # Se debe de verificar que el usuario no exista
        try:
            self.unit_of_work.repository.create(entity=user)
        except Exception as _e:
            self.unit_of_work.rollback()
            print(user.username, user.password)

        self.unit_of_work.commit()

        return UserResult(username=user.username)
