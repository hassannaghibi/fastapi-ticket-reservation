from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import typing as t

from app.db.models import Showing 
from app.db.schemas import showing as showing_schema


def get_showing(db: Session, showing_id: int):
    showing = db.query(Showing).filter(Showing.id == showing_id).first()
    if not showing:
        raise HTTPException(status_code=404, detail="showing not found")
    return showing


def get_showings(
    db: Session, skip: int = 0, limit: int = 100
) -> t.List[showing_schema.ShowingOut]:
    return db.query(Showing).offset(skip).limit(limit).all()


def create_showing(db: Session, showing: showing_schema.ShowingCreate):
    db_showing = Showing(
        title = showing.title,
        start = showing.start,
        end = showing.end,
        hall_id = showing.hall_id,
        movie_id = showing.movie_id,
        is_active = showing.is_active,
    )
    db.add(db_showing)
    db.commit()
    db.refresh(db_showing)
    return db_showing


def delete_showing(db: Session, showing_id: int):
    showing = get_showing(db, showing_id)
    if not showing:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="showing not found")
    db.delete(showing)
    db.commit()
    return showing


def edit_showing(
    db: Session, showing_id: int, showing: showing_schema.ShowingEdit
) -> showing_schema.Showing:
    db_showing = get_showing(db, showing_id)
    if not db_showing:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="showing not found")
    update_data = showing.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_showing, key, value)

    db.add(db_showing)
    db.commit()
    db.refresh(db_showing)
    return db_showing
