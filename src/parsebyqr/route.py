from fastapi import APIRouter, File, UploadFile
from .schema import decode_qr, parse_decoded_qr

router = APIRouter(
    prefix="/parseqr",
    tags=["Parsing QR"] 
)

@router.post("/check_qr/")
async def parse_qr_code(file: UploadFile = File(...)):
    decoded_value = await decode_qr(file)
    parsed_data = await parse_decoded_qr(decoded_value)
    return decoded_value
