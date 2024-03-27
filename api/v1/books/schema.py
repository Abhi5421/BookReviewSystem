from pydantic import BaseModel, ConfigDict,model_validator
from typing import Optional,Any


class Book(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    title: str
    author: str
    publication_year: int


class UpdateBook(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    title: Optional[str] = None
    author: Optional[str] = None
    publication_year: Optional[int] = None


class Review(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    book_id: int
    rating: int
    comment: str

    @model_validator(mode="before")
    @classmethod
    def check_input_data(cls, data: Any) -> Any:
        if data['rating'] < 1 or data['rating'] > 5:
            raise ValueError('Rating must be between 1 and 5')
        return data


class UpdateReview(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    book_id: Optional[int] = None
    rating: Optional[int] = None
    comment: Optional[str] = None
