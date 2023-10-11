from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget

app = QApplication([])

window = QMainWindow()
widget = QWidget()
layout = QVBoxLayout(widget)

label1 = QLabel("Label 1")
label1.setStyleSheet("background-color: red;")

label2 = QLabel("Label 2")
label2.setStyleSheet("background-color: blue;")

layout.addWidget(label1)
layout.addWidget(label2)

def resizeEvent(event):
    # 获取窗口的大小
    window_size = window.size()

    # 设置label1的位置和大小
    label1.setGeometry(10, 10, window_size.width() - 20, 50)

    # 设置label2的位置和大小
    label2.setGeometry(10, 70, window_size.width() - 20, 50)

# 将resizeEvent与窗口的resize事件关联
window.resizeEvent = resizeEvent

window.setCentralWidget(widget)
window.show()

app.exec()
