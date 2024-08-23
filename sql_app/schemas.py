from pydantic import BaseModel
from sqlalchemy.types import Date

class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
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
    id: int
    is_active: bool
    items: list[Item] = []


class BaseBook(BaseModel):
    isbn: int
    title: str
    book_author: str
    publication_year: int | None = None
    publisher: str | None = None
    image_URL: str | None = None


class BookResponse(BaseBook):
    id: int