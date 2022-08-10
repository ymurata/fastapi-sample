from abc import ABC, abstractmethod
from typing import List, Optional

from domain.models.user import User, CreateUser, UpdateUser
from domain.repositories.user_repository import UserRepository


class UserUsecase(ABC):

    @abstractmethod
    def get_users(self) -> List[User]:
        raise NotImplementedError

    @abstractmethod
    def get_user(self, id: int) -> User:
        raise NotImplementedError

    @abstractmethod
    def create_user(self, create_user: CreateUser) -> User:
        raise NotImplementedError

    @abstractmethod
    def update_user(self, update_user: UpdateUser) -> User:
        raise NotImplementedError


class UserUsecaseImpl(UserUsecase):

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_users(self) -> List[User]:
        return self.user_repository.find()

    def get_user(self, id: int) -> User:
        # TODO: try で書いて throw する
        return self.user_repository.find_by_id(id)

    def create_user(self, create_user: CreateUser) -> User:
        return self.user_repository.create(create_user)

    def update_user(self, update_user: UpdateUser) -> User:
        # TODO: try で書いて throw する
        return self.user_repository.update(update_user)
