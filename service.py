from abc import ABC, abstractmethod

from repository import StatusRepository, StatusRepositoryImpl, StatusRepositoryDummy


class StatusServce(ABC):
    @abstractmethod
    def get(self) -> str:
        raise NotImplemented


class StatusServceImpl(StatusServce):

    def __init__(self, repo: StatusRepository):
        self.repo = repo

    def get(self) -> str:
        return self.repo.find()


# FastAPI 起動時に dependency_overrides に代入する
def status_service() -> StatusServce:
    repo = StatusRepositoryImpl()
    service = StatusServceImpl(repo)
    return service


def status_service_dummy() -> StatusServce:
    repo = StatusRepositoryDummy()
    service = StatusServceImpl(repo)
    return service
