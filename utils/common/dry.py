
from PySide6.QtWidgets import QWidget

def dry(wgt: QWidget, color: str):
    wgt.setStyleSheet(f'background: {color}')
        