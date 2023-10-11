from PySide6.QtWidgets import QApplication, QComboBox
from PySide6.QtGui import QPalette, QColor
import sys

app = QApplication(sys.argv)

# 创建下拉式的列举
combo_box = QComboBox()

# 启用编辑模式并设置为只读
combo_box.setEditable(True)
combo_box.lineEdit().setReadOnly(True)

# 添加选项
combo_box.addItem("Option 1")
combo_box.addItem("Option 2")
combo_box.addItem("Option 3")

# 设置默认选中项
combo_box.setCurrentIndex(-1)

# 设置选中项的背景颜色
palette = combo_box.palette()
palette.setColor(QPalette.Highlight, QColor(135, 206, 250))
combo_box.setPalette(palette)

# 处理选择事件
def handle_selection():
    selected_options = combo_box.currentText().split(", ")
    print(f"Selected options: {selected_options}")

combo_box.currentTextChanged.connect(handle_selection)

# 显示下拉式的列举
combo_box.show()

sys.exit(app.exec())
