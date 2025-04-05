from fastapi import depends, FastApI, Query
from pydantic import BaseModel, Field
from typing import Union

from sqlalchemy.orm import Session
from db.database import SessionLocal, engine
from db import models, schemas, crud

models.Base.metadata.create_all(bind=engine)


app = FastAPI()
# Залежність
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

all_books = {"Джордж Орвелл": ("1984", 328),
    "Френсіс Скотт Фіцджеральд": ("Великий Гетсбі", 180),
    "Гарпер Лі": ("Убити пересмішника", 281),
    "Герман Мелвілл": ("Мобі Дік", 635),
    "Лев Толстой": ("Війна і мир", 1225),
    "Федір Достоєвський": ("Злочин і кара", 671),
    "Михайло Булгаков": ("Майстер і Маргарита", 470),
    "Стівен Кінг": ("Воно", 1138),
    "Джоан Роулінг": ("Гаррі Поттер і філософський камінь", 223),
    "Ернест Хемінгуей": ("Старий і море", 127),
            }



@app.get("/")
async def get_all_books(db: Session = Depends(get_db)):
    """
    Повертає список усіх книг бібліотеки
    """
    return crud.get_all_books()

@app.get("/add_book")
async def get_new_books(book:schemas.BookDB):
    """
    Додає нову книгу
    """
    if book.author  in all_books:
        all_books[book.author] = [(book.title, book.pages)]
    else:
        all_books[book.author].append((book.title, book.pages))

    return {"massage": "Книга успішно створена"}


@app.get("/author/{author}")
async def get_author_books(author:str):
    if author in all_books:
        return all[author]
    else:
        return {'message': "Книги автора не знайдено"}
    
@app.get("/{author}/{book_title}")
async def update_book_pages(author: str, book_title: str,
                             new_hages: int = Query(gt=10, title="Нова кількість сторінок")):
    if author in all_books:
        for book in all_books[author]:
            if book[0] == book_title:
                book[1] = new_page
                return {"message": 'update'}
            return {'error': 'not find'}
        
@app.get("/{author}/{book_title}")
async def delete_book(author: str, book_title: str):
    if author in all_books:
        for book in all_books[author]:
            if book[0] == book_title:
                all_books[author].remove(book)
                return{'message': "Gotovo"}
    return {'error' : 'not find'}




    


