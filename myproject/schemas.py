#schemas.py

from pydantic import BaseModel

class ItemBase(BaseModel):   #dingen die bij een post of get moet bijzijn
    title: str
    description: str | None=None   # | None=None wil zeggen dat dit optioneel is

class ItemCreate(ItemBase):  #bij creeren wat moet er bij komen bij het maken? zelfde als hierboven dus pass
    pass

class Item(ItemBase):   # Dingen van de itemBAse + dit krijgen we terug bij een Get request
    id: int
    owner_id: int

    class Config:           # Om de orm mode op te zetten
        orm_mode = True

class UserBase(BaseModel): # passwoord willen we niet uitlezen
    email: str

class UserCreate(UserBase): # hier willen we bij het aanmaken ook een password meegeven
    password: str

class User(UserBase):   # dit + UserBase krijgen we terug bij een GET
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode: True

