from app.core.config import config
import redis.asyncio as redis
from redis.asyncio import Redis


async def get_clinet() -> Redis:
    pool = redis.ConnectionPool.from_url(config.REDIS_URL)
    client = redis.Redis(connection_pool=pool)
    try:
        yield client
    finally:
        await client.aclose()
        


# async def get_session() -> AsyncSession:
#     async with async_session() as session:
#         yield session