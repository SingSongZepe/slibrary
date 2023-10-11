# a object of a book downloading
from dataclasses import dataclass

from object.book import Book
from object.time import Time

@dataclass
class Download:
    time: Time
    book: Book

    