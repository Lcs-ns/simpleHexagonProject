from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.src.usecases.signup import SignUpUseCase
from app.src.entities.userEntity import User
from app.infrastructure.db.userRepository import UserRepository
from app.infrastructure.db.session import get_db

router = APIRouter()

def get_signup_use_case(db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    return SignUpUseCase(user_repository)

@router.post('/signup')
async def signup(user: User, signup_use_case: SignUpUseCase = Depends(get_signup_use_case)):
    try:
        signup_use_case.execute(user)
        return {"message": "User successfully created"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))