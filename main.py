from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse


app = FastAPI()
app.title = "An app with FastAPI"
app.version = "0.1"

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

@app.get('/films', tags=['Films'])
def get_films():
    return films

@app.get('/films/{id}', tags=['Films'])
def get_film(id: int):
    for item in films:
        if item['id'] == id:
            return item
    return "Film not find"

@app.get('/films/old/', tags=['Films'])
def get_film_by_category(category: str):
    list_films = []
    for item in films:
        if item['category'] == category:
            list_films.append(item)
    return list_films


# a clever query from above...
@app.get('/films/', tags=['Films'])
def get_film_by_category2(category: str):
    return [item for item in films if item['category'] == category]


@app.get('/films/old/{category}/{year}', tags=['Films'])
def get_film_by_category_or_year(category: str, year: int):
    list_films = []
    for item in films:
        if item['category'] == category or item['year'] == year:
            list_films.append(item)
    return list_films

# a clever query from above...
@app.get('/films/{category}/{year}', tags=['Films'])
def get_film_by_category_or_year2(category: str, year: int):
    return [item for item in films if item['category'] == category or item['year'] == year]



@app.post('/films', tags=['Films'])
def create_film(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category:str = Body()):
    films.append({
        "id": id,
		"title": title,
		"overview": overview,
		"year": year,
		"rating": rating,
		"category": category
    })
    return films


@app.put('/films/{id}', tags=['Films'])
def update_film(id: int, title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category:str = Body()):
    for item in films:
        if item['id'] == id:
            item['title'] = title,
            item['overview'] = overview,
            item['year'] = year,
            item['rating'] = rating,
            item['category'] = category
            return films


@app.delete('/films/{id}', tags=['Films'])
def delete_film(id: int):
    for item in films:
        if item['id'] == id:
            films.remove(item)
            return films

