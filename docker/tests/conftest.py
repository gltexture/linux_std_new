import pytest
import os
from httpx import Client
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from src.main import app
from src.models import User

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://kubsu:kubsu@localhost:5432/kubsu_test"
)

test_engine = create_engine(DATABASE_URL)
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
    yield session
    session.close()

@pytest.fixture(scope="function")
def test_client():
    with Client(app=app, base_url="http://test") as client:
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
