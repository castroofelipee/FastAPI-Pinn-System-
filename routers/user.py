from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from ..crud import get_db, create_user

router = APIRouter()

@router.post("/register")
async def register(username: str, password: str, db: Session = Depends(get_db)):
    user = get_user(db, username=username)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )
    return create_user(db, username=username, password=password)
