import pytest
from app import create_app

@pytest.fixture(scope="session")
def app():
    app = create_app(FORCE_ENV_FOR_DYNACONF="testing")
    yield app


@pytest.fixture
def client(app):
    return app.test_client()