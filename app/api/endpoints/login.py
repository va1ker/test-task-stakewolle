from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud, schemas
from app import db
from app.utils import jwt
from app.core.config import config
from app.crud import crud_user

router = APIRouter()


@router.post("/login/access-token/", response_model=schemas.Token)
async def login_access_token(
    form_data: schemas.LoginUser, ## Исправить
    request: Request,
    db: AsyncSession = Depends(db.session.get_session),
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = schemas.user.LoginUser(
        username=form_data.username, password=form_data.password
    )
    user = await crud_user.authenticate(db, user)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": jwt.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }
