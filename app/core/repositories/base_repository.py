from abc import ABC, abstractmethod
from typing import TypeVar, Sequence, Generic

_T = TypeVar('_T')


class BaseRepository(ABC, Generic[_T]):

    @abstractmethod
    def create(self, entity: _T) -> _T:
        raise NotImplementedError()

    @abstractmethod
    def findall(self) -> Sequence[_T]:
        raise NotImplementedError()
    
    @abstractmethod
    def find_by_id(self, id: int) -> _T | None:
        raise NotImplementedError()
    
    @abstractmethod
    def update(self, entity: _T) -> _T:
        raise NotImplementedError()
    
    @abstractmethod
    def delete_by_id(self, id: int) -> _T:
        raise NotImplementedError()
