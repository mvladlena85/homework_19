from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, username):
        """
        получение одной записи по имени пользователя
        :param username: str
            имя пользователя
        :return: User
        """
        try:
            return self.session.query(User).filter(User.username == username).all()[0]
        except Exception as e:
            print(e)
            return None

    def get_all(self):
        """
        получение всех данных из таблицы
        :return: list[User]
        """
        return self.session.query(User).all()

    def create(self, user_d):
        """
        создание новой записи в таблице
        :param user_d: dict
        :return: User
        """
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, username):
        """
        удаление записи по ее username
        :param username: str
            имя пользователя
        :return: None
        """
        user = self.get_one(username)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_d):
        """
        обновление данных пользователя
        :param user_d: dict
        """
        user = self.get_one(user_d.get("user_to_change"))
        user.username = user_d.get("username")
        user.password = user_d.get("password")
        user.role = user_d.get("role")

        self.session.add(user)
        self.session.commit()




