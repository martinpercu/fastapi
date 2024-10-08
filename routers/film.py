from fastapi import APIRouter
from fastapi import Path, Query, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from models.film import Film as FilmModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer

film_router = APIRouter()


class Film(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=8, max_length=100)
    year: int = Field(default=1987, le=2023)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=6, max_length=16)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Nom du film",
		        "overview": "Bla bla bla descrition du notre film",
		        "year": 1980,
		        "rating": 8.6,
		        "category": "Comedie"
            },
        }


@film_router.get('/films', tags=['Films'], response_model=List[Film], status_code=200, dependencies=[Depends(JWTBearer())])
def get_films() -> List[Film]:
    db = Session()
    result = db.query(FilmModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@film_router.get('/films/{id}', tags=['Films'], response_model=Film)
def get_film(id: int = Path(ge=1, le=1000)) -> Film:
    db = Session()
    result = db.query(FilmModel).filter(FilmModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "FILM NON TROUVÉ"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


'''
@film_router.get('/films/old/', tags=['Films'])
def get_film_by_category(category: str):
    list_films = []
    for item in films:
        if item['category'] == category:
            list_films.append(item)
    return list_films
'''

# a clever query from above...
@film_router.get('/films/', tags=['Films'], response_model=List[Film])
def get_film_by_category2(category: str = Query(min_length=6, max_length=16)) -> List[Film]:
    data = [item for item in films if item['category'] == category]
    return JSONResponse(content=data)

'''
@film_router.get('/films/old/{category}/{year}', tags=['Films'])
def get_film_by_category_or_year(category: str, year: int):
    list_films = []
    for item in films:
        if item['category'] == category or item['year'] == year:
            list_films.append(item)
    return list_films
'''
# a clever query from above...
@film_router.get('/films/{category}/{year}', tags=['Films'])
def get_film_by_category_or_year2(category: str, year: int):
    db = Session()
    result = db.query(FilmModel).filter(FilmModel.category == category).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@film_router.post('/films', tags=['Films'], response_model=dict, status_code=201)
def create_film(film: Film) -> dict:
    db = Session()
    new_film = FilmModel(**film.dict())
    db.add(new_film)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Film enregistré"})


@film_router.put('/films/{id}', tags=['Films'], response_model=dict,status_code=200)
def update_film(id: int, film: Film) -> dict:
    db = Session()
    result = db.query(FilmModel).filter(FilmModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "FILM NON TROUVÉ"})
    result.title = film.title
    result.overview = film.overview
    result.year = film.year
    result.rating = film.rating
    result.category = film.category
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Film actualisé"})


@film_router.delete('/films/{id}', tags=['Films'], response_model=dict, status_code=200)
def delete_film(id: int) -> dict:
    db = Session()
    result = db.query(FilmModel).filter(FilmModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "FILM NON TROUVÉ"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Film effacé"})

