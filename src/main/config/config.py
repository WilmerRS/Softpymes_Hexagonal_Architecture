class Config(object):
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class PrdConfig(Config):
    pass


class TestConfig(Config):
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://XXXX:XXXX@127.0.0.1:3306/victoria?charset=utf8'


config = {
    'development': DevConfig,
    'test': TestConfig,
    'production': PrdConfig
}
