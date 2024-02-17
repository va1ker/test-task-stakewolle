from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas
from app.db import session
from app.utils import jwt
from app.crud import crud_user

router = APIRouter()


@router.post("/registration", response_model=schemas.user.ResponseUser)
async def registration(
    user: schemas.user.RegisterUser, db: AsyncSession = Depends(session.get_session)
):
    password = jwt.get_password_hash(user.password)
    referal_user_id = None
    if user.referal_code != "":
        referal_user_id = await crud_user.get_user_by_referal(
            db=db, referal_code=user.referal_code
        )
    user = schemas.user.CreateUser(
        username=user.username,
        email=user.email,
        password=password,
        referal_user_id=referal_user_id,
    )
    await crud_user.create_user(db, user)
    return schemas.user.ResponseUser(
        username=user.username, email=user.email
    )
