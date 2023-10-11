# this file is use to append history search or history book

from object.download import Download
from object.history_search import History_Search
from value.value import *

def append_history_book_launcher(self, download: Download):
    idx = len(self.downloads) - 1
    self.append_history_book(download, idx // history_columns, idx % history_columns)


# use for while search send a signal to append a record to view
def append_history_search_launcher(self, search: History_Search):
    idx = len(self.searches) - 1
    self.append_history_search(search, idx // history_columns, idx % history_columns)

