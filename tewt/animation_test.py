import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QRect, QPropertyAnimation, QEasingCurve

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Click me", self)
        self.button.setGeometry(QRect(100, 100, 100, 30))
        self.button.clicked.connect(self.start_animation)

    def start_animation(self):
        animation = QPropertyAnimation(self.button, "geometry")
        animation.setDuration(1000)
        animation.setStartValue(self.button.geometry())
        animation.setEndValue(self.button.geometry().translated(100, 100))
        animation.setEasingCurve(QEasingCurve.InOutQuad)
        animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
