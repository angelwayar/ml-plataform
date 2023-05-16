import sys

from fastapi import status, Depends

sys.path.append("..")
from app.api.user.routes import router
from app.domain.user.entities.user_command import UserCommand
from app.domain.user.entities.user_query import UserResult
from app.domain.user.usecases.create_user_use_case import CreateUserUseCase
from app.dependencies import get_create_user_use_case


@router.post(
    '/',
    response_model=UserResult,
    status_code=status.HTTP_201_CREATED
)
def create_user(
        data: UserCommand,
        create_user_use_case: CreateUserUseCase = Depends(get_create_user_use_case)
):
    user = create_user_use_case((data,))
    return user


@router.post('/login')
def login():
    pass
