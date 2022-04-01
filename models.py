"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://media.npr.org/assets/img/2021/04/27/prancer_wide-db59609b5bd96c9e56e4dfe32d198461197880c2.jpg?s=1400"
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
    photo_url = db.Column(db.String,
                    nullable=False,
                    server_default=DEFAULT_IMAGE_URL)
    age = db.Column(db.String(6),
                     nullable=False
                     )
    notes = db.Column(db.String,
                     nullable=True
                     )
    available = db.Column(db.Boolean,
                     default = True
                     )

