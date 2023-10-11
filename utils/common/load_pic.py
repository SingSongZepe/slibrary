import requests

from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap

def load_pic(label: QLabel, cover: str):
    # cover is direct url
    try:
        pic_req = requests.get(cover)
        if pic_req.status_code != 200:
            print('error occurred while request for pic')
            return
    except Exception as exception:
        print(exception)
        return
    pixmap = QPixmap()
    pixmap.loadFromData(pic_req.content)
    label.setPixmap(pixmap)

