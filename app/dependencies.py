# For injections
from fastapi import Depends
from sqlalchemy.orm import Session

# Get session Data Base
from core.database.database import get_session
from data.user.repositories.repository_impl import UserRepositoryImpl
from data.user.repositories.unit_of_work_impl import UserUnitOfWorkImpl
# Repository
from domain.user.repositories.repository import Repository
# Unit of Work
from domain.user.repositories.unit_of_work import UnitOfWork
# Use Cases
from domain.user.usecases.create_user_use_case import CreateUserUseCase, CreateUserUseCaseImpl


def get_user_repository(session: Session = Depends(get_session)) -> Repository:
    return UserRepositoryImpl(session)


def get_user_unit_of_work(
        session: Session = Depends(get_session),
        user_repository: Repository = Depends(get_user_repository)
) -> UnitOfWork:
    return UserUnitOfWorkImpl(session, user_repository)


def get_create_user_use_case(
        unit_of_work: UnitOfWork = Depends(get_user_unit_of_work)
) -> CreateUserUseCase:
    return CreateUserUseCaseImpl(unit_of_work)
