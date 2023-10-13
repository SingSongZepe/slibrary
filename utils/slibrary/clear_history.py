
from utils.common.gl_remove_wgt import gl_remove_wgt
from value.strings import *

from PySide6.QtCore import QMutexLocker

# associated with the current tag idx
def clear_history(self):
    with QMutexLocker(self.mutex):
        if self.current_history_type == history_search_:
            self.searches.clear()
            gl_remove_wgt(self.gl_history_search)
            self.ln('history records of search are cleared')
        elif self.current_history_type == history_book_:
            self.downloads.clear()
            gl_remove_wgt(self.gl_history_book)
            self.ln('history records of download are cleared')
