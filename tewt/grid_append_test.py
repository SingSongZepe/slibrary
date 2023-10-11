from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

app = QApplication([])
window = QWidget()

grid_layout = QGridLayout()
window.setLayout(grid_layout)

button1 = QPushButton("Button 1")
button2 = QPushButton("Button 2")
button3 = QPushButton("Button 3")

grid_layout.addWidget(button1)
grid_layout.addWidget(button2)
grid_layout.addWidget(button3)

window.show()
app.exec()
