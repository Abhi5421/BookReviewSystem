from fastapi import APIRouter, Depends, status,BackgroundTasks
from api.v1.books.schema import Book, Review,UpdateBook,UpdateReview
from database.connection import get_db
from api.v1.books.utility import *
from sqlalchemy.orm import Session
from utils.common import RaiseError
from utils.logger import create_logger
from fastapi.responses import JSONResponse
from typing import Optional
from utils.common import send_email

router = APIRouter()

logging = create_logger(__name__)


@router.post("/create")
def endpoint_create_book(
        data: Book,
        db: Session = Depends(get_db)
):
    try:
        response = create_book(data, db)
        return response
    except RaiseError as e:
        logging.error(e)
        return JSONResponse(content={'status': 'False', 'detail': e.detail, 'status_code': e.status_code},
                            status_code=e.status_code)
    except Exception as e:
        logging.error(e)
        return JSONResponse(content={'status': 'False', 'detail': str(e)},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.post("/review")
def endpoint_submit_review(
        background_tasks: BackgroundTasks,
        data: Review,
        db: Session = Depends(get_db)
):
    try:
        response = submit_book_reviews(data, db)
        if response:
            background_tasks.add_task(send_email)
            return {"status": True, "detail": "submitted successfully"}
        return {"status": False}
    except RaiseError as e:
        logging.error(e)
        return JSONResponse(content={'status': 'False', 'detail': e.detail, 'status_code': e.status_code},
                            status_code=e.status_code)
    except Exception as e:
        logging.error(e)
        return JSONResponse(content={'status': 'False', 'detail': str(e)},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get("/list")
def endpoint_list_books(
        author: Optional[str] = None,
        published_year: Optional[int] = None,
        db: Session = Depends(get_db)
):
    try:
        response = list_books(author, published_year, db)
        return response
    except RaiseError as e:
        logging.error(e)
        return JSONResponse(content={'status': 'False', 'detail': e.detail, 'status_code': e.status_code},
                            status_code=e.status_code)
    except Exception as e:
        logging.error(e)
        return JSONResponse(content={'status': 'False', 'detail': str(e)},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get("/get-reviews/{book_id}")
def endpoint_list_book_reviews(
        book_id: int,
        db: Session = Depends(get_db)
):
    try:
        response = get_book_reviews(book_id, db)
        return response
    except RaiseError as e:
        logging.error(e)
        return JSONResponse(content={'status': 'False', 'detail': e.detail, 'status_code': e.status_code},
                            status_code=e.status_code)
    except Exception as e:
        logging.error(e)
        return JSONResponse(content={'status': 'False', 'detail': str(e)},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.post("/update/{book_id}")
def endpoint_update_book(
        book_id: int,
        data: UpdateBook,
        db: Session = Depends(get_db)
):
    try:
        response = update_book(book_id,data, db)
        return response
    except RaiseError as e:
        logging.error(e)
        return JSONResponse(content={'status': 'False', 'detail': e.detail, 'status_code': e.status_code},
                            status_code=e.status_code)
    except Exception as e:
        logging.error(e)
        return JSONResponse(content={'status': 'False', 'detail': str(e)},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.post("/update/{review_id}")
def endpoint_update_review(
        review_id: int,
        data: UpdateReview,
        db: Session = Depends(get_db)
):
    try:
        response = update_review(review_id,data, db)
        return response
    except RaiseError as e:
        logging.error(e)
        return JSONResponse(content={'status': 'False', 'detail': e.detail, 'status_code': e.status_code},
                            status_code=e.status_code)
    except Exception as e:
        logging.error(e)
        return JSONResponse(content={'status': 'False', 'detail': str(e)},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.post("/delete/{book_id}")
def endpoint_delete_book(
        book_id: int,
        db: Session = Depends(get_db)
):
    try:
        response = delete_book(book_id, db)
        return response
    except RaiseError as e:
        logging.error(e)
        return JSONResponse(content={'status': 'False', 'detail': e.detail, 'status_code': e.status_code},
                            status_code=e.status_code)
    except Exception as e:
        logging.error(e)
        return JSONResponse(content={'status': 'False', 'detail': str(e)},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.post("/delete/{review_id}")
def endpoint_delete_review(
        review_id: int,
        db: Session = Depends(get_db)
):
    try:
        response = delete_review(review_id, db)
        return response
    except RaiseError as e:
        logging.error(e)
        return JSONResponse(content={'status': 'False', 'detail': e.detail, 'status_code': e.status_code},
                            status_code=e.status_code)
    except Exception as e:
        logging.error(e)
        return JSONResponse(content={'status': 'False', 'detail': str(e)},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
