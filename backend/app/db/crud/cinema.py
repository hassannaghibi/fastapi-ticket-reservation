from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import typing as t

from app.db.models import Cinema
from app.db.schemas import cinema as cinema_schema


def get_cinema(db: Session, cinema_id: int):
    cinema = db.query(Cinema).filter(Cinema.id == cinema_id).first()
    if not cinema:
        raise HTTPException(status_code=404, detail="cinema not found")
    return cinema


def get_cinemas(
    db: Session, skip: int = 0, limit: int = 100
) -> t.List[cinema_schema.CinemaOut]:
    return db.query(Cinema).offset(skip).limit(limit).all()


def create_cinema(db: Session, cinema: cinema_schema.CinemaCreate):
    db_cinema = Cinema(
        name = cinema.name,
        description = cinema.description,
        is_active = cinema.is_active,
    )
    db.add(db_cinema)
    db.commit()
    db.refresh(db_cinema)
    return db_cinema


def delete_cinema(db: Session, cinema_id: int):
    cinema = get_cinema(db, cinema_id)
    if not cinema:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="cinema not found")
    db.delete(cinema)
    db.commit()
    return cinema


def edit_cinema(
    db: Session, cinema_id: int, cinema: cinema_schema.CinemaEdit
) -> cinema_schema.Cinema:
    db_cinema = get_cinema(db, cinema_id)
    if not db_cinema:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="cinema not found")
    update_data = cinema.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_cinema, key, value)

    db.add(db_cinema)
    db.commit()
    db.refresh(db_cinema)
    return db_cinema
