from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.session import get_db
from app.db.crud.movie import (
    get_movies,
    get_movie,
    create_movie,
    delete_movie,
    edit_movie,
)
from app.db.schemas import MovieCreate, MovieEdit, Movie, MovieOut

movies_router = r = APIRouter()


@r.get("/movies", response_model=t.List[Movie], response_model_exclude_none=True,)
async def movies_list(
    response: Response,
    db=Depends(get_db),
):
    """
    Get all movies
    """
    movies = get_movies(db)
    # This is necessary for react-admin to work
    response.headers["Content-Range"] = f"0-9/{len(movies)}"
    return movies


@r.get("/movies/{movie_id}",response_model=Movie,response_model_exclude_none=True,)
async def movie_details(
    request: Request,
    movie_id: int,
    db=Depends(get_db),
):
    """
    Get any movie details
    """
    movie = get_movie(db, movie_id)
    return movie
    # return encoders.jsonable_encoder(
    #     movie, skip_defaults=True, exclude_none=True,
    # )


@r.post("/movies", response_model=Movie, response_model_exclude_none=True)
async def movie_create(
    request: Request,
    movie: MovieCreate,
    db=Depends(get_db),
):
    """
    Create a new movie
    """
    return create_movie(db, movie)


@r.put("/movies/{movie_id}", response_model=Movie, response_model_exclude_none=True)
async def movie_edit(
    request: Request,
    movie_id: int,
    movie: MovieEdit,
    db=Depends(get_db),
):
    """
    Update existing movie
    """
    return edit_movie(db, movie_id, movie)


@r.delete(
    "/movies/{movie_id}", response_model=Movie, response_model_exclude_none=True
)
async def movie_delete(
    request: Request,
    movie_id: int,
    db=Depends(get_db),
):
    """
    Delete existing movie
    """
    return delete_movie(db, movie_id)
