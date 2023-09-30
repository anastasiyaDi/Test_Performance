from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import(
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QLineEdit)


class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.show()

    def initUI(self):
        self.work_text = QLabel ("Спасибо, что прошли тестирование!")
        self.work_text.setStyleSheet("QLabel"
                                 "{"
                                 "font: bold 14px;"
                                 "min-width: 10em;"
                                 "}")
        self.layout_line = QVBoxLayout() 
        self.layout_line.addWidget(self.work_text, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)

    def set_appear(self):
        self.setWindowTitle("ежедневный тест")
        self.resize(600, 400)
        self.move(500, 300)