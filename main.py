# launch slibrary
from slibrary import SLIBRARY

from PySide6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication([])
    slibrary = SLIBRARY()
    slibrary.show()
    app.exec()
    