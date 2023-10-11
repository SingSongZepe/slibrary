from PySide6.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QGridLayout, QLabel
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 创建滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # 创建一个QWidget作为滚动区域的子widget
        content_widget = QWidget(scroll_area)
        scroll_area.setWidget(content_widget)

        # 创建一个垂直布局管理器
        layout = QVBoxLayout(content_widget)
        layout.setAlignment(Qt.AlignTop)

        # 创建子widget并添加到布局中
        for i in range(20):  # 假设有20个子widget
            label = QLabel(f"Widget {i+1}")
            label.setStyleSheet("background-color: yellow")  # 设置背景颜色
            layout.addWidget(label)
        
        # 创建一个网格布局管理器，每行两个子widget
        grid_layout = QGridLayout()
        grid_layout.addLayout(layout, 0, 0, -1, 2)  # -1表示占满剩余空间
        content_widget.setLayout(grid_layout)

        # 设置主窗口的布局为QVBoxLayout
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

