#models.py

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship      #.ORM!!

from database import Base   #van de database.py file import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  #index=true zorgt ervoor dat hij alles indexeert d.w.z: inserten duurt langer MAAR wanneer je data opvraagt gaat rapper
    email = Column(String, unique=True, index=True)  #unieke waarde     met "String(64)" kan je definieren dat de string max 64 lang is
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)  #default value is True

    items = relationship("Item", back_populates="owner")  #voor tabellen te koppelen zoals in Mysql


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))     #Item behoort tot een user

    owner = relationship("User", back_populates="items")   #voor tabellen te koppelen zoals in Mysql
