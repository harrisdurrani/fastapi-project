from pydantic import BaseModel, Field
from sqlalchemy.types import Date

from sql_app.models import Book

class LibraryCardBase(BaseModel):
    card_no: int
    description: str | None = None


class LibraryCard(LibraryCardBase):
    owner_id: int


class UserBase(BaseModel):
    first_name: str
    last_name: str
    dob: str
    address: str
    city: str
    state: str
    zip_code: int
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    user_id: int
    is_active: bool
    librarycard: LibraryCard


class BaseBook(BaseModel):
    isbn: int
    title: str
    book_author: str
    publication_year: int | None = None
    publisher: str | None = None
    image_URL: str | None = None


class BookResponse(BaseBook):
    book_id: int
    checkout_status: bool = False

class CheckoutBook(BaseModel):
    user: User
    book: BookResponse