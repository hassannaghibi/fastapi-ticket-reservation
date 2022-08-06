from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import typing as t

from app.db.models import Seat
from app.db.schemas import seat as seat_schema


def get_seat(db: Session, seat_id: int):
    seat = db.query(Seat).filter(Seat.id == seat_id).first()
    if not seat:
        raise HTTPException(status_code=404, detail="seat not found")
    return seat


def get_seats(
    db: Session, skip: int = 0, limit: int = 100
) -> t.List[seat_schema.SeatOut]:
    return db.query(Seat).offset(skip).limit(limit).all()


def create_seat(db: Session, seat: seat_schema.SeatCreate):
    db_seat = Seat(
        number = seat.number,
        hall_id = seat.hall_id,
        is_active = seat.is_active,
    )
    db.add(db_seat)
    db.commit()
    db.refresh(db_seat)
    return db_seat


def delete_seat(db: Session, seat_id: int):
    seat = get_seat(db, seat_id)
    if not seat:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="seat not found")
    db.delete(seat)
    db.commit()
    return seat


def edit_seat(
    db: Session, seat_id: int, seat: seat_schema.SeatEdit
) -> seat_schema.Seat:
    db_seat = get_seat(db, seat_id)
    if not db_seat:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="seat not found")
    update_data = seat.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_seat, key, value)

    db.add(db_seat)
    db.commit()
    db.refresh(db_seat)
    return db_seat
