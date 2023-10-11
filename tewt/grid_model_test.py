from PySide6.QtWidgets import QApplication, QGridLayout, QLabel, QLineEdit, QPushButton, QWidget, QTableView, QAbstractItemView, QHeaderView
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex

class MyTableModel(QAbstractTableModel):
    def __init__(self, data, headers):
        super().__init__()
        self._data = data
        self._headers = headers

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return len(self._headers)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._headers[section]
        return super().headerData(section, orientation, role)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        return super().data(index, role)

app = QApplication([])

# 创建数据模型
data = [
    ["John", "Doe", 30],
    ["Jane", "Doe", 25],
    ["Bob", "Smith", 40]
]
headers = ["First Name", "Last Name", "Age"]
model = MyTableModel(data, headers)

# 创建网格布局和窗口
grid_layout = QGridLayout()
window = QWidget()
window.setLayout(grid_layout)

# 创建表格视图，并将其添加到网格布局中
table_view = QTableView()
table_view.setModel(model)
table_view.setSelectionBehavior(QAbstractItemView.SelectRows)
table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
grid_layout.addWidget(table_view, 0, 0)

# 创建标签、文本框和按钮，并将它们添加到网格布局中
first_name_label = QLabel("First Name:")
first_name_edit = QLineEdit()
grid_layout.addWidget(first_name_label, 1, 0)
grid_layout.addWidget(first_name_edit, 1, 1)

last_name_label = QLabel("Last Name:")
last_name_edit = QLineEdit()
grid_layout.addWidget(last_name_label, 2, 0)
grid_layout.addWidget(last_name_edit, 2, 1)

age_label = QLabel("Age:")
age_edit = QLineEdit()
grid_layout.addWidget(age_label, 3, 0)
grid_layout.addWidget(age_edit, 3, 1)

add_button = QPushButton("Add")
grid_layout.addWidget(add_button, 4, 0, 1, 2)

# 处理添加按钮的单击事件
def add_row():
    first_name = first_name_edit.text()
    last_name = last_name_edit.text()
    age = int(age_edit.text())
    model.insertRows(model.rowCount(), 1, [first_name, last_name, age])
    first_name_edit.clear()
    last_name_edit.clear()
    age_edit.clear()

add_button.clicked.connect(add_row)

# 显示窗口
window.show()

app.exec()
