from fastapi import APIRouter, HTTPException
from schemas.schema import get_url
import traceback

router = APIRouter(
    prefix="/pars",
    tags=["Heh"]
)

@router.get("/check/")
async def parse_check(check_url: str):
    try:
        all_data = await get_url(check_url)
        return all_data
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))