import os
from flask import Flask
app = Flask(__name__)

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'

class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/data.db'
    SECRET_KEY = 'VERY_BIG_SECRET'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
