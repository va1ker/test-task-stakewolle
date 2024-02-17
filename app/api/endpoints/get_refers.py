from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, models
from app.db import session
from app.crud import crud_user
from app.utils.get_current_user import get_current_user
from app.utils.referal import generate_referal
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()


@router.get("/get_referals", response_model=schemas.ResponseUserRefers)
async def get_referals(db: AsyncSession = Depends(session.get_session),
    current_user: models.User = Depends(get_current_user)):
    users = await crud_user.get_refers(db=db, user_id=current_user.id)
    users_data = [schemas.ResponseUser(username=user.username, email=user.email) for user in users]
    return schemas.ResponseUserRefers(users=users_data)