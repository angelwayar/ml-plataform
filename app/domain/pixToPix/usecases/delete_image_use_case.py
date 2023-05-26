from abc import abstractmethod
from typing import cast, Tuple

from app.core.usecases.use_case import BaseUseCase
from app.domain.pixToPix.entities.image import ImageEntity
from app.domain.pixToPix.entities.image_query import ImageResult
from app.domain.pixToPix.repositories.pix_to_pix_unit_of_work import PixToPixUnitOfWork


class DeleteImageUseCase(BaseUseCase[Tuple[int], None]):
    unit_of_work = PixToPixUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[int]) -> ImageResult:
        raise NotImplementedError()


class DeleteImageUseCaseImpl(DeleteImageUseCase):

    def __init__(self, unit_of_work: PixToPixUnitOfWork):
        self.unit_of_work: PixToPixUnitOfWork = unit_of_work

    def __call__(self, args: Tuple[int]) -> ImageResult:
        id, = args

        existing_image = self.unit_of_work.repository.find_by_id(id)

        if existing_image is None:
            raise

        marked_image = existing_image.mark_entity_as_deleted()

        try:
            deleted_image = self.unit_of_work.repository.update(marked_image)
            self.unit_of_work.commit()
        except Exception:
            self.unit_of_work.rollback()
            raise

        return ImageResult.from_entity(cast(ImageEntity, deleted_image))
