from app import models, schemas
from app.utils.jwt import verify_password
from fastapi import HTTPException
from sqlalchemy.future import select
from sqlalchemy import update


class UserCRUD:

    async def create_user(self, db, user: schemas.user.CreateUser):
        new_user = models.User(
            username=user.username,
            email=user.email,
            password=user.password,
            referal_id=user.referal_user_id,
        )
        db.add(new_user)
        await db.commit()
        return user

    async def get_users(self, db):
        result = await db.execute(models.User.select())
        users_data = result.fetchall()
        return users_data

    async def get_user(self, db, user_id: int) -> models.User:

        statemnt = select(models.User).where(models.User.id == user_id)
        result = await db.execute(statemnt)
        user_data = result.scalar()
        if user_data:
            return user_data

    async def update_user(self, db, user_id: int, user: schemas.user.UpdateUser):
        statemnt = (
            update(models.User)
            .where(models.User.id == user_id)
            .values(username=user.username, email=user.email)
        )
        await db.execute(statemnt)

    async def delete_user(self, db, user_id: int):
        deleted_user = models.User.delete().where(models.User.c.id == user_id)
        await db.execute(deleted_user)
        await db.commit()
        return {"message": "User deleted successfully"}

    async def authenticate(self, db, user: schemas.user.LoginUser):
        statemnt = select(models.User).where(models.User.username == user.username)
        result = await db.execute(statemnt)
        user_data = result.scalar()
        if user_data and verify_password(user.password, user_data.password):
            return user_data

    async def get_referal(self, db, user_id: int) -> schemas.Referal:
        statemnt = select(models.User).where(models.User.id == user_id)
        result = await db.execute(statemnt)
        user_data = result.scalar()
        if user_data:
            return schemas.Referal(referal_code=user_data.referal_code, expiration_time=user_data.referral_code_expiration)

    async def update_referal(self, db, user_id: int, referal_data: schemas.Referal):
        statemnt = (
            update(models.User)
            .where(models.User.id == user_id)
            .values(
                referal_code=referal_data.referal_code,
                referral_code_expiration=referal_data.expiration_time,
            )
        )
        await db.execute(statemnt)

    async def get_user_by_referal(self, db, referal_data: schemas.Referal):  ## Change
        statemnt = select(models.User).where(
            models.User.referal_code == referal_data.referal_code
        )
        result = await db.execute(statemnt)
        user = result.scalar()
        if user:
            return user.id

    async def delete_referal(self, db, user_id: int):
        statemnt = (
            update(models.User)
            .where(models.User.id == user_id)
            .values(referal_code=None)
        )
        await db.execute(statemnt)

    async def get_refers(self, db, user_id: int):
        query = select(models.User).filter(models.User.id == user_id)
        result = await db.execute(query)
        users = result.scalars().all()
        return users


crud_user = UserCRUD()
