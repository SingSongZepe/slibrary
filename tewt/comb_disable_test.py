from PySide6.QtWidgets import QApplication, QComboBox, QStyle, QStyledItemDelegate, QStyleOptionViewItem
from PySide6.QtGui import QStandardItemModel, QStandardItem, QFont
from PySide6.QtCore import Qt
import sys

app = QApplication(sys.argv)

# 创建下拉式的列举
combo_box = QComboBox()

# 创建自定义模型
model = QStandardItemModel()

# 添加选项
item1 = QStandardItem("Option 1")
item2 = QStandardItem("Option 2")
item3 = QStandardItem("Option 3")
item4 = QStandardItem("Option 4")

# # 设置项的标志来禁用它们
# item2.setFlags(item2.flags() & ~Qt.ItemIsEnabled)
# item4.setFlags(item4.flags() & ~Qt.ItemIsEnabled)

# 将项添加到模型中
model.appendRow(item1)
model.appendRow(item2)
model.appendRow(item3)
model.appendRow(item4)

# 将模型设置为下拉式的列举的模型
combo_box.setModel(model)

font = QFont("Times New Roman", 12)
combo_box.setFont(font)


# 自定义项的委托以禁用项的显示
# delegate = QStyledItemDelegate()

# def paint(delegate, painter, option, index):
#     if not index.flags() & Qt.ItemIsEnabled:
#         option.state &= ~QStyle.State_Enabled
#     delegate.paint(painter, option, index)

# delegate.paint = paint

# combo_box.setItemDelegate(delegate)

# # 处理选择事件
# def handle_selection(index):
#     item = model.itemFromIndex(index)
#     if item.flags() & Qt.ItemIsEnabled:
#         print(f"Selected option: {item.text()}")

# combo_box.currentIndexChanged.connect(handle_selection)

# 显示下拉式的列举
combo_box.show()

sys.exit(app.exec())
