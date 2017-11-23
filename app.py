"""Module to initialise and configure the flask app and the db."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configuration.config import app_config
from flask_restful import Api
from flasgger import Swagger
from flask_cors import CORS, cross_origin # noqa

app = Flask(__name__)
CORS(app)
app.config.from_object(app_config["development"])
db = SQLAlchemy(app)


template = {
  "swagger": "2.0",
  "info": {
    "title": "INM API",
    "description": "API for managing research results",
    "contact": {
      "responsibleDeveloper": "Jackson Onyango",
      "email": "jackson.onyango@andela.com",
    },
    "version": "1.0"
  },
  "schemes": [
    "http",
    "https"
  ],
  "produces": ["application/x-www-form-urlencoded",
               "application/json",
               "application/txt"],
  "operationId": "getmyData",
  "content-type": "text"
}

api = Api(app=app, prefix="/api/v1")
swagger = Swagger(app, template=template)
