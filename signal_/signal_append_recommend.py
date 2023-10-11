
from object.book import Book

from PySide6.QtCore import QObject, Signal

class SIGNAL_APPEND_RECOMMEND(QObject):
    signal_append_recommend = Signal(Book)
