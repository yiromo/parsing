from fastapi import FastAPI, HTTPException
from bs4 import BeautifulSoup
import requests

app = FastAPI()

@app.get("/check/")
async def parse_check(check_url: str):
    pass


