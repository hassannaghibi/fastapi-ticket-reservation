from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.session import get_db
from app.db.crud.seat import (
    get_seats,
    get_seat,
    create_seat,
    delete_seat,
    edit_seat,
)
from app.db.schemas.seat import SeatCreate, SeatEdit, Seat, SeatOut

seats_router = r = APIRouter()


@r.get("/seats", response_model=t.List[Seat], response_model_exclude_none=True,)
async def seats_list(
    response: Response,
    db=Depends(get_db),
):
    """
    Get all seats
    """
    seats = get_seats(db)
    # This is necessary for react-admin to work
    response.headers["Content-Range"] = f"0-9/{len(seats)}"
    return seats


@r.get("/seats/{seat_id}",response_model=Seat,response_model_exclude_none=True,)
async def seat_details(
    request: Request,
    seat_id: int,
    db=Depends(get_db),
):
    """
    Get any seat details
    """
    seat = get_seat(db, seat_id)
    return seat
    # return encoders.jsonable_encoder(
    #     seat, skip_defaults=True, exclude_none=True,
    # )


@r.post("/seats", response_model=Seat, response_model_exclude_none=True)
async def seat_create(
    request: Request,
    seat: SeatCreate,
    db=Depends(get_db),
):
    """
    Create a new seat
    """
    return create_seat(db, seat)


@r.put("/seats/{seat_id}", response_model=Seat, response_model_exclude_none=True)
async def seat_edit(
    request: Request,
    seat_id: int,
    seat: SeatEdit,
    db=Depends(get_db),
):
    """
    Update existing seat
    """
    return edit_seat(db, seat_id, seat)


@r.delete(
    "/seats/{seat_id}", response_model=Seat, response_model_exclude_none=True
)
async def seat_delete(
    request: Request,
    seat_id: int,
    db=Depends(get_db),
):
    """
    Delete existing seat
    """
    return delete_seat(db, seat_id)
