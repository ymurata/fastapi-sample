from fastapi import FastAPI

from injector import user_usecase
from usecases.user_usecase import UserUsecase
from presenters.controllers import user_controller


def main() -> FastAPI:
    app = FastAPI()
    app.include_router(user_controller.router)
    app.dependency_overrides[UserUsecase] = user_usecase
    return app
