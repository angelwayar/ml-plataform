from abc import abstractmethod
from datetime import datetime, timedelta
from typing import Tuple

from jose import jwt

from app.domain.user.errors.user_exception import UserNotFoundError
from app.domain.user.repositories.unit_of_work import UnitOfWork
from core.token.token_settings import settings
from core.usecases.use_case import BaseUseCase
from domain.user.entities.token import Token
from domain.user.entities.user_command import UserCommand
from domain.user.entities.user_entity import UserEntity


class AuthenticateUserUseCase(BaseUseCase[Tuple[UserCommand], Token]):
    unit_of_work: UnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[UserCommand]) -> Token:
        raise NotImplementedError()


class AuthenticateUserUseCaseImpl(AuthenticateUserUseCase):
    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

        return encoded_jwt

    def __init__(self, unit_of_work: UnitOfWork):
        self.unit_of_work = unit_of_work

    def __call__(self, args: UserCommand) -> Token:
        data, = args
        # ----- Validar usuario ----
        # TODO: Validar que el usuario existe, verificar username y password
        user = UserEntity(
            id=None,
            **data.dict()
        )
        # TODO: Si el usuario no existe retornar una Exception
        user_exists = self.unit_of_work.repository.authenticate_user(entity=user)
        if user_exists is None:
            raise UserNotFoundError()

        # ----- Crear access token -----
        # TODO: Tiempo de expiracion del token
        # TODO: Crear objeto Token
        try:
            access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = self.create_access_token(
                data={"sub": user_exists.username}, expires_delta=access_token_expires
            )
            print(access_token)
        except Exception as _e:
            raise
        # --- Return Token ----

        return Token(
            access_toke=access_token,
            token_type="bearer"
        )
