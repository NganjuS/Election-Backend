from decimal import Decimal
from turtle import position
from typing_extensions import Required
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, DECIMAL, DateTime
from sqlalchemy.orm import relationship, backref
from datetime import datetime
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
    won = Column(Boolean, default=False)
    slogan = Column(String)
    color = Column(String)
    position_id = Column(Integer, ForeignKey("positions.id"))
    party_id = Column(Integer, ForeignKey("parties.id"))
    county_id = Column(Integer, ForeignKey("counties.id"), nullable=True)
    deputy_id = Column(Integer, ForeignKey("candidates.id"), nullable=True)

    party = relationship("Party", back_populates="candidates")
    position = relationship("Position", back_populates="candidt")
    county = relationship("County", back_populates="candidate")
    deputy  = relationship("Candidate", remote_side=[id])
    statsdtcan = relationship("StatsData", back_populates="datacandidate")  

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
class County(Base):
    __tablename__ = "counties"
    id = Column(Integer, primary_key=True, autoincrement=True)
    code =  Column(String, unique=True, index=True)
    name =  Column(String, unique=True, index=True)
    candidate = relationship("Candidate", back_populates="county")
##keep a list of all statistics source
class StatsSource(Base):
    __tablename__ = "statsources"
    id = Column(Integer, primary_key=True, autoincrement=True)
    code =  Column(String, unique=True, index=True)
    name =  Column(String, unique=True, index=True)
    statsdata = relationship("StatsData", back_populates="statssource")

class StatsData(Base):
    __tablename__ = "statsdata"
    id = Column(Integer, primary_key=True, autoincrement=True)
    candidate_id = Column(Integer, ForeignKey("candidates.id"))
    statsbatch_id = Column(Integer, ForeignKey("statsbatch.id"))
    batchname =  Column(String, unique=True, index=True)
    batchdate = Column(DateTime,  default=datetime.now)
    votes = Column(DECIMAL)
    datacandidate = relationship("Candidate", back_populates="statsdtcan")
    statssource_id = Column(Integer, ForeignKey("statsources.id"))
    statssource = relationship("StatsSource", back_populates="statsdata")

class DefaultsData(Base):
    __tablename__ = "defaultsdata"
    id = Column(Integer, primary_key=True, autoincrement=True)
    totalvotes = Column(DECIMAL)
    electiondate = Column(DateTime)

class StatsBatch(Base):
    __tablename__ = "statsbatch"
    id = Column(Integer, primary_key=True, autoincrement=True)
    batchname =  Column(String, unique=True, index=True)
    batchdate = Column(Date,  default=datetime.now)
    






