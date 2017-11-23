"""Module to initialise and configure the flask app and the db."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configuration.config import app_config
from flask_restful import Api
from flasgger import Swagger

app = Flask(__name__, template_folder="../templates")
app.config.from_object(app_config["development"])
db = SQLAlchemy(app)


template = {
  "swagger": "2.0",
  "info": {
    "title": "WSP API",
    "description": "API for managing WSP data",
    "contact": {
      "responsibleDeveloper": "Jackson Onyango",
      "email": "jackson.onyango@gmail.com",
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
