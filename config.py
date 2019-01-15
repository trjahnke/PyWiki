import os
import json

with open("secrets.json", "r") as f:
    config = json.load(f)
    
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = config["DEFAULT"]["SECRET_KEY"]

class DevConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = config["DEV"]["SECRET_KEY"]

class StageConfig(Config):
    DEBUG = True
    SECRET_KEY = config["STAGE"]["SECRET_KEY"]

class ProdConfig(Config):
    DEBUG = False
    SECRET_KEY = config["PRODUCTION"]["SECRET_KEY"]



