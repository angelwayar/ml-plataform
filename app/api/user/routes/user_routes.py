import sys

from fastapi import status, Depends

sys.path.append("..")
from app.core.utils.hashing import Hasher
from app.api.user.routes import router
from app.dependencies import get_create_user_use_case
from app.domain.user.entities.user_query import UserResult
from app.domain.user.entities.user_command import UserCommand
from app.domain.user.usecases.create_user_use_case import CreateUserUseCase


@router.post(
    '/',
    response_model=UserResult,
    status_code=status.HTTP_201_CREATED
)
def create_user(
        data: UserCommand,
        create_user_use_case: CreateUserUseCase = Depends(get_create_user_use_case)
):
    hash_pwd = Hasher.get_password_hash(password=data.password)
    new_data = UserCommand(username=data.username, password=hash_pwd)
    user = create_user_use_case((new_data,))

    return user


@router.post('/login')
def login():
    pass
