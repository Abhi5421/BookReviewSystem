from sqlalchemy import Column, Integer, VARCHAR, DateTime, ForeignKey
from database.connection import Base
from datetime import datetime
from sqlalchemy.orm import relationship


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(VARCHAR(50), unique=True, index=True)
    author = Column(VARCHAR(50))
    publication_year = Column(Integer)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow())
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow(), onupdate=datetime.utcnow())

    def book_json(self):
        return {
            "title": self.title,
            "author": self.author,
            "publication_year": self.publication_year,
        }


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    rating = Column(Integer)
    comment = Column(VARCHAR(200))
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow())
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow(), onupdate=datetime.utcnow())

    book = relationship("Book", backref="reviews")
