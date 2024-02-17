from fastapi import APIRouter
from .urls import api_v1_router


router = APIRouter()
router.include_router(api_v1_router)