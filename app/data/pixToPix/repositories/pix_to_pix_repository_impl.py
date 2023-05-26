from typing import Sequence

from sqlalchemy import select, update, delete
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from app.data.pixToPix.models.image import Image
from app.domain.pixToPix.entities.image import ImageEntity
from app.domain.pixToPix.repositories.pix_to_pix_repository import PixToPixRepository


class PixToPixRepositoryImpl(PixToPixRepository):

    def __init__(self, session: Session):
        self.session: Session = session

    def create(self, entity: ImageEntity) -> ImageEntity:
        image = Image.from_entity(image=entity)
        self.session.add(image)

        return image.to_entity()

    def findall(self) -> Sequence[ImageEntity]:
        statement = select(Image)
        try:
            result: Sequence[Image] = self.session.execute(statement=statement).scalars().all()
        except NoResultFound:
            return []

        return [image.to_entity() for image in result]

    def find_by_id(self, id: int) -> ImageEntity | None:
        result: Image | None = self.session.get(Image, id)

        if result is None:
            return None

        return result.to_entity()

    def update(self, entity: ImageEntity) -> ImageEntity:
        image = Image.from_entity(image=entity)
        update_data = image.to_dict()

        for key in [Image.updated_at.key, Image.created_at.key]:
            update_data.pop(key)

        statement = update(Image).filter_by(id=image.id).values(update_data).returning(Image)

        image_mapping = self.session.execute(statement=statement).fetchone()
        if image_mapping is None:
            raise

        result, = image_mapping

        return result.to_entity()

    def delete_by_id(self, id: int) -> ImageEntity:
        statement = delete(Image).filter_by(id=id).returning(*Image.__table__.columns)

        result: Image = self.session.execute(statement=statement).scalar_one()

        return result.to_entity()
