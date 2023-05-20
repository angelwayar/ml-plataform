from core.unitofwork.abs_unit_of_work import AbstractUnitOfWork
from domain.user.repositories.repository import Repository


class UnitOfWork(AbstractUnitOfWork[Repository]):
    pass
