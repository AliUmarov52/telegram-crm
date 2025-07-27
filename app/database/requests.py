from app.database.models import async_session, User
from sqlalchemy import select, update, delete


# Окончательно добавляет инфу по имени и id в базу данных
async def set_user(tg_id: int, name: str) -> User:
    async with async_session() as session:
        async with session.begin():
            user = await session.scalar(select(User).where(User.tg_id == tg_id))
            
            if not user:
                user = User(tg_id=tg_id, name=name)
                session.add(user)
            else:
                user.name = name
                
            await session.commit()
            return user


# Функция для получения пользователя 
async def get_user_by_tg_id(tg_id: int) -> User | None:
    async with async_session() as session:
        return await session.scalar(select(User).where(User.tg_id == tg_id))