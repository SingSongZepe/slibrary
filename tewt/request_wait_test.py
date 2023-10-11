from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

class NetworkRequestThread(QThread):
    finished = Signal()  # 定义一个信号，在网络请求完成时发射

    def run(self):
        # 在此处进行网络请求
        # ...

        # 模拟网络请求完成
        import time
        time.sleep(2)

        # 发射信号，表示网络请求完成
        self.finished.emit()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 创建等待动画
        self.movie = QMovie("loading.gif")

        # 创建等待动画标签
        self.label = QLabel()
        self.label.setMovie(self.movie)

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        # 创建并启动网络请求线程
        self.thread = NetworkRequestThread()
        self.thread.finished.connect(self.on_request_finished)
        self.thread.start()

        # 启动等待动画
        self.movie.start()

    def on_request_finished(self):
        # 在网络请求完成后更新UI界面
        # ...

        # 停止等待动画
        self.movie.stop()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
