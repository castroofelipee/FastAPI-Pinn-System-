from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordBearer

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/login/steps/felipe", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.exception_handler(404)
def not_found_exception_handler(request: Request, exc: HTTPException):
    return not_found_error(request, exc)