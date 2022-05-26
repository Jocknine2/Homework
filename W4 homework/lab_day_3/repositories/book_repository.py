from db.run_sql import run_sql

from models.book import Book
from models.author import Author
import repositories.author_repository as author_repository


def save(book):
    sql = "INSERT INTO books (title, author_id) VALUES (?,?) RETURNING *"
    values = [book.title, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book


def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], author)
        books.append(book)
    return books


def select():
    book = None
    sql = "SELECT * FROM books WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = author_repository.select(result['author.id'])
        book = Book(result['title'], author, result['id'])
    return book


def delete_all():
    sql = "DELETE  FROM books"
    run_sql(sql)