from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.session import get_db
from app.db.crud.book import (
    get_books,
    get_book,
)
from app.db.schemas import Book

books_router = r = APIRouter()


@r.get("/books", response_model=t.List[Book], response_model_exclude_none=True,)
async def books_list(
    response: Response,
    db=Depends(get_db),
):
    """
    Get all books
    """
    books = get_books(db)
    # This is necessary for react-admin to work
    response.headers["Content-Range"] = f"0-9/{len(books)}"
    return books


@r.get("/books/{book_id}",response_model=Book,response_model_exclude_none=True,)
async def book_details(
    request: Request,
    book_id: int,
    db=Depends(get_db),
):
    """
    Get any book details
    """
    book = get_book(db, book_id)
    return book
    # return encoders.jsonable_encoder(
    #     book, skip_defaults=True, exclude_none=True,
    # )
