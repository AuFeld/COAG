from fastapi import FastAPI

from app.api.growjoAPI_v1.api import router as api_router
from mangum import Mangum

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Shalom!"}

app.include_router(api_router, prefix="/api/v1")
handler = Mangum(app)