# use for a gridLayout removing of all the children widget

from PySide6.QtWidgets import QGridLayout 

def gl_remove_wgt(gl: QGridLayout):
    while gl.count():
        item = gl.takeAt(0)
        wgt = item.widget()
        if item:
            wgt.deleteLater()

