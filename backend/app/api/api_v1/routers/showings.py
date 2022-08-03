from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.session import get_db
from app.db.crud.showing import (
    get_showings,
    get_showing,
    create_showing,
    delete_showing,
    edit_showing,
)
from app.db.schemas.showing import ShowingCreate, ShowingEdit, Showing, ShowingOut

showings_router = r = APIRouter()


@r.get("/showings", response_model=t.List[Showing], response_model_exclude_none=True,)
async def showings_list(
    response: Response,
    db=Depends(get_db),
):
    """
    Get all showings
    """
    showings = get_showings(db)
    # This is necessary for react-admin to work
    response.headers["Content-Range"] = f"0-9/{len(showings)}"
    return showings


@r.get("/showings/{showing_id}",response_model=Showing,response_model_exclude_none=True,)
async def showing_details(
    request: Request,
    showing_id: int,
    db=Depends(get_db),
):
    """
    Get any showing details
    """
    showing = get_showing(db, showing_id)
    return showing
    # return encoders.jsonable_encoder(
    #     showing, skip_defaults=True, exclude_none=True,
    # )


@r.post("/showings", response_model=Showing, response_model_exclude_none=True)
async def showing_create(
    request: Request,
    showing: ShowingCreate,
    db=Depends(get_db),
):
    """
    Create a new showing
    """
    return create_showing(db, showing)


@r.put("/showings/{showing_id}", response_model=Showing, response_model_exclude_none=True)
async def showing_edit(
    request: Request,
    showing_id: int,
    showing: ShowingEdit,
    db=Depends(get_db),
):
    """
    Update existing showing
    """
    return edit_showing(db, showing_id, showing)


@r.delete(
    "/showings/{showing_id}", response_model=Showing, response_model_exclude_none=True
)
async def showing_delete(
    request: Request,
    showing_id: int,
    db=Depends(get_db),
):
    """
    Delete existing showing
    """
    return delete_showing(db, showing_id)
