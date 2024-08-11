from fastapi import APIRouter

router = APIRouter()


BOOKS = [
    {"id": "1", "title": "Title Three", "author": "Author Three", "category":
        "science", "favorite": False},
    {"id": "2", "title": "Title Two", "author": "Author Two", "category": "history",
     "favorite": False},
    {"id": "3", "title": "Title Four", "author": "Author Four", "category": "science",
     "favorite": True},
    {"id": "4", "title": "Title Five", "author": "Author Five", "category": "math",
     "favorite": False},
    {"id": "5", "title": "Title Six", "author": "Author Six", "category": "languages",
     "favorite": False},
    {"id": "6", "title": "Title One", "author": "Author One", "category": "science",
     "favorite": True},
]


@router.get("/books")
async def get_books():
    return BOOKS


@router.get("/books/mybook")
async def get_favorite_books():
    user_favorites = []
    for book in BOOKS:
        if book.get("favorite") is True:
            user_favorites.append(book)

    if len(user_favorites) == 0:
        return "no books marked as a favorite, yet"
    else:
        return user_favorites


@router.get("/books/{p}")
async def get_book(p: str):
    for book in BOOKS:
        if book.get("id") == p:
            return book
    else:
        return "no books with that id"
