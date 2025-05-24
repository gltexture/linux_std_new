import pytest
import os
from httpx import AsyncClient, ASGITransport
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from src.main import app
from src.models import User

DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql+asyncpg://kubsu:kubsu@localhost:5432/kubsu_test"
)

test_engine = create_async_engine(DATABASE_URL)
TestSessionLocal = sessionmaker(
    bind=test_engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

@pytest.fixture(scope="session")
async def init_db():
    async with test_engine.begin() as conn:
        await conn.run_sync(User.metadata.create_all)
    yield
    async with test_engine.begin() as conn:
        await conn.run_sync(User.metadata.drop_all)

@pytest.fixture(scope="function")
async def db():
    async with TestSessionLocal() as session:
        yield session

@pytest.fixture(scope="function")
async def test_client():
    async with AsyncClient(
        transport=ASGITransport(app=app), 
        base_url="http://test"
    ) as client:
        yield client

@pytest.fixture(autouse=True)
async def clear_tables(db: AsyncSession):
    async with db.begin():
        await db.execute(text("TRUNCATE TABLE users RESTART IDENTITY CASCADE;"))
    yield

@pytest.fixture
async def user(db: AsyncSession) -> User:
    user = User(name="John Doe")
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
