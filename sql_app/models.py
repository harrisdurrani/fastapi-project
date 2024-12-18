from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    dob = Column(String, index=True)
    address = Column(String, index=True)
    city = Column(String, index=True)
    state = Column(String, index=True)
    zip_code = Column(Integer, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    librarycard = relationship("LibraryCard", uselist=False, back_populates="owner")


class LibraryCard(Base):
    __tablename__ = "librarycard"
    card_no = Column(Integer, primary_key=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.user_id"))
    owner = relationship("User", back_populates="librarycard")

class Book(Base):
    __tablename__ = "books"
    book_id = Column(Integer, primary_key=True)
    isbn = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    book_author = Column(String, nullable=False)
    publication_year = Column(Integer, nullable=True)
    publisher = Column(String, nullable=True)
    image_url = Column(String, nullable=True)

class Checkout(Base):
    __tablename__ = "checked_out"
    user_id = Column(Integer, primary_key=True)
    card_no = Column(Integer, primary_key=True)
    book_id = Column(Integer, primary_key=True)
    checkout_status = Column(Boolean, default=False)
