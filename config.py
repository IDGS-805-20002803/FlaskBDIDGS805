import os

from sqlalchemy import create_engine

class config(object):
    SECRET_KEY ="ClaveSecreta"
    SESSION_COOKIE_SECURE=False
    

class DevelopmentConfig(config):
    DEBUG=True
    SQLALCHEMY_DATABASES_URI='mysql+pymysql://adair:root@127.0.0.1/bdidgs805'
    SQLALCHEMY_TRACK_MODIFICATIONS=False