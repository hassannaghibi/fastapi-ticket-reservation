from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.session import get_db
from app.db.crud.cinema import (
    get_cinemas,
    get_cinema,
    create_cinema,
    delete_cinema,
    edit_cinema,
)
from app.db.schemas.cinema import CinemaCreate, CinemaEdit, Cinema, CinemaOut

cinemas_router = r = APIRouter()


@r.get("/cinemas", response_model=t.List[Cinema], response_model_exclude_none=True,)
async def cinemas_list(
    response: Response,
    db=Depends(get_db),
):
    """
    Get all cinemas
    """
    cinemas = get_cinemas(db)
    # This is necessary for react-admin to work
    response.headers["Content-Range"] = f"0-9/{len(cinemas)}"
    return cinemas


@r.get("/cinemas/{cinema_id}",response_model=Cinema,response_model_exclude_none=True,)
async def cinema_details(
    request: Request,
    cinema_id: int,
    db=Depends(get_db),
):
    """
    Get any cinema details
    """
    cinema = get_cinema(db, cinema_id)
    return cinema
    # return encoders.jsonable_encoder(
    #     cinema, skip_defaults=True, exclude_none=True,
    # )


@r.post("/cinemas", response_model=Cinema, response_model_exclude_none=True)
async def cinema_create(
    request: Request,
    cinema: CinemaCreate,
    db=Depends(get_db),
):
    """
    Create a new cinema
    """
    return create_cinema(db, cinema)


@r.put("/cinemas/{cinema_id}", response_model=Cinema, response_model_exclude_none=True)
async def cinema_edit(
    request: Request,
    cinema_id: int,
    cinema: CinemaEdit,
    db=Depends(get_db),
):
    """
    Update existing cinema
    """
    return edit_cinema(db, cinema_id, cinema)


@r.delete(
    "/cinemas/{cinema_id}", response_model=Cinema, response_model_exclude_none=True
)
async def cinema_delete(
    request: Request,
    cinema_id: int,
    db=Depends(get_db),
):
    """
    Delete existing cinema
    """
    return delete_cinema(db, cinema_id)
