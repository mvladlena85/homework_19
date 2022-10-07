from dao.model.genre import Genre


class GenreDAO:
    """
    Класс доступа данным из таблицы БД genre
    """
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        """
        получение одной записи по ее id
        :param gid: str
            id
        :return: Genre
        """
        return self.session.query(Genre).get(bid)

    def get_all(self):
        """
        получение всех данных из таблицы
        :return: list[Genre]
        """
        return self.session.query(Genre).all()

    def create(self, genre_d):
        """
        Создание записи в таблице
        :return: Genre
        """
        ent = Genre(**genre_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        """
        удаление записи из таблицы по id
        :param rid: str
            id
        """
        genre = self.get_one(rid)
        self.session.delete(genre)
        self.session.commit()

    def update(self, genre_d):
        """
        обновление данных
        :param genre_d: dict
            данные по жанру
        """
        genre = self.get_one(genre_d.get("id"))
        genre.name = genre_d.get("name")

        self.session.add(genre)
        self.session.commit()
