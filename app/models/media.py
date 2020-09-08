from datetime import datetime, date
from dataclasses import dataclass
from ..extensions.database import db


@dataclass
class Media(db.Model):
    id: int = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    name: str = db.Column(db.String(512), nullable=False)
    url: str = db.Column(db.String(512), nullable=False, unique=True)
    duration: int = db.Column(db.Integer, nullable=False)
    upload_date: date = db.Column(db.DateTime, default=datetime.utcnow)
    deleted: bool = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return self.name
