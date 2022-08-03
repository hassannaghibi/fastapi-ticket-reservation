from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.session import get_db
from app.db.crud.hall import (
    get_halls,
    get_hall,
    create_hall,
    delete_hall,
    edit_hall,
)
from app.db.schemas.hall import HallCreate, HallEdit, Hall, HallOut

halls_router = r = APIRouter()


@r.get("/halls", response_model=t.List[Hall], response_model_exclude_none=True,)
async def halls_list(
    response: Response,
    db=Depends(get_db),
):
    """
    Get all halls
    """
    halls = get_halls(db)
    # This is necessary for react-admin to work
    response.headers["Content-Range"] = f"0-9/{len(halls)}"
    return halls


@r.get("/halls/{hall_id}",response_model=Hall,response_model_exclude_none=True,)
async def hall_details(
    request: Request,
    hall_id: int,
    db=Depends(get_db),
):
    """
    Get any hall details
    """
    hall = get_hall(db, hall_id)
    return hall
    # return encoders.jsonable_encoder(
    #     hall, skip_defaults=True, exclude_none=True,
    # )


@r.post("/halls", response_model=Hall, response_model_exclude_none=True)
async def hall_create(
    request: Request,
    hall: HallCreate,
    db=Depends(get_db),
):
    """
    Create a new hall
    """
    return create_hall(db, hall)


@r.put("/halls/{hall_id}", response_model=Hall, response_model_exclude_none=True)
async def hall_edit(
    request: Request,
    hall_id: int,
    hall: HallEdit,
    db=Depends(get_db),
):
    """
    Update existing hall
    """
    return edit_hall(db, hall_id, hall)


@r.delete(
    "/halls/{hall_id}", response_model=Hall, response_model_exclude_none=True
)
async def hall_delete(
    request: Request,
    hall_id: int,
    db=Depends(get_db),
):
    """
    Delete existing hall
    """
    return delete_hall(db, hall_id)
