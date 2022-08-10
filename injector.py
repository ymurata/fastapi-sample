from usecases.user_usecase import UserUsecase, UserUsecaseImpl
from infrastructure.repositories.user_repository import UserRepositoryImpl


def user_usecase() -> UserUsecase:
    return UserUsecaseImpl(
        user_repository=UserRepositoryImpl()
    )
