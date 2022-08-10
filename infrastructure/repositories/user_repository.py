from typing import List

from ..models.user import User as IUser
from domain.models.user import User, CreateUser, UpdateUser
from domain.repositories.user_repository import UserRepository


class NotFoundError(Exception):
    pass


class UserRepositoryImpl(UserRepository):

    def find(self) -> List[User]:
        return [user for user in IUser.select()]

    def find_by_id(self, id: int) -> User:
        try:
            return IUser.get_by_id(id)
        except IUser.DoesNotExist:
            raise NotFoundError

    def create(self, create_user: CreateUser) -> User:
        return IUser.create(name=create_user.name)

    def update(self, update_user: UpdateUser) -> User:
        user = self.find_by_id(update_user.id)
        return user.save(name=update_user.name)
