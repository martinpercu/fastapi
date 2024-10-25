from fastapi import APIRouter
from fastapi import Path, Query, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from models.film import Film as FilmModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.film import FilmService
from schemas.film import Film

film_router = APIRouter()


@film_router.get('/films', tags=['Films'], response_model=List[Film], status_code=200, dependencies=[Depends(JWTBearer())])
def get_films() -> List[Film]:
    db = Session()
    result = FilmService(db).get_films()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@film_router.get('/films/{id}', tags=['Films'], response_model=Film)
def get_film(id: int = Path(ge=1, le=1000)) -> Film:
    db = Session()
    result = FilmService(db).get_film(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "FILM NON TROUVÉ"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@film_router.get('/films/', tags=['Films'], response_model=List[Film])
def get_film_by_category(category: str = Query(min_length=6, max_length=16)) -> List[Film]:
    db = Session()
    result = FilmService(db).get_films_by_category(category)
    if not result:
        return JSONResponse(status_code=404, content={'message': "FILM NON TROUVÉ"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@film_router.post('/films', tags=['Films'], response_model=dict, status_code=201)
def create_film(film: Film) -> dict:
    db = Session()
    FilmService(db).create_film(film)
    return JSONResponse(status_code=201, content={"message": "Film enregistré"})


@film_router.put('/films/{id}', tags=['Films'], response_model=dict,status_code=200)
def update_film(id: int, film: Film) -> dict:
    db = Session()
    result = FilmService(db).get_film(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "FILM NON TROUVÉ"})
    
    FilmService(db).update_film(id, film)
    return JSONResponse(status_code=200, content={"message": "Film actualisé"})


@film_router.delete('/films/{id}', tags=['Films'], response_model=dict, status_code=200)
def delete_film(id: int) -> dict:
    db = Session()
    result = db.query(FilmModel).filter(FilmModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "FILM NON TROUVÉ"})
    FilmService(db).delete_film(id)
    return JSONResponse(status_code=200, content={"message": "Film effacé"})

