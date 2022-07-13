from fastapi import APIRouter, Depends
from services.status import StatusServce

router = APIRouter()


@router.get("/status", tags=["status"])
async def status(service: StatusServce = Depends(StatusServce)):
    status = service.get()
    return {"status": status}
