import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from typing import AsyncGenerator, Generator
from dotenv import load_dotenv

from app.models import Base

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql+asyncpg://postgres:postgres@localhost:5432/deribit_db"
)

DATABASE_URL_SYNC = os.getenv(
    "DATABASE_URL_SYNC",
    "postgresql://postgres:postgres@localhost:5432/deribit_db"
)

# Асинхронный движок для FastAPI
async_engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    future=True,
    pool_size=20,
    max_overflow=0
)

# Синхронный движок для Celery и миграций
sync_engine = create_engine(
    DATABASE_URL_SYNC,
    echo=False,
    pool_size=20,
    max_overflow=0
)

# Асинхронная сессия
AsyncSessionLocal = async_sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)

# Синхронная сессия для Celery
SyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=sync_engine
)


async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


def get_sync_db() -> Generator:
    db = SyncSessionLocal()
    try:
        yield db
    finally:
        db.close()


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Таблицы созданы (асинхронно)")


def create_tables_sync():
    Base.metadata.create_all(bind=sync_engine)
    print("Таблицы созданы (синхронно)")


def get_db_url() -> str:
    return DATABASE_URL_SYNC.replace("postgresql+asyncpg://", "postgresql://")


async def check_db_connection():
    try:
        async with async_engine.connect() as conn:
            await conn.execute("SELECT 1")
        print("Подключение к базе данных успешно")
        return True
    except Exception as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return False