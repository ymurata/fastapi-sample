from abc import ABC, abstractmethod
from typing import List

from ..models.user import User, CreateUser, UpdateUser


class UserRepository(ABC):

    @abstractmethod
    def find(self) -> List[User]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: int) -> User:
        raise NotImplementedError

    @abstractmethod
    def create(self, create_user: CreateUser) -> User:
        raise NotImplementedError

    @abstractmethod
    def update(self, update_user: UpdateUser) -> User:
        raise NotImplementedError
