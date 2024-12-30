import pytest
import pytest_asyncio
import asyncio
from httpx import AsyncClient
from httpx._transports.asgi import ASGITransport
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from app.main import app
from app.core.config import settings
from app.core.db import async_engine
import os
import json
from typing import AsyncGenerator



@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
async def async_client():
    transport = ASGITransport(app=app)      
    async with AsyncClient(
        transport=transport,
        base_url="http://test/api/v1"             
    ) as client:
        yield client


@pytest_asyncio.fixture(scope="function")
async def async_session() -> AsyncGenerator[AsyncSession, None]:
    session = sessionmaker(
        async_engine, class_=AsyncSession, expire_on_commit=False
    )

    async with session() as s:
        async with async_engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

        yield s
        
        await s.close()

        async with async_engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.drop_all)

    await async_engine.dispose()


@pytest.fixture(scope="function")
def test_data() -> dict:
    import os, json

    
    conf_dir = os.path.dirname(__file__)      

   
    data_path = os.path.join(conf_dir, "heroes", "data", "data.json")

    with open(data_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data
