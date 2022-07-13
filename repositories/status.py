from abc import ABC, abstractmethod


class StatusRepository(ABC):

    @abstractmethod
    def find(self) -> str:
        raise NotImplemented


class StatusRepositoryImpl(StatusRepository):

    def find(self) -> str:
        return "call:repository"
