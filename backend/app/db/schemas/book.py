from pydantic import BaseModel



class BookBase(BaseModel):
    pass
            
class BookOut(BookBase):
    pass

class Book(BookBase):
    id: int
    seat_id: int
    user_id: int
    showing_id: bool
    
    class Config:
        orm_mode = True