import os
from dotenv import load_dotenv
from sqlalchemy import String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

# Загружаем переменные окружения из .env файла
load_dotenv()

"""
Создание асинхронного движка SQLAlchemy:
- url: берется из переменной окружения DB_URL (формат: "sqlite+aiosqlite:///database.db")
- echo=True - логирование всех SQL-запросов в консоль
"""
engine = create_async_engine(
    url=os.getenv('DB_URL'),
    echo=True
)


# Создание фабрики асинхронных сессий
async_session = async_sessionmaker(engine, expire_on_commit=False)


"""
    Базовый класс для всех моделей:
    - AsyncAttrs - добавляет асинхронный доступ к атрибутам
    - DeclarativeBase - основа для декларативного стиля SQLAlchemy
"""
class Base(AsyncAttrs, DeclarativeBase):
    pass



class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    name: Mapped[str] = mapped_column(String(100))


"""
    Инициализация базы данных:
    - Создает все таблицы, определенные в моделях
    - Работает через асинхронный контекст engine.begin()
"""
async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)