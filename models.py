"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = 'https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/65761296352685.5eac4787a4720.jpg'

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Create Pet class and models table"""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                     nullable=False
                     )
    species = db.Column(db.String(50),
                     nullable=False
                     )
    photo_url = db.Column(db.Text,
                     server_default=DEFAULT_IMAGE_URL
                     )
    age = db.Column(db.String(6),
                     nullable=False
                     )
    notes = db.Column(db.String,
                     nullable=True
                     )
    available = db.Column(db.Boolean,
                     default = True
                     )

