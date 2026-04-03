from jose import jwt,JWTError
from passlib.context import CryptContext
from datetime import datetime,timedelta
from app.core.config import settings

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

pwd_context = CryptContext(schemes=['bcrypt'],deprecated='auto')


def hash_password(password:str):
    return pwd_context.hash(password)


def verify_password(plain,hashed):
    return pwd_context.verify(plain,hashed)


def create_access_token(data: dict):
    to_encode = data.copy()
    
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt