from PySide6.QtWidgets import QApplication, QLabel
import sys

app = QApplication(sys.argv)

# Создаем QLabel
label = QLabel()

# Устанавливаем HTML разметку с переносом строки
label.setText("<html>Текст по вертикали<br>в две строки</html>")

# Отображаем QLabel
label.show()

sys.exit(app.exec())
