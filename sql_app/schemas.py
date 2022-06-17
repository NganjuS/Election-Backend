from __future__ import annotations
from datetime import date, datetime
from dis import show_code
from typing import List, Optional,Union
from unicodedata import decimal


from pydantic import BaseModel

class PartyBase(BaseModel):
    name : str
    short_code : str
    party_code : str
    formeddate : Union[date, None] = None
    motto : Union[str, None] = None
    slogan : Union[str, None] = None
    logourl : Union[str, None] = None
    symbol : Union[str, None] = None
    colors : Union[str, None] = None
    postaladdress : Union[str, None] = None
    officelocation : Union[str, None] = None
    is_active : bool
    is_coalition : bool
class PartyCreate(PartyBase):
    pass
class Party(PartyBase):
    id : int
    class Config:
        orm_mode = True
class CountyBase(BaseModel):
    code : str
    name : str
class CountyCreate(CountyBase):
    pass

class County(CountyBase):
    id : int
    class Config:
        orm_mode = True
class PositionBase(BaseModel):
    name : str

class PositionCreate(PositionBase):
    pass
class Position(PositionBase):
    id : int
    class Config:
        orm_mode = True
class CandidateBase(BaseModel):
    fullnames : Union[str, None]
    short_code : Union[str, None]
    age  : Union[int, None]
    weight : Union[int, None]
    dateofbirth : Union[date, None]
    imageurl : Union[str, None]
    is_active : Union[bool, None]
    slogan : Union[str, None] = None
    color : Union[str, None] = None
    position_id : Union[int, None]
    party_id : Union[int, None]
    county_id : Union[int, None] = None
    deputy_id : Union[int, None] = None
class CandidateCreate(CandidateBase):
    pass
class CandidateUpdate(CandidateBase):
    id : int = None
    class Config:
        orm_mode = True
class Candidate(CandidateBase):
    id : int = None
    position : Position = None
    party : Party = None
    county : County = None
    deputy : Union[Candidate, None] = None
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username : str

class UserLogin(UserBase):
    password : str

class UserCreate(UserBase):
    password : str

class User(UserBase):
    id : int
    class Config:
        orm_mode = True
class SessionBase(BaseModel):
    userid : User
    sessiontoken : str

class SessionCreate(SessionBase):
    pass
class Session(SessionBase):
    id : int
    class Config:
        orm_mode = True

class DefaultsDataBase(BaseModel):
    totalvotes : float
    electiondate : date

class DefaultsDataCreate(DefaultsDataBase):
    pass
class DefaultsDataUpdate(DefaultsDataBase):
    id : int
    class Config:
        orm_mode = True
class DefaultsData(DefaultsDataBase):
    id : int
    class Config:
        orm_mode = True



