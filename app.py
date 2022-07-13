from fastapi import FastAPI, Depends

import controller
from service import StatusServce, status_service, status_service_dummy


def main() -> FastAPI:
    app = FastAPI()
    app.include_router(controller.router)
    app.dependency_overrides[StatusServce] = status_service
    return app


def dummy() -> FastAPI:
    app = FastAPI()
    app.include_router(controller.router)
    app.dependency_overrides[StatusServce] = status_service_dummy
    return app
