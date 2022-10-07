from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service
from service.decorators import auth_required, admin_required

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    @auth_required
    def post(self):
        data = request.json
        genre = genre_service.create(data)
        return "", 201


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    @auth_required
    def get(self, gid):
        genre = genre_service.get_one(gid)
        if not genre:
            return "Wrong genre id", 404
        sm_d = GenreSchema().dump(genre)
        return sm_d, 200

    @admin_required
    @auth_required
    def put(self, gid):
        data = request.json
        if "id" not in data:
            data["id"] = gid
        genre_service.update(data)
        return "", 204

    @admin_required
    @auth_required
    def delete(self, gid):
        genre_service.delete(gid)
        return "", 204
