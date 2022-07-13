from fastapi import APIRouter, Depends
from service import StatusServce

router = APIRouter()


@router.get("/status", tags=["status"])
async def status(service: StatusServce = Depends(StatusServce)):
    status = service.get()
    return status
