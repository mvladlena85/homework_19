class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Параметры для хеширования паролей
    PWD_HASH_SALT = b'secret here'
    PWD_HASH_ITERATIONS = 100000
    PWD_ALGO = 'sha256'
    # Параметры для генерации токенов
    TOKEN_EXPIRE_MINUTES = 15
    TOKEN_EXPIRE_DAYS = 130
    SECRET_KEY = '249y823r9v8238r9u'
    ALGO = 'HS256'

