from flask import Flask, render_template, request, redirect
from repositories import book_repository, author_repository
from models.book import Book


from flask import Blueprint

books_blueprint = Blueprint("books", __name__)


@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("index.html", all_books=books)


@books_blueprint.route("/books/new", methods=["GET"])
def new_task():
    authors = author_repository.select_all()
    return render_template("tasks/new.html", all_authors=authors)
