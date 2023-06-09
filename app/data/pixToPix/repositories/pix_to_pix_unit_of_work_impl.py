from sqlalchemy.orm import Session

from app.domain.pixToPix.repositories.pix_to_pix_repository import PixToPixRepository
from app.domain.pixToPix.repositories.pix_to_pix_unit_of_work import PixToPixUnitOfWork


class PixToPixUnitOfWorkImpl(PixToPixUnitOfWork):

    def __init__(self, session: Session, pix_to_pix_repository: PixToPixRepository):
        self.session: Session = session
        self.repository: PixToPixRepository = pix_to_pix_repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
