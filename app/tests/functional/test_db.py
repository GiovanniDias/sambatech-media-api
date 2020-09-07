from sqlalchemy.exc import IntegrityError
from contextlib import suppress

def test_insert_media(db, media_instance, Media):
    # Add
    db.session.add(media_instance)
    db.session.commit()
    new_media = db.session.query(Media).get(media_instance.id)
    assert new_media is media_instance


def test_update_media(db, media_instance, Media):
    # Verify existing media
    new_media = db.session.query(Media).get(media_instance.id)
    
    if not new_media:
        # Insert new media
        test_insert_media(db, media_instance, Media)
    
    # Update media
    new_media = db.session.query(Media).get(media_instance.id)
    new_media.name = "Video test"
    db.session.commit()
    updated_media = db.session.query(Media).get(media_instance.id)
    assert new_media is updated_media
