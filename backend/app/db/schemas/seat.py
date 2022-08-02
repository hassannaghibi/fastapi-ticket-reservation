from pydantic import BaseModel
from book import Book 
import typing as t


class SeatBase(BaseModel):
    number: int
    
    class Config:
        orm_mode = True

class SeatOut(SeatBase):
    pass

class SeatCreate(SeatBase):
    pass

class SeatEdit(SeatBase):
    number: t.Optional[int] = None

    class Config:
        orm_mode = True

class Seat(SeatBase):
    id: int
    hall_id: int
    is_active: bool
    books: list[Book] = []
    
    class Config:
        orm_mode = True