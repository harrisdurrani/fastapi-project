from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Path
from sqlalchemy.orm import Session
from sql_app import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/{user_email}", response_model=schemas.User)
def read_users_by_email(user_email: Annotated[str, Path], db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user_email)
    if not db_user:
        raise HTTPException(status_code=400, detail="Email not found")
    return db_user


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.LibraryCard)
def create_item_for_user(user_id: int, db: Session = Depends(get_db)):
    existing_library_card = crud.get_library_card(db, user_id=user_id)
    
    if existing_library_card:
        raise HTTPException(status_code=400, detail= f"User_id {user_id} already has a library card")
    return crud.create_user_item(db=db, user_id=user_id)


@app.get("/items/", response_model=list[schemas.LibraryCard])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@app.get("/book/{title}", response_model=schemas.BookResponse)
def get_book(title: str, db: Session = Depends(get_db)):
    book = crud.get_book(db=db, book_title=title)
    return book


@app.post("/books/", response_model=schemas.BookResponse)
def create_book(book: schemas.BaseBook, db: Session = Depends(get_db)):
    existing_book = crud.get_book(db, book_title= book.title)
    if existing_book:
        raise HTTPException(status_code=400, detail="Book already in catalog")
    return crud.create_book(db, book)

# @app.patch("/checkout_book", response_model = schemas.CheckoutBook)
# def 