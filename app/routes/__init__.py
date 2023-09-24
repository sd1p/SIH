from fastapi import APIRouter

router = APIRouter()

from . import prediction

router.include_router(prediction.router, prefix="/prediction")

__all__ = ["router"]
