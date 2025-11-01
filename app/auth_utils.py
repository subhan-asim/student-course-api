from passlib.context import CryptContext
from jose import JWTError, jwt
import datetime


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "c3f9caa7e8247f0e6e7f95a2466b91e479c4c2b3a6615eaf3b7dbe90dbb273d2"
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 30

def hash_password(plain_password: str) -> str:
    return pwd_context.hash(plain_password)

def verify_password(plain_password:str, hashed_password:str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return payload
    except JWTError:
        return None




