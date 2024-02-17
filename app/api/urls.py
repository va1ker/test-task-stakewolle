from fastapi import APIRouter
from .endpoints import router

api_v1_router = APIRouter(prefix="/api/v1", tags=[""])

api_v1_router.include_router(router)
