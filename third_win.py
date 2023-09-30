from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import(
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QLineEdit, QRadioButton)

from fourth_win import*

class Question2(QWidget):
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


        self.text = QLabel("Какой Ваш уровень работоспособности")
        self.text.setStyleSheet("QLabel"
                                 "{"
                                 "font: bold 14px;"
                                 "min-width: 10em;"
                                 "}")
        self.btn_number1 = QRadioButton ("Я готов к любой работе!")
        self.btn_number2 = QRadioButton ("Не хочется ничего делать, но надо")
        self.btn_number3 = QRadioButton ("Лучше бы остался(ась) дома")
        self.btn_number4 = QRadioButton ("Не могу ничего делать!")

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
        self.q3 = Question3()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)