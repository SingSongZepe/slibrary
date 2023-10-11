
from PySide6.QtCore import Qt

def mousePressEvent(s, eve):
    if eve.button() == Qt.LeftButton:
        s.isMousePressed = True
        s.mousePressPos = eve.pos()

        