import pytest
from datetime import datetime


def test_get_medias(client):
    response = client.get('/medias/')
    assert response.status_code == 200


def test_add_media(client, db):
    payload = dict(
        name = "Test video2",
        duration = 100,
        url = "http://samba_videos/test_video2.mp4",
        upload_date = datetime.now().date().isoformat()
    )
    response = client.post('/medias/', json=payload)
    assert response.status_code == 200


@pytest.mark.parametrize('id', [1, 2])
def test_get_media(client, id, db):
    response = client.get(f'/medias/{id}')
    assert response.status_code == 200


@pytest.mark.parametrize('id', [10])
def test_get_media_not_found(client, id, db):
    response = client.get('/medias/{id}'.format(id=id))
    assert response.status_code == 404


def test_update_media(client, db):
    payload = dict(
        id = 1,
        name = "Test video2",
        duration = 100,
        url = "http://samba_videos/test_video2.mp4",
        upload_date = datetime.now().date().isoformat()
    )
    response = client.put('/medias/{id}'.format(id=payload.get('id')), json=payload)
    assert response.status_code == 200


@pytest.mark.parametrize('id', [1, 2])
def test_delete_media(client, id, db):
    response = client.delete(f'/medias/{id}')
    assert response.status_code == 200