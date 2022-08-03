from pydantic import BaseModel
from datetime import datetime
from .book import Book 
import typing as t


class ShowingBase(BaseModel):
    title: str
    start: datetime
    end: datetime
    
    class Config:
        orm_mode = True

class MovieShowingOut(ShowingBase):
    pass

class ShowingCreate(ShowingBase):
    pass

class ShowingEdit(ShowingBase):
    number: t.Optional[int] = None

    class Config:
        orm_mode = True

class Showing(ShowingBase):
    id: int
    hall_id: int
    movie_id: int
    is_active: bool
    books: t.List[Book] = None
    
    class Config:
        orm_mode = True