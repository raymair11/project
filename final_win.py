from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit
from instr import *
from second_win import *


class Finish(QWidget):
    def __init__(self, ex,):
        super().__init__()
        self.ex = ex
        self.appear()
        self.unit()
        self.show()
        self.res()

    def appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def unit(self):
        self.heart = self.res()
        self.index = (4*(int(self.ex.res1)+int(self.ex.res2) +
                         int(self.ex.res3))-200)/10
        try:
            self.txt2 = QLabel(
                self.ex.name + ', ваша работоспособность сердца: ' + self.heart)
            self.txt = QLabel('Индекс Руфье: '+str(self.index))
        except TypeError:
            self.txt2 = QLabel(
                'Для получения результатов теста необходим ваш возраст. ')
            self.txt = QLabel('')

        self.line = QVBoxLayout()
        self.line.addWidget(self.txt, alignment=Qt.AlignCenter)
        self.line.addWidget(self.txt2, alignment=Qt.AlignCenter)
        self.setLayout(self.line)

    def res(self):
        self.index = (4*(int(self.ex.res1)+int(self.ex.res2) +
                         int(self.ex.res3))-200)/10
        print(self.index)
        if self.ex.age >= 15:
            if self.index >= 11 and self.index <= 14.9:
                return str_res2
            elif self.index >= 6 and self.index <= 10.9:
                return str_res3
            elif self.index >= 0.5 and self.index <= 5.9:
                return str_res4
            elif self.index >= 15:
                return str_res
            else:
                return str_res5
        elif self.ex.age == 13 or self.ex.age == 14:
            if self.index >= 12.5 and self.index <= 16.4:
                return str_res2
            elif self.index >= 7.5 and self.index <= 12.4:
                return str_res3
            elif self.index >= 2 and self.index <= 7.4:
                return str_res4
            elif self.index >= 16.5:
                return str_res
            else:
                return str_res5
        if self.ex.age == 11 or self.ex.age == 12:
            if self.index >= 14 and self.index <= 17.9:
                return str_res2
            elif self.index >= 9 and self.index <= 13.9:
                return str_res3
            elif self.index >= 3.5 and self.index <= 8.9:
                return str_res4
            elif self.index >= 18:
                return str_res
            else:
                return str_res5
        if self.ex.age == 9 or self.ex.age == 10:
            if self.index >= 15.5 and self.index <= 19.4:
                return str_res2
            elif self.index >= 10.5 and self.index <= 15.4:
                return str_res3
            elif self.index >= 5 and self.index <= 10.4:
                return str_res4
            elif self.index >= 19.5:
                return str_res
            else:
                return str_res5
        if self.ex.age == 7 or self.ex.age == 8:
            if self.index >= 17 and self.index <= 20.9:
                return str_res2
            elif self.index >= 12 and self.index <= 16.9:
                return str_res3
            elif self.index >= 6.5 and self.index <= 11.9:
                return str_res4
            elif self.index > 21:
                return str_res
            else:
                return str_res5
