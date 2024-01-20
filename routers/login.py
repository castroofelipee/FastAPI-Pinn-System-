# routers/login.py

from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
async def login_info():
    return None

@router.post("/register")
async def register_user(username: str = Form(...), email: str = Form(...), password: str = Form(...)):
    return {"message": "User registered successfully"}

