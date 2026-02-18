import os

from sqlalchemy import create_engine

class config(object):
    SECRET_KEY ="ClaveSecreta"
    SESSION_COOKIE_SECURE=False
    

class DevelopmentConfig(config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
    "mysql+pymysql://root:root@127.0.0.1/BDIDGS805"
    "?charset=utf8mb4"
)

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    