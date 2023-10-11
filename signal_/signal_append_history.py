
from object.download import Download
from object.history_search import History_Search

from PySide6.QtCore import QObject, Signal

class SIGNAL_APPEND_HISTORY(QObject):
    signal_append_history_book = Signal(Download)
    signal_append_history_search = Signal(History_Search)
