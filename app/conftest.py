import pytest
import pytest_asyncio
import asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from app.main import app
from app.core.config import settings
from app.core.db import async_engine
import os
import json


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
async def async_client():
    async with AsyncClient(
        app=app,
        base_url=f"http://{settings.api_v1_prefix}"
    ) as client:
        yield client


@pytest_asyncio.fixture(scope="function")
async def async_session() -> AsyncSession:
    session = sessionmaker(
        async_engine, class_=AsyncSession, expire_on_commit=False
    )

    async with session() as s:
        async with async_engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

        yield s

        async with async_engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.drop_all)

    await async_engine.dispose()


@pytest.fixture(scope="function")
def test_data() -> dict:
    path = os.getenv('PYTEST_CURRENT_TEST')
    path = os.path.join(*os.path.split(path)[:-1], "data", "data.json")

    if not os.path.exists(path):
        path = os.path.join("data", "data.json")

    with open(path, "r") as file:
        data = json.loads(file.read())

    return data
