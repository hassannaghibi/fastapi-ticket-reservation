from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import typing as t

from db import models
from schemas import book as book_schema


def get_book(db: Session, book_id: int):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="book not found")
    return book