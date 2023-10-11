
from object.book import Book

from PySide6.QtCore import QObject, Signal

class SIGNAL_APPEND_BOOK(QObject):
    signal_append_books = Signal(Book)
    signal_append_book = Signal(Book, int, int)
