
from object.book import Book
from utils.common.gl_remove_wgt import gl_remove_wgt
from value.strings import *
from value.value import *

def append_recommends(self, books: [Book]):
    gl_remove_wgt(self.append_recommends)

    # new a object, the remain object will be delete    self.gl_result.setContentsMargins(0, 0, 0, 0)
    self.gl_result.setSpacing(spacing_gl_result)
    # self.gl_result.setAlignment(Qt.AlignTop)

    for idx, book in enumerate(books):
        self.append_recommend(book, idx // columns, idx % columns)


