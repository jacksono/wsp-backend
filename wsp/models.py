"""Module to create the models for the app."""

from app import db


class SongsToGlory(db.Model):
    """Docstring."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    origin = db.Column(db.String(50))
    tempo = db.Column(db.String(10))
    language = db.Column(db.String(10))
    album = db.Column(db.String(50))
    category = db.Column(db.String(10))
    lyrics = db.Column(db.String(1000))


class Lyrics(db.Model):
    """Docstring."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    lyrics = db.Column(db.String(1000))


class Songs(db.Model):
    """Docstring."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    origin = db.Column(db.String(50))
    tempo = db.Column(db.String(10))
    language = db.Column(db.String(10))
    message = db.Column(db.String(50))
    category = db.Column(db.String(10))