from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QScrollArea, QLabel, QMainWindow
import sys
from PySide6.QtGui import QPixmap

pic_path_sszp = '../res/img/reSSZp.png'

def dry(wgt: QWidget, color: str):
    wgt.setStyleSheet(f'background: {color}')
        

class ScrollableGridView(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个滚动区域
        scroll_area = QScrollArea()
        self.setCentralWidget(scroll_area)

        self.setFixedHeight(300)
        self.setFixedWidth(330)

        # 创建一个网格布局
        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)
        
        # 添加子widget到网格布局中
        for i in range(10):  # 假设有10行
            for j in range(3):  # 每行有3个子widget
                wgt = QWidget()
                wgt.setFixedHeight(100)
                wgt.setFixedWidth(100)

                dry(wgt, 'blue')

                label = QLabel(wgt)
                label.setGeometry(0, 0, 50, 50)
                label.setPixmap(QPixmap(pic_path_sszp))
                grid_layout.addWidget(wgt, i, j)

        # 创建一个占位widget，用于撑开滚动区域的高度
        spacer = QWidget()
        spacer.setMinimumHeight(10 + (10 - 1) * grid_layout.spacing())  # 计算网格布局的总高度
        grid_layout.addWidget(spacer, 10, 0, 1, 3)

        # 设置滚动区域的窗口小部件为网格布局
        scroll_widget = QWidget()
        scroll_widget.setLayout(grid_layout)
        scroll_area.setWidget(scroll_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScrollableGridView()
    window.show()
    sys.exit(app.exec())
