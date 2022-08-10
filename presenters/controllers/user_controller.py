from typing import List

from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel

from domain.models.user import User, CreateUser, UpdateUser as DUpdateUser
from usecases.user_usecase import UserUsecase

router = APIRouter()


# TODO: schema の置き場を作る
class UpdateUser(BaseModel):
    name: str


class UserResponse(BaseModel):
    user: User


class UsersResponse(BaseModel):
    users: List[User]


@router.get("/users", response_model=UsersResponse)
def get_users(_: Request, usecase: UserUsecase = Depends(UserUsecase)) -> UsersResponse:
    users = usecase.get_users()
    return UsersResponse(users=users)


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(_: Request, user_id: int, usecase: UserUsecase = Depends(UserUsecase)) -> UserResponse:
    user = usecase.get_user(id=user_id)
    return UserResponse(user=user)


@router.post("/users", response_model=UserResponse)
def create_user(_: Request, data: CreateUser, usecase: UserUsecase = Depends(UserUsecase)) -> UserResponse:
    user = usecase.create_user(create_user=data)
    return UserResponse(user=user)


@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(_: Request, user_id: int, data: UpdateUser, usecase: UserUsecase = Depends(UserUsecase)):
    user = usecase.update_user(
        update_user=DUpdateUser(id=user_id, name=data.name))
    return UserResponse(user=user)
