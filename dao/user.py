from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, username):
        try:
            return self.session.query(User).filter(User.username == username).all()[0]
        except Exception as e:
            print(e)
            return None

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_d):
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, username):
        user = self.get_one(username)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_d):
        user = self.get_one(user_d.get("user_to_change"))
        user.username = user_d.get("username")
        user.password = user_d.get("password")
        user.role = user_d.get("role")

        self.session.add(user)
        self.session.commit()




