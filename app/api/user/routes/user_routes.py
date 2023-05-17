import sys

from fastapi import Depends, HTTPException, status, Response, Request

sys.path.append("..")
from app.api.schemas.user_error_message import ErrorMessageUserAlreadyExists
from app.core.utils.hashing import Hasher
from app.api.user.routes import router
from app.dependencies import get_create_user_use_case
from app.domain.user.errors.user_exception import UserAlreadyExistsError
from app.domain.user.entities.user_query import UserResult
from app.domain.user.entities.user_command import UserCommand
from app.domain.user.usecases.create_user_use_case import CreateUserUseCase


@router.post(
    '/',
    response_model=UserResult,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_409_CONFLICT: {
            'model': ErrorMessageUserAlreadyExists
        }
    }
)
def create_user(
        data: UserCommand,
        response: Response,
        request: Request,
        create_user_use_case: CreateUserUseCase = Depends(get_create_user_use_case)
):
    hash_pwd = Hasher.get_password_hash(password=data.password)
    new_data = UserCommand(username=data.username, password=hash_pwd)
    try:
        user = create_user_use_case((new_data,))
    except UserAlreadyExistsError as exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=exception.message
        )
    except Exception as _exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    response.headers['location'] = f"{request.url.path}"
    return user


@router.post('/login')
def login():
    pass
