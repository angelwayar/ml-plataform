from domain.user.repositories.repository import Repository
from core.unitofwork.abs_unit_of_work import AbstractUnitOfWork

class UnitOfWork(AbstractUnitOfWork[Repository]):
    pass