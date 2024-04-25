from fastapi import APIRouter, HTTPException
from schemas.schema import get_url

router = APIRouter(
    prefix="/pars",
    tags=["Heh"]
)

@router.get("/check/")
async def parse_check(check_url: str):
    try:
        return await get_url(check_url)
    except Exception as e:
        raise HTTPException(status_code=500)