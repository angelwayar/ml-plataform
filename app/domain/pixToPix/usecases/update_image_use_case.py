from abc import abstractmethod
from typing import cast, Tuple

from app.core.usecases.use_case import BaseUseCase
from app.domain.pixToPix.entities.image import ImageEntity
from app.domain.pixToPix.entities.image_command import ImageUpdateCommand
from app.domain.pixToPix.entities.image_query import ImageResult
from app.domain.pixToPix.repositories.pix_to_pix_unit_of_work import PixToPixUnitOfWork


class UpdateImageUseCase(BaseUseCase[Tuple[int, ImageUpdateCommand], ImageResult]):
    unit_of_work: PixToPixUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[int, ImageUpdateCommand]) -> ImageResult:
        raise NotImplementedError()


class UpdateImageUseCaseImpl(UpdateImageUseCase):
    def __init__(self, unit_of_work: PixToPixUnitOfWork):
        self.unit_of_work = unit_of_work

    def __call__(self, args: Tuple[int, ImageUpdateCommand]) -> ImageResult:
        id, update_data = args
        existing_image = self.unit_of_work.repository.find_by_id(id=id)

        if existing_image is None:
            raise

        update_entity = existing_image.update_entity(
            entity_update_model=update_data,
            get_update_data_fn=lambda image_data: image_data.dict(exclude_unset=True)
        )

        try:
            update_image = self.unit_of_work.repository.update(update_entity)
            self.unit_of_work.commit()
        except Exception:
            self.unit_of_work.rollback()
            raise

        return ImageResult.from_entity(cast(ImageEntity, update_image))
