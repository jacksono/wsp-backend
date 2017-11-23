"""Module to define index page."""
from flask_restful import Resource


class Home(Resource):
    """Response to the index route using the GET method."""

    def get(self):  # noqa
        """
           This is the index page with a welcome message
           ---
           responses:
             200:
               description: A simple welcome message is returned
            """
        return {"message": "You are WELCOME!!. "}
