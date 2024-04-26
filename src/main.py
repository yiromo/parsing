from fastapi import FastAPI
import uvicorn
from parseurl.route import router as parse_url
from parsebyqr.route import router as parse_qr

app = FastAPI()

app.include_router(parse_url)
app.include_router(parse_qr)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)