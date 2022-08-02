from pydantic import BaseModel


class Book(BaseModel):
    id: int
    seat_id: int
    user_id: int
    showing_id: bool
    
    class Config:
        orm_mode = True