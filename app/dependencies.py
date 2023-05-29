# For injections
from fastapi import Depends
from sqlalchemy.orm import Session

# Pix To Pix
from app.data.pixToPix.repositories.pix_to_pix_repository_impl import PixToPixRepositoryImpl
from app.data.pixToPix.repositories.pix_to_pix_unit_of_work_impl import PixToPixUnitOfWorkImpl
from app.data.pixToPix.services.image_query_service_impl import ImageQueryServiceImpl
# Pix To Pix
from app.domain.pixToPix.repositories.pix_to_pix_repository import PixToPixRepository
# Pix To Pix
from app.domain.pixToPix.repositories.pix_to_pix_unit_of_work import PixToPixUnitOfWork
# Services
# Pix to pix
from app.domain.pixToPix.services.image_query_service import ImageQueryService
from app.domain.pixToPix.usecases.create_image_use_case import CreateImageUseCase, CreateImageUseCaseImpl
from app.domain.pixToPix.usecases.delete_image_use_case import DeleteImageUseCase, DeleteImageUseCaseImpl
from app.domain.pixToPix.usecases.get_image_use_case import GetImageUseCase, GetImageUseCaseImpl
from app.domain.pixToPix.usecases.get_images_use_case import GetImagesUseCase, GetImagesUseCaseImpl
from app.domain.pixToPix.usecases.improve_the_image_of_rain_use_case import ImproveImageRainUseCase, \
    ImproveImageRainUseCaseImpl
from app.domain.pixToPix.usecases.update_image_use_case import UpdateImageUseCase, UpdateImageUseCaseImpl
# Get session Data Base
from core.database.database import get_session
# User
from data.user.repositories.repository_impl import UserRepositoryImpl
from data.user.repositories.unit_of_work_impl import UserUnitOfWorkImpl
# Repositories
# User
from domain.user.repositories.repository import Repository
# Unit of Work
# User
from domain.user.repositories.unit_of_work import UnitOfWork
from domain.user.usecases.authenticate_user_use_case import AuthenticateUserUseCase, AuthenticateUserUseCaseImpl
# Use Cases
from domain.user.usecases.create_user_use_case import CreateUserUseCase, CreateUserUseCaseImpl


def get_images_query_service(session: Session = Depends(get_session)) -> ImageQueryService:
    return ImageQueryServiceImpl(session=session)


# Repositories
# User
def get_user_repository(session: Session = Depends(get_session)) -> Repository:
    return UserRepositoryImpl(session)


# Pix To Pix
def get_pix_to_pix_image_repository(session: Session = Depends(get_session)) -> PixToPixRepository:
    return PixToPixRepositoryImpl(session=session)


# Unit of work
def get_user_unit_of_work(
        session: Session = Depends(get_session),
        user_repository: Repository = Depends(get_user_repository)
) -> UnitOfWork:
    return UserUnitOfWorkImpl(session, user_repository)


def get_pix_to_pix_image_unit_of_work(
        session: Session = Depends(get_session),
        pix_to_pix_repository: PixToPixRepository = Depends(get_pix_to_pix_image_repository)
) -> PixToPixUnitOfWork:
    return PixToPixUnitOfWorkImpl(
        session=session,
        pix_to_pix_repository=pix_to_pix_repository
    )


# User use case
def get_create_user_use_case(
        unit_of_work: UnitOfWork = Depends(get_user_unit_of_work)
) -> CreateUserUseCase:
    return CreateUserUseCaseImpl(unit_of_work)


def get_authenticate_user_use_case(
        unit_of_work: UnitOfWork = Depends(get_user_unit_of_work)
) -> AuthenticateUserUseCase:
    return AuthenticateUserUseCaseImpl(unit_of_work)


# Pix To Pix Use Case
def get_create_image_use_case(
        unity_of_work: PixToPixUnitOfWork = Depends(get_pix_to_pix_image_unit_of_work),
) -> CreateImageUseCase:
    return CreateImageUseCaseImpl(unit_of_work=unity_of_work)


def get_images_use_case(
        image_query_service: ImageQueryService = Depends(get_images_query_service)
) -> GetImagesUseCase:
    return GetImagesUseCaseImpl(image_query_service)


def get_image_use_case(
        image_query_service: ImageQueryService = Depends(get_images_query_service)
) -> GetImageUseCase:
    return GetImageUseCaseImpl(image_query_service)


def get_update_image_use_case(
        unity_of_work: PixToPixUnitOfWork = Depends(get_pix_to_pix_image_unit_of_work)
) -> UpdateImageUseCase:
    return UpdateImageUseCaseImpl(unit_of_work=unity_of_work)


def get_delete_image_use_case(
        unity_of_work: PixToPixUnitOfWork = Depends(get_pix_to_pix_image_unit_of_work)
) -> DeleteImageUseCase:
    return DeleteImageUseCaseImpl(unit_of_work=unity_of_work)


def get_improve_image_rain_use_case() -> ImproveImageRainUseCase:
    return ImproveImageRainUseCaseImpl()
