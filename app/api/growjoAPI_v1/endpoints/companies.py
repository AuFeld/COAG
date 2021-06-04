from fastapi import APIRouter

router = APIRouter()

@router.get("/companies")
async def get_companies():
    return {"message": "Get Companies!"}