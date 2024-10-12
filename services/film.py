from models.film import Film as FilmModel
from schemas.film import Film


class FilmService():

    def __init__(self, db) -> None:
        self.db = db

    def get_films(self):
        result = self.db.query(FilmModel).all()
        return result
    
    def get_film(self, id):
        result = self.db.query(FilmModel).filter(FilmModel.id == id).first()
        return result
    
    def get_films_by_category(self, category):
        result = self.db.query(FilmModel).filter(FilmModel.category == category).all()
        return result
    
    def create_film(self, film: Film):
        new_film = FilmModel(**film.dict())
        self.db.add(new_film)
        self.db.commit()
        return
    
    def update_film(self, id: int, data: Film):
        film = self.db.query(FilmModel).filter(FilmModel.id == id).first()
        film.title = data.title
        film.overview = data.overview
        film.year = data.year
        film.rating = data.rating
        film.category = data.category
        self.db.commit()
        return
    
    def delete_film(self, id: int):
        self.db.query(FilmModel).filter(FilmModel.id == id).delete()
        self.db.commit()
        return
