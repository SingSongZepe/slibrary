
from object.book import Book
from value.value import *
from value.color import *
from utils.common.gl_remove_wgt import gl_remove_wgt

def append_books(self, books: [Book]):
    gl_remove_wgt(self.gl_result)

    # new a object, the remain object will be delete    self.gl_result.setContentsMargins(0, 0, 0, 0)
    self.gl_result.setSpacing(spacing_gl_result)
    # self.gl_result.setAlignment(Qt.AlignTop)

    self.wgt_result.setVisible(True)
    
    for idx, book in enumerate(books):
        # self.signal_append_book.signal_append_book.emit(book, idx // columns, idx % columns)
        self.append_book(book, idx // columns, idx % columns)

