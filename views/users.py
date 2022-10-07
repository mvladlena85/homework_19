from flask import request
from flask_restx import Namespace, Resource

from dao.model.user import UserSchema
from implemented import user_service


"""
Представления для обработки запросов к /users/
"""
user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        users = user_service.get_all()
        users_json = UserSchema(many=True).dump(users)
        return users_json, 200

    def post(self):
        data = request.json
        user = user_service.create(data)
        return "", 201


@user_ns.route('/<string:username>')
class UserView(Resource):
    def get(self, username):
        user = user_service.get_one(username)
        user_json = UserSchema().dump(user)
        return user_json, 200

    def put(self, username):
        data = request.json
        data["user_to_change"] = username
        # if "id" not in data:
        #     data["id"] = username
        user = user_service.update(data)
        return "", 204

    def delete(self, username):
        user_service.delete(username)
        return "", 204
