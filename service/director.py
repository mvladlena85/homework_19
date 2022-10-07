from dao.director import DirectorDAO


class DirectorService:
    """
    Описание бизнес логики для объекта "режиссер"
    """
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, bid):
        """Получение режиссера по его id"""
        return self.dao.get_one(bid)

    def get_all(self):
        """Получение полного списка режиссеров"""
        return self.dao.get_all()

    def create(self, director_d):
        """Создание режиссера"""
        return self.dao.create(director_d)

    def update(self, director_d):
        """Обновление данных режиссера"""
        self.dao.update(director_d)
        return self.dao

    def delete(self, rid):
        """Удаление режиссера"""
        self.dao.delete(rid)
