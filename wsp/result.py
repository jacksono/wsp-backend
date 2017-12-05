"""Module to define buckeltist endpoints."""

from flask_restful import Resource, reqparse, marshal, fields
from wsp.models import SongsToGlory, Songs, Lyrics
from flask import request
from app import db

song_serializer = {"title": fields.String,
                   "origin": fields.String,
                   "tempo": fields.String,
                   "category": fields.String,
                   "message": fields.String,
                   "language": fields.String,
                   "created": fields.DateTime,
                   "updated": fields.DateTime}

def get_single_song(song_title):  # noqa
    """
       Returns a single song
        """
    song = Songs.query.filter_by(title=song_title).first()
    output = {
        "title": song.title,
        "origin": song.origin,
        "tempo": song.tempo,
        "message": song.message,
        "category": song.category,
        "language": song.language,
        "created": song.created,
        "updated": song.updated
    }
    return marshal(output, song_serializer), 200


class GetAllSongsToGlory(Resource):
    """Shows all results for STG. Route: /api/v1/stg/ using GET."""

    def get(self):  # noqa
        """
           End point for returning all results for STG
            """
        stg = SongsToGlory.query.all()
        stg_results = []
        for result in stg:
            output = {
                "id": result.id,
                "title": result.title,
                "origin": result.origin,
                "tempo": 'TEMPO',
                "album": result.album,
                "category": result.category,
                "language": result.language,
                "created": result.created,
                "updated": result.updated
            }
            stg_results.append(output)
            output = {}
        return stg_results


class GetSingleSong(Resource):
    """Shows a single song . Route: /api/v1/songs/<song_title> using GET."""

    def get(self, song_title):  # noqa
        """
           End point for returning a single song
            """
        return get_single_song(song_title)


class GetAllSongs(Resource):
    """Shows all results for STG. Route: /api/v1/songs/ using GET."""

    def get(self):  # noqa
        """
           End point for returning all songs
            """
        args = request.args.to_dict()
        songs = Songs.query.all()
        songs_results = []
        search_by_title = args.get("q")
        # if search_by_title.find("%20"):
        #     search_by_title = search_by_title.replace("%10", " ")
        if search_by_title:
            return get_single_song(search_by_title)

        for result in songs:
            output = {
                "id": result.id,
                "title": result.title,
                "origin": result.origin,
                "tempo": result.tempo,
                "message": result.message,
                "category": result.category,
                "language": result.language,
                "created": result.created,
                "updated": result.updated
            }
            songs_results.append(marshal(output, song_serializer))
            output = {}
        return songs_results, 200


class GetAllPraiseSongs(Resource):
    """Shows all results for praise songs. Route: /api/v1/praise/ using GET."""

    def get(self):  # noqa
        """
           End point for returning all praise songs
            """
        songs = Songs.query.filter_by(category="PRAISE")
        songs_results = []
        id = 1
        for result in songs:
            output = {
                "id": id,
                "title": result.title,
                "origin": result.origin,
                "tempo": result.tempo,
                "message": result.message,
                "category": result.category,
                "language": result.language,
                "created": result.created,
                "updated": result.updated
            }
            songs_results.append(marshal(output, song_serializer))
            output = {}
            id += 1
        return songs_results


class GetAllWorshipSongs(Resource):
    """Shows all results for worship songs. Route: /api/v1/worship/ using GET."""

    def get(self):  # noqa
        """
           End point for returning all worship songs
            """
        songs = Songs.query.filter_by(category="WORSHIP")
        songs_results = []
        id = 1
        for result in songs:
            output = {
                "id": id,
                "title": result.title,
                "origin": result.origin,
                "tempo": result.tempo,
                "message": result.message,
                "category": result.category,
                "language": result.language,
                "created": result.created,
                "updated": result.updated
            }
            songs_results.append(marshal(output, song_serializer))
            output = {}
            id += 1
        return songs_results


