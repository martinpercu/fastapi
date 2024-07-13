from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()
app.title = "An app with FastAPI"
app.version = "0.1"

films = [
    {
        "id": 1,
		"title": "Avatar",
		"overview": "Un human va a la planete pandora ou tous sont bleus ....",
		"year": "2012",
		"rating": 7.8,
		"category": "Action"
    },
    {
        "id": 2,
		"title": "Avatar 2",
		"overview": "Un human va a la planete pandora ou tous sont bleus ....",
		"year": "2019",
		"rating": 7.2,
		"category": "Action"
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




