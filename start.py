"""Module to run the API."""

from wsp.user_routes import (Home)
from wsp.result import (GetAllSongsToGlory, GetAllSongs, GetAllPraiseSongs,
                        GetAllWorshipSongs, GetOtherSongs, EditSong, SongLyrics,
                        AddSong, GetSingleSong, AddLyrics, EditLyrics)
from app import api, app


# Create api endpoints
api.add_resource(Home, "/")
api.add_resource(GetAllSongsToGlory, "/stg/")
api.add_resource(GetAllSongs, "/songs/")
api.add_resource(GetAllPraiseSongs, "/praise/")
api.add_resource(GetAllWorshipSongs, "/worship/")
api.add_resource(GetOtherSongs, "/other/")
api.add_resource(EditSong, "/<song_category>/<song_title>")
api.add_resource(SongLyrics, "/lyrics/<song_title>")
api.add_resource(AddLyrics, "/lyrics/<song_title>")
api.add_resource(EditLyrics, "/lyrics/<song_title>")
api.add_resource(AddSong, "/add/")
api.add_resource(GetSingleSong, "/song/<song_category>/<song_title>")

if __name__ == "__main__":
    app.run()
