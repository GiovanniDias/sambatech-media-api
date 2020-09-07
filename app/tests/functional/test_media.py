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
