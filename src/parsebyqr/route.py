from fastapi import APIRouter, File, UploadFile
from .schema import decode_qr, parse_decoded_qr, oofd_check

router = APIRouter(
    prefix="/parseqr",
    tags=["Parsing QR"] 
)

@router.post("/get_url/")
async def get_url_from_qr(file: UploadFile = File(...)):
    decoded_value = await decode_qr(file)
    return decoded_value

@router.post("/check_qr/")
async def parse_qr_code(file: UploadFile = File(...)):
    decoded_value = await decode_qr(file)
    parsed_data = await parse_decoded_qr(decoded_value)
    return parsed_data

@router.post("/consumer-oofd-check/")
async def parse_qr_oofd(file: UploadFile = File(...)):
    decoded_value = await decode_qr(file)
    oofd_parse = await oofd_check(decoded_value)
    return oofd_parse