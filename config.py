import os
    
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "2f336f67d6e8c38a177035e718131a8a2f8609671532e456"

class DevConfig(Config): #used as the local env
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = "8ccd11b11afa14777a196a0833f220859f33dd7fb27a3831"

class StageConfig(Config):
    DEBUG = True
    #SECRET_KEY is set within an env var in Heroku

class ProdConfig(Config):
    DEBUG = False
    #SECRET_KEY is set within an env var in Heroku



