from pydantic import BaseModel, Field

from app.domain.user.errors.user_exception import (
    UserNotFoundError,
    UserAlreadyExistsError,
    UsersNotFoundError
)


class ErrorMessageUserNotFound(BaseModel):
    detail: str = Field(example=UserNotFoundError.message)


class ErrorMessageUsersNotFound(BaseModel):
    detail: str = Field(example=UsersNotFoundError.message)


class ErrorMessageUserAlreadyExists(BaseModel):
    detail: str = Field(example=UserAlreadyExistsError.message)
