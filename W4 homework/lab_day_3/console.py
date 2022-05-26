import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author_repository.delete_all()
book_repository.delete_all()

author1 = Author("John", "Jones")
author_repository.save(author1)
author2 = Author("Billy", "Bobson")
author_repository.save(author2)

book1 = Book("Into The Deep", author2)
book_repository.save(book1)
book2 = Book("How To Code", author1)
book_repository.save(book2)

pdb.set_trace()
