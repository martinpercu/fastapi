from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List


app = FastAPI()
app.title = "An app with FastAPI"
app.version = "0.1"

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


films = [
    {
        "id": 1,
		"title": "Avatar",
		"overview": "Un human va a la planete pandora ou tous sont bleus ....",
		"year": 2012,
		"rating": 7.8,
		"category": "Action"
    },
    {
        "id": 2,
		"title": "Avatar 2",
		"overview": "Un human va a la planete pandora ou tous sont bleus ....",
		"year": 2019,
		"rating": 7.2,
		"category": "Action"
    },
    {
        "id": 3,
		"title": "Avatar 3",
		"overview": "Un human va a la planete pandora ou tous sont bleus ....",
		"year": 2020,
		"rating": 7.2,
		"category": "Action"
    },
    {
        "id": 4,
		"title": "Funny Avatar",
		"overview": "Un human va a la planete pandora ou tous sont bleus ....",
		"year": 2005,
		"rating": 7.2,
		"category": "Comedy"
    },
    {
        "id": 5,
		"title": "Funny Avatar",
		"overview": "Un human va a la planete pandora ou tous sont bleus ....",
		"year": 2020,
		"rating": 7.2,
		"category": "Comedy"
    }
]

@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('<h2>"Bonjour monde"</h2>')

@app.get('/films', tags=['Films'], response_model=List[Film], status_code=200)
def get_films() -> List[Film]:
    return JSONResponse(status_code=200, content=films)

@app.get('/films/{id}', tags=['Films'], response_model=Film)
def get_film(id: int = Path(ge=1, le=1000)) -> Film:
    for item in films:
        if item['id'] == id:
            return JSONResponse(status_code=200,content=item)
    return JSONResponse(status_code=404, content=[])
'''
@app.get('/films/old/', tags=['Films'])
def get_film_by_category(category: str):
    list_films = []
    for item in films:
        if item['category'] == category:
            list_films.append(item)
    return list_films
'''

# a clever query from above...
@app.get('/films/', tags=['Films'], response_model=List[Film])
def get_film_by_category2(category: str = Query(min_length=6, max_length=16)) -> List[Film]:
    data = [item for item in films if item['category'] == category]
    return JSONResponse(content=data)

'''
@app.get('/films/old/{category}/{year}', tags=['Films'])
def get_film_by_category_or_year(category: str, year: int):
    list_films = []
    for item in films:
        if item['category'] == category or item['year'] == year:
            list_films.append(item)
    return list_films
'''
# a clever query from above...
@app.get('/films/{category}/{year}', tags=['Films'])
def get_film_by_category_or_year2(category: str, year: int):
    return [item for item in films if item['category'] == category or item['year'] == year]



@app.post('/films', tags=['Films'], response_model=dict, status_code=201)
def create_film(film: Film) -> dict:
    films.append(film)
    return JSONResponse(status_code=201, content={"message": "Film enregistré"})


@app.put('/films/{id}', tags=['Films'], response_model=dict,status_code=200)
def update_film(id: int, film: Film) -> dict:
    for item in films:
        if item['id'] == id:
            item['title'] = film.title
            item['overview'] = film.overview
            item['year'] = film.year
            item['rating'] = film.rating
            item['category'] = film.category
            return JSONResponse(status_code=200, content={"message": "Film actualisé"})


@app.delete('/films/{id}', tags=['Films'], response_model=dict, status_code=200)
def delete_film(id: int) -> dict:
    for item in films:
        if item['id'] == id:
            films.remove(item)
            return JSONResponse(status_code=200, content={"message": "Film effacé"})

