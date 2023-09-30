from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import(
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QLineEdit, QRadioButton)

from third_win import*

class Question(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

    def set_appear(self):
        self.setWindowTitle("ежедневный тест")
        self.resize(600, 400)
        self.move(500, 300)

    def initUI(self):
        self.btn_next = QPushButton("Следующий вопрос")
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


        self.text = QLabel("Как оцениваете своё самочувствие сегодня?")
        self.text.setStyleSheet("QLabel"
                                 "{"
                                 "font: bold 14px;"
                                 "min-width: 10em;"
                                 "}")
        self.btn_number1 = QRadioButton("Всё отлично")
        self.btn_number2 = QRadioButton("Я очень усталый(ая)")
        self.btn_number3 = QRadioButton("Бывало и хуже")
        self.btn_number4 = QRadioButton("Всё ужасно")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.btn_number1, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.btn_number2, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.btn_number3, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.btn_number4, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)


        
    def next_click(self):
        self.hide()
        self.q2 = Question2()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)