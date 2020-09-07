import pytest
from datetime import datetime
from app.extensions import database
from app.models.media import Media as MediaModel
from app import create_app

@pytest.fixture(scope="session")
def app():
    app = create_app(FORCE_ENV_FOR_DYNACONF="testing")
    with app.app_context():
        yield app


@pytest.fixture(scope="session")
def client(app):
    return app.test_client()


@pytest.fixture(scope="session")
def db(app):
    database.db.create_all()
    yield database.db
    database.db.drop_all()


@pytest.fixture
def Media():
    return MediaModel


@pytest.fixture
def media_instance():
    return MediaModel(
        id = 1,
        name = "Test video",
        duration = 100,
        url = "http://samba_videos/test_video.mp4",
    )


@pytest.fixture
def media_payload_unit():
    return dict(
        name = "Test video2",
        duration = 80,
        url = "http://samba_videos/test_video2.mp4",
        upload_date = datetime.now().date().isoformat()
    )

@pytest.fixture
def media_payload_functional():
    return dict(
        name = "Test video3",
        duration = 45,
        url = "http://samba_videos/test_video3.mp4",
        upload_date = datetime.now().date().isoformat()
    )
