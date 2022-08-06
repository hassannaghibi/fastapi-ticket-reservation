from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import typing as t

from app.db.models import Hall
from app.db.schemas import hall as hall_schema


def get_hall(db: Session, hall_id: int):
    hall = db.query(Hall).filter(Hall.id == hall_id).first()
    if not hall:
        raise HTTPException(status_code=404, detail="hall not found")
    return hall


def get_halls(
    db: Session, skip: int = 0, limit: int = 100
) -> t.List[hall_schema.HallOut]:
    return db.query(Hall).offset(skip).limit(limit).all()


def create_hall(db: Session, hall: hall_schema.HallCreate):
    db_hall = Hall(
        name = hall.name,
        description = hall.description,
        cinema_id = hall.cinema_id,
        is_active = hall.is_active,
    )
    db.add(db_hall)
    db.commit()
    db.refresh(db_hall)
    return db_hall


def delete_hall(db: Session, hall_id: int):
    hall = get_hall(db, hall_id)
    if not hall:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="hall not found")
    db.delete(hall)
    db.commit()
    return hall


def edit_hall(
    db: Session, hall_id: int, hall: hall_schema.HallEdit
) -> hall_schema.Hall:
    db_hall = get_hall(db, hall_id)
    if not db_hall:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="hall not found")
    update_data = hall.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_hall, key, value)

    db.add(db_hall)
    db.commit()
    db.refresh(db_hall)
    return db_hall
