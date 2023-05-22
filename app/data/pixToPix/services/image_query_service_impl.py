from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.data.pixToPix.models.image import Image
from app.domain.pixToPix.entities.image_query import ImageResult
from app.domain.pixToPix.services.image_query_service import ImageQueryService


class ImageQueryServiceImpl(ImageQueryService):

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id: int) -> ImageResult | None:
        result: Image | None = self.session.get(Image, id)
        if result is None:
            return None

        return result.to_read_model()

    def findall(self) -> Sequence[ImageResult]:
        # TODO: Add offset and limit
        statement = select(Image)

        result = self.session.execute(statement=statement).scalars().all()

        if len(result) == 0:
            return []

        return [image.to_read_model() for image in result]
