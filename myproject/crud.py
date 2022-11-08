#crud.py

from sqlalchemy.orm import Session

import models
import schemas

def get_user(db: Session, user_id: int):   # user zoeken op ID
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email:str):  # User zoeken op email
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):     #get ALL users, skip: De hoeveel eerste users wil je skippen?
    return db.query(models.User).offset(skip).limit(limit).all()     # limit= hoeveel wil je er max nemen

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "Notreallyyapassword"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)  # "user" is de var die je bij de def meegeeft
    db.add(db_user)
    db.commit()
    db.refresh(db_user)      #refreshed het object met de nieuwe waardes
    return db_user



def get_items(db: Session, skip: int = 0, limit: int = 100):     #get ALL Items, skip: De hoeveel eerste users wil je skippen?
    return db.query(models.Item).offset(skip).limit(limit).all()     # limit= hoeveel wil je er max nemen

def create_item(db: Session, item: schemas.ItemCreate, user_id: int):    #We geven hier ook een user_id mee omdat een item aan een user toebehoort
    db_item = models.Item(**item.dict(), owner_id=user_id)     #google: "The ** operator allows us to take a dictionary of key-value pairs and unpack it into keyword arguments in a function call"
    db.add(db_item)
    db.commit()
    db.refresh(db_item)      #refreshed het object met de nieuwe waardes
    return db_item