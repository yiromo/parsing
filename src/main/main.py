from fastapi import APIRouter, HTTPException
from bs4 import BeautifulSoup

router = APIRouter(
    prefix="/pars",
    tags=["Lol"]
)

@router.get("/check/")
async def parse_check(check_url: str):
    pass


