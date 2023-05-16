from sqlalchemy.orm import Session

from domain.user.repositories.repository import Repository
from domain.user.repositories.unit_of_work import UnitOfWork


class UserUnitOfWorkImpl(UnitOfWork):

    def __init__(self, session: Session, user_repository: Repository):
        self.session: Session = session
        self.repository: Repository = user_repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
