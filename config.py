import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'developement key'
    DEBUG = os.environ.get('DEBUG') or True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:////' + basedir + '/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class OtherConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin:admin@localhost/mac'