from fastapi import APIRouter, HTTPException
from .schema import get_url
from parsebyqr.schema import parse_decoded_qr

router = APIRouter(
    prefix="/parsing",
    tags=["Parsing URL"]
)

@router.get("/check/")
async def parse_check(check_url: str):
    try:
        all_data = await get_url(check_url)
        return all_data
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/parse_by_url/")
async def url_parse(url: str):
    return await parse_decoded_qr(url)