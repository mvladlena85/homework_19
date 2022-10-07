from dao.genre import GenreDAO


class GenreService:
    """
    Описание бизнес логики для объекта "жанр"
    """
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, bid):
        """Получение жанра по его id"""
        return self.dao.get_one(bid)

    def get_all(self):
        """Получение полного списка жанров"""
        return self.dao.get_all()

    def create(self, genre_d):
        """Создание жанра"""
        return self.dao.create(genre_d)

    def update(self, genre_d):
        """Обновление данных жанра"""
        self.dao.update(genre_d)
        return self.dao

    def delete(self, rid):
        """Удаление жанра"""
        self.dao.delete(rid)
