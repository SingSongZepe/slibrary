
from PySide6.QtCore import Qt

def mouseReleaseEvent(s, eve):
    if eve.button() == Qt.LeftButton:
        s.isMousePressed = False

    