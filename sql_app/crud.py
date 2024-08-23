from sqlalchemy.orm import Session
from sql_app import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_dob(db: Session, dob: str):
    return db.query(models.User).filter(models.User.dob == dob).first()
    

def get_book(db:Session, book_title:str):
    return db.query(models.Book).filter(models.Book.title == book_title).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(
                        email=user.email, hashed_password=fake_hashed_password, first_name=user.first_name,
                        last_name=user.last_name, dob=user.dob, address=user.address,
                        city=user.city, state=user.state, zip_code=user.zip_code
                        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.LibraryCard).offset(skip).limit(limit).all()

def get_library_card(db: Session, user_id: int):
    return db.query(models.LibraryCard).filter(models.LibraryCard.owner_id == user_id).first()


def create_user_item(db: Session, user_id: int):
    db_item = models.LibraryCard(owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def create_book(db: Session, book: schemas.BaseBook):
    db_item = models.Book(
        isbn=book.isbn, title= book.title, book_author = book.book_author
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
