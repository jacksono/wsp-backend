"""Module to store settings for different environments."""

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Set the default configurations."""

    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + \
        os.path.join(basedir, "wsp.sqlite")


class DevelopmentConfig(Config):
    """Set the configurations for the development environment."""

    DEBUG = True
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = 'postgres://oaogkvqqbendph:ea2ffa9f169f4d5b2133db902c984f56a190172c3332f004d9fa1a78360157c0@ec2-54-197-232-155.compute-1.amazonaws.com:5432/ddu3i2c2a81vju'
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + \
        os.path.join(basedir, "wsp.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'sgykhzifsxaqca:343f51064cb2dbcd7bb9b08d13b340396e5615570fdb6b29b36c51b9ca7b944b@ec2-54-243-255-57.compute-1.amazonaws.com:5432/d8894uku5kb28i'


class TestingConfig(Config):
    """Set the configurations for the testing environment."""

    DEBUG = True
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = 'postgres://sgykhzifsxaqca:343f51064cb2dbcd7bb9b08d13b340396e5615570fdb6b29b36c51b9ca7b944b@ec2-54-243-255-57.compute-1.amazonaws.com:5432/d8894uku5kb28i'
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + \
        os.path.join(basedir, "test.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'sgykhzifsxaqca:343f51064cb2dbcd7bb9b08d13b340396e5615570fdb6b29b36c51b9ca7b944b@ec2-54-243-255-57.compute-1.amazonaws.com:5432/d8894uku5kb28i'


class ProductionConfig(Config):
    """Set the configurations for the production environment."""

    DEBUG = False
    TESTING = False
    # SQLALCHEMY_DATABASE_URI = 'postgres://sgykhzifsxaqca:343f51064cb2dbcd7bb9b08d13b340396e5615570fdb6b29b36c51b9ca7b944b@ec2-54-243-255-57.compute-1.amazonaws.com:5432/d8894uku5kb28i'


app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
