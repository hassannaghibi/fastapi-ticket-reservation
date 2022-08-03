from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import typing as t

from db import models
from db.schemas import book as book_schema


def get_book(db: Session, book_id: int):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="book not found")
    return book

def get_books(
    db: Session, skip: int = 0, limit: int = 100
) -> t.List[book_schema.BookOut]:
    return db.query(models.Book).offset(skip).limit(limit).all()
