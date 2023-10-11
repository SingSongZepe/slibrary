import asyncio
from PySide6.QtWidgets import QApplication, QLabel

async def download_launcher():
    # 执行一些异步操作
    await asyncio.sleep(32)
    print("下载完成")

app = QApplication([])

label = QLabel("点击下载")
label.show()

async def on_button_clicked():
    print("开始下载")
    await download_launcher()

def button_clicked():
    asyncio.create_task(on_button_clicked())

label.mousePressEvent = button_clicked

asyncio.run(app.exec())
