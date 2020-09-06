import pytest
from app.extensions import database
from app import create_app

@pytest.fixture(scope="session")
def app():
    app = create_app(FORCE_ENV_FOR_DYNACONF="testing")
    with app.app_context():        
        yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def db():
    return database.db