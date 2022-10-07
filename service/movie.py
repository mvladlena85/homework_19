from dao.movie import MovieDAO


class MovieService:
    """
    Описание бизнес логики для объекта "фильм"
    """
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid):
        """Получение фильма по его ID"""
        return self.dao.get_one(bid)

    def get_all(self, filters):
        """Получение списка фильмов по заданным критериям"""
        if filters.get("director_id") is not None:
            movies = self.dao.get_by_director_id(filters.get("director_id"))
        elif filters.get("genre_id") is not None:
            movies = self.dao.get_by_genre_id(filters.get("genre_id"))
        elif filters.get("year") is not None:
            movies = self.dao.get_by_year(filters.get("year"))
        else:
            movies = self.dao.get_all()
        return movies

    def create(self, movie_d):
        """Создание нового фильма"""
        return self.dao.create(movie_d)

    def update(self, movie_d):
        """Изменение данных фильма"""
        self.dao.update(movie_d)
        return self.dao

    def delete(self, rid):
        """Удаление фильма"""
        self.dao.delete(rid)
