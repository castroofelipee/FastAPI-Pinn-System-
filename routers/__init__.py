from fastapi import APIRouter
from . import auth, user, home

api_router = APIRouter()

api_router.include_router(auth.router, tags=["auth"], prefix="/auth")
api_router.include_router(user.router, tags=["user"], prefix="/user")
api_router.include_router(home.router, tags=["home"])
