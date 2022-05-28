from datetime import date
from dis import show_code
from typing import List, Optional,Union

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

class PositionBase(BaseModel):
    name : str

class PositionCreate(PositionBase):
    pass
class Position(PositionBase):
    id : int
    class Config:
        orm_mode = True
class CandidateBase(BaseModel):
    fullnames : str
    short_code : str
    age  : int
    weight : int
    dateofbirth : date
    imageurl : str
    is_active : bool
    position_id : int
    party_id : int
class CandidateCreate(CandidateBase):
    pass
class Candidate(CandidateBase):
    id : int
    position : Position
    party : Party
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

