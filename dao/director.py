from dao.model.director import Director


class DirectorDAO:
    """
    Класс доступа данным из таблицы БД director
    """
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        """
        получение режиссера по его id
        :param did: str
            id
        :return: Director
        """
        return self.session.query(Director).get(bid)

    def get_all(self):
        """
        получение всех данных из таблицы
        :return: list[Director]
        """
        return self.session.query(Director).all()

    def create(self, director_d):
        """
        Создание новой записи
        :return: Director
        """
        ent = Director(**director_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        """
        удаление записи с Id
        """
        director = self.get_one(rid)
        self.session.delete(director)
        self.session.commit()

    def update(self, director_d):
        """
        Обновление записи
        """
        director = self.get_one(director_d.get("id"))
        director.name = director_d.get("name")

        self.session.add(director)
        self.session.commit()
