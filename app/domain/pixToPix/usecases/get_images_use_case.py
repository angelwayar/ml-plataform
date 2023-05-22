from abc import abstractmethod
from typing import Sequence

from app.core.usecases.use_case import BaseUseCase
from app.domain.pixToPix.entities.image_query import ImageResult
from app.domain.pixToPix.services.image_query_service import ImageQueryService


class GetImagesUseCase(BaseUseCase[None, Sequence[ImageResult]]):
    service: ImageQueryService

    @abstractmethod
    def __call__(self, args: None) -> Sequence[ImageResult]:
        raise NotImplementedError()


class GetImagesUseCaseImpl(GetImagesUseCase):

    def __init__(self, service: ImageQueryService):
        self.service: ImageQueryService = service

    def __call__(self, args: None) -> Sequence[ImageResult]:
        try:
            images = self.service.findall()
        except Exception:
            raise

        return images
