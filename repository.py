from abc import ABC, abstractmethod


class StatusRepository(ABC):

    @abstractmethod
    def find(self):
        raise NotImplemented


class StatusRepositoryImpl(StatusRepository):

    def find(self):
        return {"status": "call repository"}


class StatusRepositoryDummy(StatusRepository):

    def find(self):
        return {"status": "call dummy repository"}
