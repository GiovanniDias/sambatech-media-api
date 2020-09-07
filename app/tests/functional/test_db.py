from sqlalchemy.exc import IntegrityError
from contextlib import suppress

def test_insert_media(db, media, Media):
    # Add
    db.session.add(media)
    db.session.commit()
    new_media = db.session.query(Media).get(media.id)
    assert new_media is media


def test_update_media(db, media, Media):
    # Verify existing media
    new_media = db.session.query(Media).get(media.id)
    
    if not new_media:
        # Insert new media
        test_insert_media(db, media, Media)
    
    # Update media
    new_media = db.session.query(Media).get(media.id)
    new_media.name = "Video test"
    db.session.commit()
    updated_media = db.session.query(Media).get(media.id)
    assert new_media is updated_media
