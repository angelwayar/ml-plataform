from abc import ABC
from app.core.unitofwork.abs_unit_of_work import AbstractUnitOfWork
from app.domain.pixToPix.repositories.pix_to_pix_repository import PixToPixRepository


class PixToPixUnitOfWork(AbstractUnitOfWork[PixToPixRepository]):
    pass
