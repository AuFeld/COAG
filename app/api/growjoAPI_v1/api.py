from fastapi import APIRouter

from .endpoints import companies

router = APIRouter()
router.include_router(companies.router, prefix="/companies",
                        tags=["Companies"])