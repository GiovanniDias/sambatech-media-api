from datetime import datetime
from ..extensions.database import db


class Media(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    name = db.Column(db.String(512), nullable=False)
    url = db.Column(db.String(512), nullable=False, unique=True)
    duration = db.Column(db.Integer, nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    deleted = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return self.name
