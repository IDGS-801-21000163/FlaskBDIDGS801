import os
from sqlalchemy import create_engine

class Config:
    SECRET_KEY = 'ClaveSecreta'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/IDGS'
    SQLALCHEMY_TRACK_MODIFICATIONS = False