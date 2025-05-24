import pytest
import os
from httpx import AsyncClient, ASGITransport
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from src.main import app
from src.models import User

# Синхронное подключение для тестов
SYNC_DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://kubsu:kubsu@localhost:5432/kubsu_test"
)

# Асинхронное подключение (если нужно)
ASYNC_DATABASE_URL = SYNC_DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")

# Синхронный движок для фикстур
test_engine = create_engine(SYNC_DATABASE_URL)
TestSessionLocal = sessionmaker(
    bind=test_engine,
    expire_on_commit=False
)

@pytest.fixture(scope="session")
def init_db():
    with test_engine.begin() as conn:
        User.metadata.create_all(conn)
    yield
    with test_engine.begin() as conn:
        User.metadata.drop_all(conn)

@pytest.fixture(scope="function")
def db():
    session = TestSessionLocal()
    try:
        yield session
    finally:
        session.close()

@pytest_asyncio.fixture(autouse=True)
async def test_client():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
        follow_redirects=True
    ) as client:
        yield client

@pytest.fixture(autouse=True)
def clear_tables(db):
    with db.begin():
        db.execute(text("TRUNCATE TABLE users RESTART IDENTITY CASCADE;"))
    yield

@pytest.fixture
def user(db) -> User:
    user = User(name="John Doe")
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
