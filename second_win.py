from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit
from instr import *
from final_win import *
from PyQt5.QtGui import QFont


class Ex():
    def __init__(self, age, res1, res2, res3):
        super().__init__()
        self.age = age
        self.res1 = res1
        self.res2 = res2
        self.res3 = res3


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
        self.t = QLabel('00:00:00')
        self.buttonFinish = QPushButton('Отправить результаты')
        self.button1 = QPushButton('Запустить таймер')
        self.button2 = QPushButton('Запустить счётчик приседаний')
        self.button3 = QPushButton('Запустить таймер')
        self.lay.addWidget(self.name, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.line1, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.age, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.line2, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.test1, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.button1, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.line3, alignment=Qt.AlignLeft, )
        self.lay.addWidget(self.test2, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.button2, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.test3, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.button3, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.line4, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.line5, alignment=Qt.AlignLeft)
        self.lay.addWidget(self.t, alignment=Qt.AlignRight)
        self.lay.addWidget(self.buttonFinish, alignment=Qt.AlignCenter)
        self.t.setFont(QFont('Times', 36, QFont.Bold))
        self.setLayout(self.lay)

    def connects(self):
        self.button1.clicked.connect(self.timer_test)
        self.button2.clicked.connect(self.timer_test2)
        self.button3.clicked.connect(self.timer_test3)
        self.buttonFinish.clicked.connect(self.next_click)

    def next_click(self):
        self.ex = Ex(int(self.line2.text()), int(self.line3.text()),
                     int(self.line4.text()), int(self.line5.text()))
        self.idk = Finish(self.ex)
        self.hide()

    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1)
        self.timer.start(1000)

    def timer1(self):
        global time
        time = time.addSecs(-1)
        self.t.setText(time.toString('hh:mm:ss'))
        self.t.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def timer_test2(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2)
        self.timer.start(1500)

    def timer2(self):
        global time
        time = time.addSecs(-1)
        self.t.setText(time.toString('hh:mm:ss')[6:8])
        self.t.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def timer_test3(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3)
        self.timer.start(1000)

    def timer3(self):
        global time
        time = time.addSecs(-1)
        self.t.setText(time.toString('hh:mm:ss'))
        if int(time.toString('hh:mm:ss')[6:8]) >= 45:
            self.t.setStyleSheet('color: rgb(0,200,0)')
        elif int(time.toString('hh:mm:ss')[6:8]) <= 15:
            self.t.setStyleSheet('color: rgb(0,200,0)')
        else:
            self.t.setStyleSheet('color: rgb(0,0,0)')

        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()


# app = QApplication([])
# app.exec_()
