# Add any model classes for Flask-SQLAlchemy here

from . import db


class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    poster = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)



    def __init__(self, title, description, poster, created_at):
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = created_at


    def serialize(self):
        return {
            "title": self.title,
            "description": self.description,
            "poster": self.poster,
            "created_at": self.created_at
        }

    def __repr__(self):
        return "<Movie %r>" % self.title

