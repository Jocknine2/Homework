from db.run_sql import run_sql

from models.author import Author
from models.book import Book
from repositories import book_repository


def save(author):
    sql = "INSERT INTO authors (first_name, last_name) VALUES (?, ?) RETURNING *"
    values = [author.first_name, author.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author


def select_all():
    authors = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        book = book_repository.select(row['book_id'])
        author = Author(row['first_name'], row['last_name'])
        authors.append(author)
    return authors


def select(id):
    author = None
    sql = "SELECT * FROM authors WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = Author(result['first_name'],
                        result['last_name'], result['id'])
    return author


def delete_all():
    sql = "DELETE  FROM authors"
    run_sql(sql)