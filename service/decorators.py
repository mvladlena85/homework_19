import jwt
from flask import request
from flask_restx import abort

from config import Config
from implemented import user_service


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization'not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.ALGO])
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
        return func(*args, ** kwargs)
    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization'not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.ALGO])
            username = data.get("username")
            user = user_service.get_one(username)
            print(user.role)
            if user.role != "admin":
                abort(403)

        except Exception as e:
            print("JWT Decode Exception", e)
            abort(403)
        return func(*args, ** kwargs)
    return wrapper
