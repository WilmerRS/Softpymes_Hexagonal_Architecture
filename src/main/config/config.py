import os


class Config(object):
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class PrdConfig(Config):
    pass


class TestConfig(Config):
    pass


class DevConfig(Config):
    # DATABASE = os.environ.get('DATABASE')
    # USER = os.environ.get('USER')
    # PASSWORD = os.environ.get('PASSWORD')
    # HOST = os.environ.get('HOST')
    # PORT = os.environ.get('PORT')
    # DATABASE_NAME = os.environ.get('DATABASE_NAME')
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://softpymes:softpymes@localhost:3306/softpymes_v1'


config = {
    'development': DevConfig,
    'test': TestConfig,
    'production': PrdConfig
}
