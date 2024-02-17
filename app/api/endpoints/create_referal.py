from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, models
from app.db import session
from app.crud import crud_user
from app.utils.get_current_user import get_current_user
from app.utils.referal import generate_referal
from datetime import datetime, timedelta
from app.redis import get_clinet
from pydantic import TypeAdapter
import redis

router = APIRouter()


@router.get("/create_referal", response_model=schemas.Referal)
async def create_referal(
    db: AsyncSession = Depends(session.get_session),
    current_user: models.User = Depends(get_current_user),
    redis: redis.Redis = Depends(get_clinet),
):
    type_adapter = TypeAdapter(list[schemas.Referal])
    referal_code_cache = await redis.get(current_user.id)
    if referal_code_cache:
        await redis.delete(current_user.id, referal_code_cache)
    referal_code = await generate_referal()
    expiration_time = datetime.now() + timedelta(days=30)
    referal_data = schemas.Referal(
        referal_code=referal_code, expiration_time=expiration_time
    )

    await crud_user.update_referal(
        db=db,
        user_id=current_user.id,
        referal_data=referal_data,
    )
    await db.commit()
    encoded = type_adapter.dump_json(referal_data).decode("utf-8")
    await redis.set(current_user.id, encoded)
    return referal_data
