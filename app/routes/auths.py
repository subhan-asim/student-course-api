from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.models_auth import UserLogin, UserRegister, Token
from app.auth_utils import verify_password, hash_password, create_token, verify_token
from app.crud import register_user
from app.db import get_connection
import sqlite3

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
router = APIRouter(prefix="/auth", tags=["Auth"])

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=201, detail="Invalid Token.")
    return payload

@router.post("/register")
def user_register(user: UserRegister):
    hashed_pw = hash_password(user.password)
    _ = register_user(user.username, hashed_pw)
    if _ == True:
        return {"message": "User added successfully."}
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User Already Exists.")

@router.post("/login", response_model=Token)
def login(user: OAuth2PasswordRequestForm = Depends()):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (user.username,))
    db_user = c.fetchone()
    print(db_user)
    if not db_user or not verify_password(user.password, db_user[2]):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    token = create_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}


@router.get("/me")
def user_info(user= Depends(get_current_user)):
    return {"user": user}




