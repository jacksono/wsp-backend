"""Module to run the API."""

from wsp.user_routes import (Home)
from wsp.result import GetAllSongsToGlory
from app import api, app


# Create api endpoints
api.add_resource(Home, "/")
api.add_resource(GetAllSongsToGlory, "/stg/")

if __name__ == "__main__":
    app.run()
