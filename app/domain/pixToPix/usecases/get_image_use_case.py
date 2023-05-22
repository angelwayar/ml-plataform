from abc import abstractmethod
from typing import Tuple

from app.core.usecases.use_case import BaseUseCase
from app.domain.pixToPix.entities.image_query import ImageResult
from app.domain.pixToPix.services.image_query_service import ImageQueryService


class GetImageUseCase(BaseUseCase[Tuple[int], ImageResult]):
    service: ImageQueryService

    @abstractmethod
    def __call__(self, args: Tuple[int]) -> ImageResult:
        raise NotImplementedError()


class GetImageUseCaseImpl(GetImageUseCase):
    def __init__(self, service: ImageQueryService):
        self.service: ImageQueryService = service

    def __call__(self, args: Tuple[int]) -> ImageResult:
        id, = args
        try:
            image = self.service.find_by_id(id=id)
            if image is None:
                raise
        except Exception:
            raise

        return image
