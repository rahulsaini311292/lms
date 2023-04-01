from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import session
from lms.p_models import book_p_model
from lms.schema import book_models
from lms.lib.database import get_db

book_router = APIRouter()


@book_router.get("/book")
def get(db: session = Depends(get_db)):
    # return all books
    return db.query(book_models.Book).all()


@book_router.post("/book")
def post(book: book_p_model.BookPModel, db: session = Depends(get_db)):
    book_obj = book_models.Book()
    book_obj.book_name = book.book_name

    db.add(book_obj)
    db.commit()
    return book
