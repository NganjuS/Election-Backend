from datetime import datetime, timedelta
from typing import Union, List

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from sql_app import crud, models, schemas
from sqlalchemy.orm import Session
from sql_app.database import SessionLocal, engine
import uvicorn
# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "cfd4cf823c32453770673729540f61ee70ccb940474ea7c1e455bfd52a6fe292"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(username: str, db : Session):
    user = crud.get_db_user(db, username)
    if user:
        return user


def authenticate_user( username: str, password: str, db : Session):
    user = get_user(username, db)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username, db=next(get_db()))
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: schemas.User = Depends(get_current_user)):
    if not current_user.active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),db : Session=Depends(get_db)):
    user = authenticate_user( form_data.username, form_data.password, db=db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(get_current_active_user)):
    return current_user
@app.get("/hashedpassword", response_model=str)
async def get_hashed_password(password : str):
    return get_password_hash(password=password)

@app.get("/verifypassword", response_model=str)
async def confirm_hashed_password(password : str, hashedpassword : str):
    if verify_password(password, hashedpassword):
        return "Found"
    return "Not Found"
@app.post("/user/add", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db,user)  
@app.post("/candidate/add", response_model=schemas.Candidate)
async def create_candidate(candidate: schemas.CandidateCreate, db: Session = Depends(get_db)):
    return crud.create_candidate(db,candidate)  
@app.get("/getcandidates", response_model=List[schemas.Candidate])
async def get_candidates(db: Session = Depends(get_db)):
    return crud.get_db_candidates(db)
@app.get("/positions/", response_model=List[schemas.Position])
def read_positions(db: Session = Depends(get_db)):
    return crud.get_position(db) 
@app.post("/position/add/", response_model=schemas.Position)
def create_position(position: schemas.PositionCreate, db: Session = Depends(get_db)):
    return crud.create_position(db=db, posi=position)  
@app.get("/parties/", response_model=List[schemas.Party])
def read_parties(db: Session = Depends(get_db)):
    return crud.get_db_parties(db) 
@app.post("/party/add/", response_model=schemas.Party)
def create_party(party: schemas.PartyCreate, db: Session = Depends(get_db)):
    return crud.create_party(db, party)  
@app.post("/party/addmany/", response_model=List[schemas.Position])
def create_many_parties(parties: List[schemas.PartyCreate], db: Session = Depends(get_db)):
    return crud.create_parties(db, parties)
##@app.get("/users/me/items/")
##async def read_own_items(current_user: User = Depends(get_current_active_user)):
 ##   return [{"item_id": "Foo", "owner": current_user.username
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)