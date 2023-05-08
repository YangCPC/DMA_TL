class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345678@127.0.0.1:3306/flask_revisit_20230309'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SECRET_KEY = 'afsjskahsfdkhadsjk'

class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True

class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False