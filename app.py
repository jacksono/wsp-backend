"""Module to initialise and configure the flask app and the db."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configuration.config import app_config
from flask_restful import Api
from flask_cors import CORS, cross_origin # noqa

app = Flask(__name__)
CORS(app)
# app.config.from_object(app_config["production"])
app.config.from_object(app_config["development"])
db = SQLAlchemy(app)


api = Api(app=app, prefix="/api/v1")
