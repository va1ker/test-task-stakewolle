from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, models
from app.db import session
from app.crud import crud_user
from app.utils.get_current_user import get_current_user
from app.utils.referal import generate_referal
from datetime import datetime, timedelta
from app.redis import get_clinet
import redis
import json
from pydantic import TypeAdapter

router = APIRouter()


@router.get("/get_referal_code", response_model=schemas.Referal)
async def get_referal_code(
    db: AsyncSession = Depends(session.get_session),
    current_user: models.User = Depends(get_current_user),
    redis: redis.Redis = Depends(get_clinet),
):
    type_adapter = TypeAdapter(schemas.Referal)
    cache = await redis.get(current_user.id)
    if cache:
        decoded = type_adapter.validate_json(cache)
        return schemas.Referal(
            referal_code=decoded.referal_code,
            expiration_time=decoded.expiration_time,
        )
    referal_data = await crud_user.get_referal(db=db, user_id=current_user.id)
    referal_data_list = [referal_data]
    encoded = type_adapter.dump_json(referal_data_list).decode("utf-8")
    await redis.set(current_user.id, encoded)
    return (
        referal_data
        if referal_data
        else schemas.Referal(referal_code="", expiration_time="")
    )
