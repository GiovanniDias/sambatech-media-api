import pytest
from datetime import datetime


def test_add_media(client, media, db):
    payload = dict(
        name = "Video Test3",
        duration = 100,
        url = "http://samba_videos/test_video3.mp4",
        upload_date = datetime.now().date().isoformat()
    )
    response = client.post('/medias/', json=payload)
    assert type(response.json) is dict
    assert type(response.json.get('id')) is int


def test_get_medias(client, db):
    media = client.get('/medias/').json
    
    if not media:
        test_add_media(client, media, db)

    response = client.get('/medias/')
    assert type(response.json) is list


def test_get_media(client, db):
    media = client.get('/medias/').json
    
    if not media:
        test_add_media(client, media, db)
        media = client.get('/medias/').json

    response = client.get('/medias/{id}'.format(id=media[0].get('id')))
    media = response.json
    assert type(media) is dict    
    assert media.get('name') is not None
    assert media.get('duration') is not None
    assert media.get('upload_date') is not None
    assert media.get('url') is not None


def test_update_media(client, db):
    media = client.get('/medias/').json
    
    if not media:
        test_add_media(client, media, db)

    payload = dict(
        id = 1,
        name = "Test video",
        duration = 100,
        url = "http://samba_videos/test_video2.mp4",
        upload_date = datetime.now().date().isoformat()
    )
    response = client.put('/medias/{id}'.format(id=payload.get('id')), json=payload)
    assert response.status_code == 200


@pytest.mark.parametrize('id', [1, 2])
def test_delete_media(client, id, db):
    media = client.get('/medias/').json
    
    if not media:
        test_add_media(client, media, db)

    response = client.delete(f'/medias/{id}')
    assert response.status_code == 200
