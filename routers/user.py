from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token
from schemas.user import User


user_router = APIRouter()



@user_router.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "admin@admin.com" and user.password == "Admin123456":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)
    return JSONResponse(status_code=404, content="PAS DE USER")


