"""Module to define buckeltist endpoints."""

from flask_restful import Resource, reqparse, marshal, fields
from wsp.models import SongsToGlory, Songs, Lyrics
from flask import request
from app import db

song_serializer = {"title": fields.String,
                   "id": fields.Integer,
                   "origin": fields.String,
                   "tempo": fields.String,
                   "category": fields.String,
                   "message": fields.String,
                   "language": fields.String,
                   "lyrics": fields.String,
                   "comment": fields.String,
                   "created": fields.DateTime,
                   "updated": fields.DateTime}

def get_single_song(song_title, category):  # noqa
    """
       Returns a single song
        """
    if category == "STG":
        song = SongsToGlory.query.filter_by(title=song_title).first()
    else:
        song = Songs.query.filter_by(title=song_title).first()

    output = {
        "title": song.title,
        "origin": song.origin,
        "tempo": song.tempo,
        "message": song.message,
        "category": song.category,
        "language": song.language,
        "lyrics": song.lyrics,
        "comment": song.comment,
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
                "tempo": result.tempo,
                "message": result.message,
                "category": result.category,
                "lyrics": result.lyrics,
                "comment": result.comment,
                "language": result.language,
                "created": result.created,
                "updated": result.updated
            }
            stg_results.append(marshal(output, song_serializer))
            output = {}
        return stg_results


class GetSingleSong(Resource):
    """Shows a single song . Route: /api/v1/songs/<category>/<song_title> using GET."""

    def get(self, song_title, category):  # noqa
        """
           End point for returning a single song
            """
        return get_single_song(song_title, category)


class GetAllSongs(Resource):
    """Shows all results for STG. Route: /api/v1/songs/ using GET."""

    def get(self):  # noqa
        """
           End point for returning all songs
            """
        # args = request.args.to_dict()
        songs = Songs.query.all()
        songs.extend(SongsToGlory.query.all())
        songs_results = []
        # search_by_title = args.get("q")
        # if search_by_title.find("%20"):
        #     search_by_title = search_by_title.replace("%10", " ")
        # if search_by_title:
        #     return get_single_song(search_by_title)

        for result in songs:
            output = {
                "id": result.id,
                "title": result.title,
                "origin": result.origin,
                "tempo": result.tempo.upper(),
                "message": result.message.upper(),
                "category": result.category,
                "lyrics": result.lyrics,
                "comment": result.comment,
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
        songs = Songs.query.filter_by(category="PRAISE").order_by(Songs.created.desc())
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
                "comment": result.comment,
                "lyrics": result.lyrics,
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
        songs = Songs.query.filter_by(category="WORSHIP").order_by(Songs.created.desc())
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
                "comment": result.comment,
                "lyrics": result.lyrics,
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
        songs = Songs.query.filter(Songs.category != "PRAISE").order_by(Songs.created.desc())
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
                        "lyrics": result.lyrics,
                        "comment": result.comment,
                        "created": result.created,
                        "updated": result.updated
                    }
                    songs_results.append(marshal(output, song_serializer))
                    output = {}
                    id += 1
        return songs_results


class EditSong(Resource):
    """Update a song list: Route: PUT /details/<category>/<song>."""

    def put(self, song_title, category):  # noqa
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
        parser.add_argument(
                            "comment",
                            required=False,
                            )
        parser.add_argument(
                            "lyrics",
                            required=False,
                            )
        args = parser.parse_args()
        title, category, origin, tempo, message, language, comment, lyrics = (args["title"],
                                                                              args["category"],
                                                                              args["origin"],
                                                                              args["tempo"],
                                                                              args["message"],
                                                                              args["language"],
                                                                              args["comment"],
                                                                              args["lyrics"])
        if category == "STG":
            song = SongsToGlory.query.filter_by(title=song_title).first()
            song.title = title
            song.category = category
            song.origin = origin
            song.tempo = tempo
            song.message = message
            song.language = language
            song.comment = comment
        else:
            song = Songs.query.filter_by(title=song_title).first()
            if title:
                song.title = title
            if category:
                song.category = category
            if origin:
                song.origin = origin
            if tempo:
                song.tempo = tempo
            if message:
                song.message = message
            if language:
                song.language = language
            if comment:
                song.comment = comment
            if lyrics:
                song.lyrics = lyrics

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
                            "lyrics": lyrics,
                            "created": song.created,
                            "comment": song.comment,
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
        parser.add_argument(
                            "comment",
                            required=False,
                            )
        parser.add_argument(
                            "lyrics",
                            required=False,
                            )
        args = parser.parse_args()
        title, category, origin, tempo, message, language, comment, lyrics = (args["title"],
                                                                              args["category"],
                                                                              args["origin"],
                                                                              args["tempo"],
                                                                              args["message"],
                                                                              args["language"],
                                                                              args["comment"],
                                                                              args["lyrics"])
        songs_obj = Songs(title=title,
                          origin=origin,
                          message=message,
                          tempo=tempo,
                          category=category,
                          language=language,
                          comment=comment,
                          lyrics=lyrics
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
                    "language": language,
                    "comment": comment
                    })
        return msg


class AddLyrics(Resource):
    """Add a new song lyrics: Route: POST /lyrics/<song_title>."""

    def post(self, song_title):  # noqa
        """Docstring.
            """
        parser = reqparse.RequestParser()
        parser.add_argument(
                            "lyrics",
                            required=False,
                            )

        args = parser.parse_args()
        lyrics = (args["lyrics"])

        lyrics_obj = Lyrics(title=song_title,
                            lyrics=lyrics)
        try:
            db.session.add(lyrics_obj)
            db.session.commit()
        except:
            """Show when the the title already exists"""
            db.session.rollback()
            return {"message": "Error Somewhere"}, 400
        msg = {"msg": "Added succesfully"}
        msg.update({"title": song_title,
                    "lyrics": lyrics
                    })
        return msg
