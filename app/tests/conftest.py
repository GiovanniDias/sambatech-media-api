import pytest
from app.extensions import database
from app.models.media import Media as MediaModel
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
def db(app):
    # with app.app_context():
    database.db.create_all()
    yield database.db
    database.db.drop_all()


@pytest.fixture
def Media():
    return MediaModel


@pytest.fixture
def media():
    return MediaModel(
        id = 1,
        name = "Test video",
        duration = 100,
        url="http://samba_videos/test_video.mp4"
    )
