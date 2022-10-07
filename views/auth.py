from flask import request
from flask_restx import Namespace, Resource

from implemented import user_service
from service.auth import refresh_tokens, generate_token


"""
Представления для обработки запросов к /auth/ - авторизация пользователя
"""
auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        username = request.json.get("username")
        password = request.json.get("password")
        user = user_service.get_one(username)
        password_hash = user.password
        print(username, password, password_hash)
        tokens = generate_token(username=username, password=password, password_hash=password_hash, is_refresh=False)
        if tokens is None:
            return "Некорректные имя пользователя или пароль", 401
        return tokens, 201

    def put(self):
        refresh_token = request.json.get("refresh_token")
        tokens = refresh_tokens(refresh_token)
        if tokens is None:
            return "Некорректный токен", 401
        return tokens, 201
