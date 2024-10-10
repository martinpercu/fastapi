from models.film import Film as FilmModel


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
    
