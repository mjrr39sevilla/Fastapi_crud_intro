from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database.database_connection import get_db
from app.schemas.book import BookCreate, BookOut
from app.services import book_service

router = APIRouter()

@router.post("/", response_model=BookOut, status_code=201)
def create(data: BookCreate, db: Session = Depends(get_db)):
    return book_service.create_book(db, data)

@router.get("/", response_model=list[BookOut])
def list_all(db: Session = Depends(get_db)):
    return book_service.list_books(db)

@router.get("/{book_id}", response_model=BookOut)
def get_one(book_id: int, db: Session = Depends(get_db)):
    book = book_service.get_book(db, book_id)
    if book is None:
        raise HTTPException(404, "Book not found")
    return book

@router.put("/{book_id}", response_model=BookOut)
def update(book_id: int, data: BookCreate, db: Session = Depends(get_db)):
    book = book_service.update_book(db, book_id, data)
    if book is None:
        raise HTTPException(404, "Book not found")
    return book

@router.delete("/{book_id}", status_code=204)
def delete(book_id: int, db: Session = Depends(get_db)):
    if not book_service.delete_book(db, book_id):
        raise HTTPException(404, "Book not found")