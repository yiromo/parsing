import requests
from bs4 import BeautifulSoup

async def parse_data(data):
    parsed_data = {}
    for item in data:
        parsed_data[item['name']] = item['info']
    return parsed_data


async def get_url(check_url: str):
    r = requests.get(check_url)

    soup = BeautifulSoup(r.content, "html.parser")
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
    return await parse_data(parsed_data)
