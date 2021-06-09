from fastapi import FastAPI
from app.routes.company_routes import GrowjoAPI as GrowjoAPIRouter

from mangum import Mangum

app = FastAPI()

app.include_router(GrowjoAPIRouter, tags=["Company"], prefix="/company")

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to COAG!"}


handler = Mangum(app)