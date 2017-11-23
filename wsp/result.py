"""Module to define buckeltist endpoints."""

from flask_restful import Resource
from wsp.models import SongsToGlory


class GetAllSongsToGlory(Resource):
    """Shows all results for STG. Route: /api/v1/stg/ using GET."""

    def get(self):  # noqa
        """
           End point for returning all results for STG
           ---
           parameters:
             - in: header
               name: token
               type: string
               description: Access token
               required: true
           responses:
             200:
               description: Returns all results.

            """
        stg = SongsToGlory.query.all()
        stg_results = []
        for result in stg:
            output = {
                "title": result.title,
                "origin": result.origin,
                "tempo": result.tempo,
                "album": result.album,
                "category": result.category
            }
            stg_results.append(output)
            output = {}
        return stg_results
