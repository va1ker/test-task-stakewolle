from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, models
from app.db import session
from app.crud import crud_user
from app.utils.get_current_user import get_current_user
from fastapi.security import OAuth2PasswordRequestForm
import logging

router = APIRouter()


@router.put("/me/", response_model=schemas.UpdateUser)
async def update_user_me(
    user_in: schemas.UpdateUser,
    db: AsyncSession = Depends(session.get_session),
    current_user: models.User = Depends(get_current_user),
):
    """
    Update own user.
    """

    await crud_user.update_user(db=db, user_id=current_user.id, user=user_in)
    await db.commit()
    user = await crud_user.get_user(db=db, user_id=current_user.id)
    return user
