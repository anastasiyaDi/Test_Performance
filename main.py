from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QLineEdit)

from second_win import*

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def initUI(self):
        self.btn_next = QPushButton("Начнём тест!")
        self.btn_next.setStyleSheet("QPushButton"
                                    "{"
                                    "background-color: rgb(32, 178, 170);"
                                    "border-style: outset;"
                                    "border-width: 2px;"
                                    "border-radius: 10px;"
                                    "border-color: rgb(2, 63, 7);"
                                    "font: bold 14px;"
                                    "min-width: 10em;"
                                    "padding: 6px;"
                                    "}")
        self.hello_text = QLabel("Здравствуйте сотруднки нашей компании!")
        self.hello_text1 = QLabel("Давайте начнём ежедневный учёт вашего самочувствия!")
        self.hello_text.setStyleSheet("QLabel"
                                 "{"
                                 "background : rgb(102, 205, 170);"
                                 "font: bold 14px;"
                                 "min-width: 10em;"
                                 "}")
        self.hello_text1.setStyleSheet("QLabel"
                                 "{"
                                 "font: bold 10px;"
                                 "min-width: 20em;"
                                 "}")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.hello_text1, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)

    def next_click(self):
        self.q = Question()
        self.hide()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWindowTitle("Ежедневный тест")
        self.resize(600, 400)
        self.move(500, 300)

app = QApplication([])
mw = MainWin()
app.exec_()