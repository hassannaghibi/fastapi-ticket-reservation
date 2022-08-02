from typing import Union
from pydantic import BaseModel
from hall import Hall 

import typing as t

class CinemaBase(BaseModel):
    name: str
    description: Union[str, None] = None
    
    class Config:
        orm_mode = True

class CinemaOut(CinemaBase):
    pass


class CinemaCreate(CinemaBase):
    pass

class CinemaEdit(CinemaBase):
    name: t.Optional[str] = None
    description: t.Optional[str] = None

    class Config:
        orm_mode = True

class Cinema(CinemaBase):
    id: int
    user_id: int
    : bool
    halls: list[Hall] = []
    
    class Config:
        orm_mode = True