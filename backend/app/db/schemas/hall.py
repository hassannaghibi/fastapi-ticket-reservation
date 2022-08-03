from typing import Union
from pydantic import BaseModel
from .seat import Seat 
from .showing import Showing 
import typing as t


class HallBase(BaseModel):
    name: str
    description: Union[str, None] = None
    
    class Config:
        orm_mode = True

class HallOut(HallBase):
    pass

class HallCreate(HallBase):
    pass

class HallEdit(HallBase):
    name: t.Optional[str] = None
    description: t.Optional[str] = None

    class Config:
        orm_mode = True

class Hall(HallBase):
    id: int
    is_active: bool
    seats: t.List[Seat] = None
    showings: t.List[Showing] = None
    
    class Config:
        orm_mode = True