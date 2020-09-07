import pytest
from datetime import datetime


def test_get_medias(client, db):
    response = client.get('/medias/')
    assert response.status_code == 200


def test_add_media(client, db, media_payload_unit):
    response = client.post('/medias/', json=media_payload_unit)
    assert response.status_code == 201


def test_add_media_missing_field(client, db): 
    payload = dict(
        name = "Missing Field",
        duration = 100,
        upload_date = datetime.now().date().isoformat()
    )
    response = client.post('/medias/', json=payload)
    assert response.status_code == 400
    

@pytest.mark.parametrize('upload_invalid_date', ['2020', '2020-08', 2020])
def test_add_media_wrong_date_format(client, db, upload_invalid_date): 
    payload = dict(
        name = "Wrong date",
        duration = 100,
        url = "http://samba_videos/test_video6.mp4",
        upload_date = upload_invalid_date
    )
    response = client.post('/medias/', json=payload)
    assert response.status_code == 400


@pytest.mark.parametrize('id', [1, 2])
def test_get_media(client, id, db):
    response = client.get('/medias/{id}'.format(id=id))
    assert response.status_code == 200


@pytest.mark.parametrize('id', [10])
def test_get_media_not_found(client, id, db):
    response = client.get('/medias/{id}'.format(id=id))
    assert response.status_code == 404


def test_update_media(client, db):
    payload = dict(
        id = 2,
        name = "Test video update"
    )
    response = client.put('/medias/{id}'.format(id=payload.get('id')), json=payload)
    assert response.status_code == 200


@pytest.mark.parametrize('id', [1, 2])
def test_delete_media(client, id, db):
    response = client.delete(f'/medias/{id}')
    assert response.status_code == 200