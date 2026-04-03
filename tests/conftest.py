import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.db.session import get_db, Base
from app.core.config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

@pytest.fixture
def session():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture
def client(session):
    def override_get_db():
        yield session

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()

@pytest.fixture
def admin_token(client):
    client.post("/auth/register", json={
        "username": "admin_user",
        "email": "admin@test.com",
        "password": "strongpassword",
        "role": "admin"
    })
    response = client.post("/auth/login", data={
        "username": "admin@test.com", 
        "password": "strongpassword"
    })
    return response.json()["access_token"]

@pytest.fixture
def analyst_token(client):
    client.post("/auth/register", json={
        "username": "analyst_user",
        "email": "analyst@test.com",
        "password": "strongpassword",
        "role": "analyst"
    })
    response = client.post("/auth/login", data={
        "username": "analyst@test.com",
        "password": "strongpassword"
    })
    return response.json()["access_token"]