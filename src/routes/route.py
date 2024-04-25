from fastapi import APIRouter, HTTPException
from bs4 import BeautifulSoup
import requests

router = APIRouter(
    prefix="/pars",
    tags=["Heh"]
)


@router.get("/check/")
async def parse_check(check_url: str):
    try:
        response = requests.get(check_url)

        soup = BeautifulSoup(response.content, "html.parser")
        tables = soup.find_all('table')

        parsed_data = []
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                columns = row.find_all('td')
                if len(columns) >= 2:
                    check_name = columns[0].text.strip()
                    check_price = columns[1].text.strip()
                    parsed_data.append({"name": check_name, "info": check_price})
        return parsed_data
    except Exception as e:
        raise HTTPException(status_code=500)



