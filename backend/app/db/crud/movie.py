from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import typing as t

from app.db.models import Movie
from app.db.schemas import movie as movie_schema


def get_movie(db: Session, movie_id: int):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="movie not found")
    return movie


def get_movies(
    db: Session, skip: int = 0, limit: int = 100
) -> t.List[movie_schema.MovieOut]:
    return db.query(Movie).offset(skip).limit(limit).all()


def create_movie(db: Session, movie: movie_schema.MovieCreate):
    db_movie = Movie(
        title = movie.title,
        description = movie.description,
        is_active = movie.is_active,
    )
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def delete_movie(db: Session, movie_id: int):
    movie = get_movie(db, movie_id)
    if not movie:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="movie not found")
    db.delete(movie)
    db.commit()
    return movie


def edit_movie(
    db: Session, movie_id: int, movie: movie_schema.MovieEdit
) -> movie_schema.Movie:
    db_movie = get_movie(db, movie_id)
    if not db_movie:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="movie not found")
    update_data = movie.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_movie, key, value)

    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie
