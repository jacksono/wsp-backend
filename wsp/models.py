"""Module to create the models for the app."""

from app import db
from datetime import datetime


class SongsToGlory(db.Model):
    """Docstring."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    origin = db.Column(db.String(50))
    tempo = db.Column(db.String(10))
    language = db.Column(db.String(10))
    message = db.Column(db.String(50))
    category = db.Column(db.String(10))
    comment = db.Column(db.String(1000))
    lyrics = db.Column(db.Boolean, default=True)
    created = db.Column(db.DateTime, default=datetime.now)
    updated = db.Column(db.DateTime, onupdate=datetime.now)
    date_sang = db.Column(db.String(1000))


class Lyrics(db.Model):
    """Docstring."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    lyrics = db.Column(db.String(1000))
    created = db.Column(db.DateTime, default=datetime.now)
    updated = db.Column(db.DateTime, onupdate=datetime.now)


class Songs(db.Model):
    """Docstring."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    origin = db.Column(db.String(50))
    tempo = db.Column(db.String(10))
    language = db.Column(db.String(10))
    message = db.Column(db.String(50))
    lyrics = db.Column(db.Boolean, default=False)
    category = db.Column(db.String(10))
    comment = db.Column(db.String(1000))
    created = db.Column(db.DateTime, default=datetime.now)
    updated = db.Column(db.DateTime, onupdate=datetime.now)
    date_sang = db.Column(db.String(1000))