class GetOtherSongs(Resource):
    """Shows all results for other songs. Route: /api/v1/other/ using GET."""

    def get(self):  # noqa
        """
           End point for returning all other songs
            """
        songs = Songs.query.filter(Songs.category != "PRAISE")
        songs_results = []
        id = 1
        for result in songs:
            if result.category != "WORSHIP":
                if result.category != "STG":
                    output = {
                        "id": id,
                        "title": result.title,
                        "origin": result.origin,
                        "tempo": result.tempo,
                        "message": result.message,
                        "category": result.category,
                        "language": result.language,
                        "created": result.created,
                        "updated": result.updated
                    }
                    songs_results.append(marshal(output, song_serializer))
                    output = {}
                    id += 1
        return songs_results


class EditSong(Resource):
    """Update a song list: Route: PUT /details/<song>."""

    def put(self, song_title):  # noqa
        """Docstring.
            """
        parser = reqparse.RequestParser()
        parser.add_argument(
            "title",
            required=True,
            help="Please enter a new title.")
        parser.add_argument(
                            "category",
                            required=False,
                            )
        parser.add_argument(
                            "origin",
                            required=False,
                            )
        parser.add_argument(
                            "tempo",
                            required=False,
                            )
        parser.add_argument(
                            "message",
                            required=False,
                            )
        parser.add_argument(
                            "language",
                            required=False,
                            )
        args = parser.parse_args()
        title, category, origin, tempo, message, language = (args["title"],
                                                             args["category"],
                                                             args["origin"],
                                                             args["tempo"],
                                                             args["message"],
                                                             args["language"])
        song = Songs.query.filter_by(title=song_title).first()
        song.title = title
        song.category = category
        song.origin = origin
        song.tempo = tempo
        song.message = message
        song.language = language

        try:
            db.session.add(song)
            db.session.commit()
        except:
            """Show when the the title already exists"""
            db.session.rollback()
            return {"message": "Error Somewhere"}, 400
        msg = {"msg": "Updated succesfully"}
        msg.update(marshal({"title": title,
                            "category": category,
                            "origin": origin,
                            "tempo": tempo,
                            "message": message,
                            "language": language,
                            "created": song.created,
                            "updated": song.updated
                            },
                           song_serializer)
                   )
        return msg


class SongLyrics(Resource):
    """Shows Lyrics for selected song. Route: /api/v1/lyrics/<song_title> using GET."""

    def get(self, song_title):  # noqa
        """
           End point for returning song lyrics
            """
        song_lyrics = Lyrics.query.filter_by(title=song_title).first().lyrics
        output = {
            "message": "Lyrics found",
            "lyrics": song_lyrics
        }
        return output


class AddSong(Resource):
    """Add a new song: Route: POST /add/."""

    def post(self):  # noqa
        """Docstring.
            """
        parser = reqparse.RequestParser()
        parser.add_argument(
            "title",
            required=True,
            help="Please enter a song title.")
        parser.add_argument(
                            "category",
                            required=False,
                            )
        parser.add_argument(
                            "origin",
                            required=False,
                            )
        parser.add_argument(
                            "tempo",
                            required=False,
                            )
        parser.add_argument(
                            "message",
                            required=False,
                            )
        parser.add_argument(
                            "language",
                            required=False,
                            )
        args = parser.parse_args()
        title, category, origin, tempo, message, language = (args["title"],
                                                             args["category"],
                                                             args["origin"],
                                                             args["tempo"],
                                                             args["message"],
                                                             args["language"])
        songs_obj = Songs(title=title,
                          origin=origin,
                          message=message,
                          tempo=tempo,
                          category=category,
                          language=language,
                          )
        try:
            db.session.add(songs_obj)
            db.session.commit()
        except:
            """Show when the the title already exists"""
            db.session.rollback()
            return {"message": "Error Somewhere"}, 400
        msg = {"msg": "Added succesfully"}
        msg.update({"title": title,
                    "category": category,
                    "origin": origin,
                    "tempo": tempo,
                    "message": message,
                    "language": language
                    })
        return msg
