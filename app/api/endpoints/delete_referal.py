from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, models
from app.db import session
from app.crud import crud_user
from app.utils.get_current_user import get_current_user
from app.utils.referal import generate_referal
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()


@router.get("/delete_referal", response_model=schemas.Referal)
async def delete_referal(
    db: AsyncSession = Depends(session.get_session),
    current_user: models.User = Depends(get_current_user),
):
    await crud_user.delete_referal(db=db, user_id=current_user.id)
    await db.commit()
    return schemas.Referal(referal_code="", exiration_time="")
