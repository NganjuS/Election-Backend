from decimal import Decimal
from turtle import position
from typing_extensions import Required
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .database import Base


class Party(Base):
    __tablename__ = "parties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    short_code = Column(String, unique=True, index=True)
    party_code = Column(String, unique=True, index=True)
    formeddate = Column(Date)
    motto = Column(String)
    slogan = Column(String)
    logourl = Column(String)
    symbol = Column(String)
    colors = Column(String)
    postaladdress = Column(String)
    officelocation = Column(String)
    is_active = Column(Boolean, default=True)
    is_coalition = Column(Boolean, default=True)
    candidates = relationship("Candidate", back_populates="party")


class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    fullnames = Column(String, unique=True, index=True)
    short_code = Column(String, unique=True, index=True)
    age = Column(Integer)
    weight = Column(Integer) ## orders the candidates based on popularity
    dateofbirth = Column(Date)
    imageurl = Column(String) 
    is_active = Column(Boolean, default=True)
    position_id = Column(Integer, ForeignKey("positions.id"))
    party_id = Column(Integer, ForeignKey("parties.id"))

    party = relationship("Party", back_populates="candidates")
    position = relationship("Position", back_populates="candidt")

class Position(Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, index=True) 
    candidt = relationship("Candidate", back_populates="position")
    
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, index=True) 
    password = Column(String) 
    email = Column(String) 
    active = Column(Boolean, default=True)
    sessions = relationship("Sessions")
class Sessions(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    userid = Column(Integer, ForeignKey('user.id'))
    sessiontoken =  Column(String)