from marshmallow import Schema, fields

from setup_db import db


class User(db.Model):
    """
    Модель SQLAlchemy для объекта "пользователь".
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    role = db.Column(db.String)


class UserSchema(Schema):
    """
    Схема для сериализации объекта "фильм"
    """
    id = fields.Int(dump_only=True)
    username = fields.Str()
    password = fields.Str()
    role = fields.Str()