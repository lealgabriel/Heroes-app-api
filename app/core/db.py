from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

from app import settings
from sys import modules

db_connection_str = settings.db_async_connection_str

if "pytest" in modules:
    db_connection_str = settings.db_async_test_connection_str

async_engine = create_async_engine(
   settings.db_async_connection_str,
   echo=True,
   future=True
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
   async_session = sessionmaker(
       bind=async_engine, class_=AsyncSession, expire_on_commit=False
   )
   async with async_session() as session:
       yield session