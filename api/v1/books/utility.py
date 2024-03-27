from sqlalchemy.orm import Session
from api.v1.books import model
from sqlalchemy import and_
from utils.common import RaiseError


def create_book(data, db: Session):
    db_data = model.Book(**data.dict())
    db.add(db_data)
    db.commit()
    return {"status": True, "detail": "created successfully"}


def submit_book_reviews(data, db: Session):
    book_data = db.query(model.Book).filter(model.Book.id == data.book_id).first()
    if not book_data:
        raise RaiseError(error="Book not found", statuscode=200)
    db_data = model.Review(**data.dict())
    db.add(db_data)
    db.commit()
    return {"status": True, "detail": "submitted successfully"}


def list_books(author, year, db: Session):
    query = db.query(model.Book)

    filters = []
    if author:
        filters.append(model.Book.author == author)
    if year:
        filters.append(model.Book.publication_year == year)

    if filters:
        query = query.filter(and_(*filters))

    data = query.all()
    return data


def get_book_reviews(book_id, db: Session):
    book_data = db.query(model.Review).filter(model.Book.id == book_id).all()
    return book_data


def update_book(book_id, data,db: Session):
    book_data = db.query(model.Book).filter(model.Book.id == book_id).first()
    if not book_data:
        raise RaiseError(error="Book not found", statuscode=200)
    data_dict = data.__dict__
    for key, value in data_dict.items():
        setattr(book_data, key, value)
    db.commit()
    return {"status": True, "detail": "updated successfully"}


def update_review(review_id,data, db: Session):
    review_data = db.query(model.Review).filter(model.Review.id == review_id).first()
    if not review_data:
        raise RaiseError(error="Book not found", statuscode=200)
    data_dict = data.__dict__
    for key, value in data_dict.items():
        setattr(review_data, key, value)
    db.commit()
    return {"status": True, "detail": "updated successfully"}


def delete_book(book_id, db: Session):
    book_data = db.query(model.Book).filter(model.Book.id == book_id).first()
    if not book_data:
        raise RaiseError(error="Book not found", statuscode=200)
    db.delete(book_data)
    db.commit()
    return {"status": True, "detail": "deleted successfully"}


def delete_review(review_id, db: Session):
    review_data = db.query(model.Review).filter(model.Review.id == review_id).first()
    if not review_data:
        raise RaiseError(error="Book not found", statuscode=200)
    db.delete(review_data)
    db.commit()
    return {"status": True, "detail": "deleted successfully"}
