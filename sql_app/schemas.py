from datetime import date
from typing import List, Optional

from pydantic import BaseModel


class PartyBase(BaseModel):
    id : int
    name : str
    formeddate : date
    motto : str
    logourl : str
    is_active : bool
    is_coalition : bool
class PartyCreate(PartyBase):
    pass
class Party(PartyBase):
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