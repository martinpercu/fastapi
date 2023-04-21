from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from utils.jwt_manager import create_token
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.film import film_router
from routers.user import user_router

app = FastAPI()
app.title = "An app with FastAPI"
app.version = "0.1"

app.add_middleware(ErrorHandler)
app.include_router(film_router)
app.include_router(user_router)



Base.metadata.create_all(bind=engine)


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


