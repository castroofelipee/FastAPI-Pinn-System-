from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordBearer

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

# Inclua a lógica de autenticação aqui

@router.get("/home/comprar", response_class=HTMLResponse)
async def home():
    return templates.TemplateResponse("index.html", {"request": request})
