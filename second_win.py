from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit
from instr import *
from final_win import *


class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.appear()
        self.unit()
        self.connects()
        self.show()

    def appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def unit(self):
        self.name = QLabel(name)
        self.line1 = QLineEdit('Ф.И.О')
        self.age = QLabel(age)
        self.line2 = QLineEdit('0')
        self.test1 = QLabel(test1)
        self.line3 = QLineEdit('0')
        self.test2 = QLabel(test2)
        self.lay = QVBoxLayout()
        self.lay2 = QVBoxLayout()
        self.test3 = QLabel(test3)
        self.line4 = QLineEdit('0')
        self.line5 = QLineEdit('0')
        self.t = QLabel('hhhhhhh')
        self.buttonFinish = QPushButton('Отправить результаты')
        self.button1 = QPushButton('Начать тест 1')
        self.button2 = QPushButton('Начать тест 2')
        self.button3 = QPushButton('Начать тест 3')
        self.lay.addWidget(self.name, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.line1, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.age, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.line2, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.test1, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.button1, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.line3, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.test2, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.button2, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.test3, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.button3, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.line4, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.line5, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.t, alignment=Qt.AlignRight)
        self.lay.addWidget(self.buttonFinish, alignment=Qt.AlignCenter)

        self.setLayout(self.lay)

    def connects(self):
        self.button1.clicked.connect(self.timer)
        self.buttonFinish.clicked.connect(self.next_click)

    def next_click(self):
        self.tw = Finish()
        self.hide()

    def timer(self):

        from time import sleep
        for i in range(0, 60, -1):
            self.t.setText(str(i))
            sleep(1)


# app = QApplication([])
# app.exec_()
