from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True) # створюємо унікальний ІД
    name = Column(String(200), nullable=False, index=True) 

    books = relationship("Book", back_populates= 'author' ) 

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False, index=True) 
    pages = Column(Integer, nullable=False, defaulte=11)
    author_id = Column(Integer, ForeignKey("author.id"))

    author = relationship("Author", back_populates= 'books' ) 






