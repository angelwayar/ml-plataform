from abc import abstractmethod
from typing import Tuple

from app.core.usecases.use_case import BaseUseCase
from app.domain.pixToPix.entities.image import ImageEntity
from app.domain.pixToPix.entities.image_command import ImageCommand
from app.domain.pixToPix.entities.image_query import ImageResult
from app.domain.pixToPix.repositories.pix_to_pix_unit_of_work import PixToPixUnitOfWork


class CreateImageUseCase(BaseUseCase[Tuple[ImageCommand], ImageResult]):
    unit_of_work: PixToPixUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[ImageCommand]) -> ImageResult:
        raise NotImplementedError()


class CreateImageUseCaseImpl(CreateImageUseCase):

    def __init__(self, unit_of_work: PixToPixUnitOfWork):
        self.unit_of_work = unit_of_work

    def __call__(self, args: Tuple[ImageCommand]):
        data, = args

        image = ImageEntity(
            id=None,
            owner_id=data.owner_id,
            image_base=data.image_base
        )

        try:
            result: ImageEntity = self.unit_of_work.repository.create(entity=image)
        except Exception as _e:
            self.unit_of_work.rollback()
            raise

        self.unit_of_work.commit()

        return ImageResult(
            id=result.owner_id,
            image=result.image_base,
            is_deleted=image.is_deleted
        )
