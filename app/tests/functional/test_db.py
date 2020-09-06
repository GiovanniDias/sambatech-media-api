def test_insert_media(db, media, Media):
    # Add
    db.session.add(media)
    db.session.commit()
    new_media = db.session.query(Media).get(media.id)
    assert new_media is media


def test_update_media(db, media, Media):
    # Add before update
    test_insert_media(db, media, Media)

    # Update
    new_media = db.session.query(Media).get(media.id)
    new_media.name = "Video test"
    db.session.commit()
    updated_media = db.session.query(Media).get(media.id)
    assert new_media is updated_media
