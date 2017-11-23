"""Module to create the models for the app."""

from app import db


class SongsToGlory(db.Model):
    """Maps bucketlists table which contains bucketlist inforamtion."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    origin = db.Column(db.String(50))
    tempo = db.Column(db.String(10))
    language = db.Column(db.String(10))
    album = db.Column(db.String(50))
    category = db.Column(db.String(10))
