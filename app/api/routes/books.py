from fastapi import APIRouter

router = APIRouter()


BOOKS = [
    {"id": "1", "title": "Title Three", "author": "Author Three", "category": "science"},
    {"id": "2", "title": "Title Two", "author": "Author Two", "category": "history"},
    {"id": "3", "title": "Title Four", "author": "Author Four", "category": "science"},
    {"id": "4", "title": "Title Five", "author": "Author Five", "category": "math"},
    {"id": "5", "title": "Title Six", "author": "Author Six", "category": "languages"},
    {"id": "6", "title": "Title One", "author": "Author One", "category": "science"},
]


@router.get("/books")
async def get_books():
    return BOOKS


@router.get("/books/{p}")
async def get_book(p):
    for book in BOOKS:
        if book["id"] is p:
            return book
    else:
        return "No book found with that ID"
