from fastapi import FastAPI, Depends
from controllers import status
from services.status import StatusServce, status_service


def main() -> FastAPI:
    app = FastAPI()
    app.include_router(status.router)
    app.dependency_overrides[StatusServce] = status_service
    return app
