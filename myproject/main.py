#main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

#alle andere .py bestanden inladen (importeren)
import crud
import schemas
import models
from database import SessionLocal, engine

import os    #Nodig om de map aan te maken --> SQLALCHEMY_DATABASE_URL = "sqlite:/// -->  ./sqlitedb/ <--   sqlitedata.db"

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')


models.Base.metadata.create_all(bind=engine)   # start de database op en pakt de data van models en create daar onze entiteiten uit

app = FastAPI()

def get_db():
    db = SessionLocal()    #Hier maak je de db aan die je overal in crud gebruikt
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:         #is db_user null of is dit iets (opgevuld) zoja: ...
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip, limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item, user_id=user_id)

@app.get("/items/", response_model=list[schemas.Item])
def read_item(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip, limit)
    return items
