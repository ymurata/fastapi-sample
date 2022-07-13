from abc import ABC, abstractmethod

from repositories.status import StatusRepository, StatusRepositoryImpl


class StatusServce(ABC):
    @abstractmethod
    def get(self) -> str:
        raise NotImplemented


class StatusServceImpl(StatusServce):

    def __init__(self, repo: StatusRepository):
        self.repo = repo

    def get(self) -> str:
        return self.repo.find()


# これを Dpends する
def status_service() -> StatusServce:
    repo = StatusRepositoryImpl()
    service = StatusServceImpl(repo)
    return service
