from abc import ABC

from app.core.repositories.base_repository import BaseRepository
from app.domain.pixToPix.entities.image import ImageEntity


class PixToPixRepository(BaseRepository[ImageEntity], ABC):
    pass
