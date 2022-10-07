from flask import request
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service
from service.decorators import auth_required, admin_required

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    @auth_required
    @admin_required
    def post(self):
        data = request.json
        director = director_service.create(data)
        return "", 201


@director_ns.route('/<int:uid>')
class DirectorView(Resource):
    @auth_required
    def get(self, uid):
        r = director_service.get_one(uid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    @auth_required
    @admin_required
    def put(self, uid):
        data = request.json
        if "id" not in data:
            data["id"] = uid
        director_service.update(data)
        return "", 204

    @auth_required
    @admin_required
    def delete(self, uid):
        director_service.delete(uid)
        return "", 204
