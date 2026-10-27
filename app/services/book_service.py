from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.book import Book
from app.schemas.book import BookCreate

def create_book(db: Session, data: BookCreate) -> Book:
    book = Book(**data.model_dump())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def list_books(db: Session) -> list[Book]:
    return list(db.scalars(select(Book)))

def get_book(db: Session, book_id: int) -> Book | None:
    return db.get(Book, book_id)

def update_book(db: Session, book_id: int, data: BookCreate) -> Book | None:
    book = db.get(Book, book_id)
    if book is None:
        return None
    for field, value in data.model_dump().items():
        setattr(book, field, value)
    db.commit()
    db.refresh(book)
    return book

def delete_book(db: Session, book_id: int) -> bool:
    book = db.get(Book, book_id)
    if book is None:
        return False
    db.delete(book)
    db.commit()
    return True