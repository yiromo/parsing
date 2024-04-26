from pyzbar.pyzbar import decode
import cv2
from fastapi import UploadFile, HTTPException
import numpy as nup
import requests
from bs4 import BeautifulSoup

async def decode_qr(file: UploadFile):
    inside = await file.read()
    numpy_arr = nup.frombuffer(inside, nup.uint8)
    image = cv2.imdecode(numpy_arr, cv2.IMREAD_COLOR)
    
    val = decode(image)
    if val:
        return val[0].data.decode("utf-8")
    else:
        raise HTTPException(status_code=400, detail="No Qr")

async def parse_decoded_qr(url:str):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        tag = soup.body
        
        ret = []
        for string in tag.strings:
            stripped_string = string.strip()
            if stripped_string:
                ret.append(stripped_string)
        return ret
    else:
        raise HTTPException(status_code=404, detail="Lol")