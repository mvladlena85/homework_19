from dao.user import UserDAO
from service.auth import decode_hash, get_hash


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, username):
        return self.dao.get_one(username)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_d):
        password = user_d["password"]
        user_d["password"] = get_hash(password)
        print(type(user_d["password"]))
        return self.dao.create(user_d)

    def update(self, user_d):
        self.dao.update(user_d)
        return self.dao

    def delete(self, username):
        self.dao.delete(username)



