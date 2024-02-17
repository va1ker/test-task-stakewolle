from fastapi import APIRouter
from .registration import router as registration
from .login import router as login
from .me import router as me
from .create_referal import router as create_referal
from .delete_referal import router as delete_referal
from .get_refers import router as get_refers
from .get_referal import router as get_referal_code

router = APIRouter()

router.include_router(registration)
router.include_router(login)
router.include_router(me)
router.include_router(create_referal)
router.include_router(delete_referal)
router.include_router(get_refers)
router.include_router(get_referal_code)
