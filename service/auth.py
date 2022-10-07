import base64
import calendar
import datetime
import hashlib
import hmac
import jwt

from config import Config

"""
Вспомогательные функции для реализации авторизации пользователя
"""


def get_hash(password: str) -> bytes:
    """
    Хеширование пароля
    """
    return base64.b64encode(hashlib.pbkdf2_hmac(
        Config.PWD_ALGO,
        password.encode('utf-8'),  # Convert the password to bytes
        Config.PWD_HASH_SALT,
        Config.PWD_HASH_ITERATIONS
    ))


def decode_hash(password):
    return base64.b64decode(get_hash(password))


def compare_passwords(password_hash, password):
    """Валидация пароля по его хешу"""
    return hmac.compare_digest(get_hash(password), password_hash)


def generate_token(username, password, password_hash, is_refresh=True):
    """Генерация пары токенов: "access_token" и "refresh_token" """
    if username is None:
        return None

    if not is_refresh:
        if not compare_passwords(password_hash=password_hash, password=password):
            return None

    data = {"username": username,
            "password": password}

    minutes = datetime.datetime.utcnow() + datetime.timedelta(minutes=Config.TOKEN_EXPIRE_MINUTES)
    data['exp'] = calendar.timegm(minutes.timetuple())
    access_token = jwt.encode(data, Config.SECRET_KEY, algorithm=Config.ALGO)

    days = datetime.datetime.utcnow() + datetime.timedelta(days=Config.TOKEN_EXPIRE_DAYS)
    data['exp'] = calendar.timegm(days.timetuple())
    refresh_token = jwt.encode(data, Config.SECRET_KEY, algorithm=Config.ALGO)

    return {"access_token": access_token, "refresh_token": refresh_token}


def refresh_tokens(token):
    """Обновление пары токенов: "access_token" и "refresh_token" по refresh_token"""
    if token is None:
        return None

    try:
        token_data = jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.ALGO])
    except Exception as e:
        return None

    username = token_data.get("username")
    password = token_data.get("password")

    return generate_token(username, password, None, True)
