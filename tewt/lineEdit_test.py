import sys
from PySide6.QtWidgets import QApplication, QLineEdit
from PySide6.QtGui import QPainter, QColor, QFont, QPen, QCursor
from PySide6.QtCore import Qt, QTimer

class CustomLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cursor_visible = True
        self.cursor_timer = QTimer(self)
        self.cursor_timer.timeout.connect(self.toggle_cursor)
        self.cursor_timer.start(500)  # 光标闪烁间隔时间为500ms

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 绘制背景
        painter.setBrush(QColor(240, 240, 240))
        painter.setPen(QColor(200, 200, 200))
        painter.drawRoundedRect(self.rect(), 5, 5)

        # 绘制文本
        painter.setPen(QColor(80, 80, 80))
        painter.setFont(QFont("Arial", 12))
        painter.drawText(self.rect().adjusted(5, 0, -5, 0), self.text())

        # 绘制光标
        if self.cursor_visible and self.hasFocus():
            cursor_rect = self.cursorRect()
            cursor_rect.setWidth(2)
            painter.setPen(QPen(QColor(0, 0, 0), 2))
            painter.drawRect(cursor_rect)

    def toggle_cursor(self):
        self.cursor_visible = not self.cursor_visible
        self.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    line_edit = CustomLineEdit()
    line_edit.resize(200, 30)
    line_edit.show()

    sys.exit(app.exec())
