from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class CreateUser(BaseModel):
    name: str


class UpdateUser(BaseModel):
    id: int
    name: str
