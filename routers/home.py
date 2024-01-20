from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from ..crud import oauth2_scheme

router = APIRouter()

@router.get("/home/comprar")
async def home_comprar(request: HTMLResponse, token: str = Depends(oauth2_scheme)):
    return {"message": "Compra realizada com sucesso!"}
