

from PyQt5.QtCore import Qt, QTimer, QTime, QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit
from instr import *
from PyQt5.QtGui import QFont
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
app = QApplication([])
QSS_LabelBold = '''QLabel { 
    font: bold 25px;
}'''


class Ex():
    def __init__(self, name, age, res1, res2, res3):
        super().__init__()
        self.age = age
        self.res1 = res1
        self.res2 = res2
        self.res3 = res3
        self.name = name


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

        self.media_player = QMediaPlayer()
        url = QUrl.fromLocalFile("tiktak.mp3")
        content = QMediaContent(url)
        self.media_player.setMedia(content)

        self.name = QLabel(name)
        self.line1 = QLineEdit('Ф И О')
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
        self.buttonFinish.setStyleSheet('background: rgb(150,200,250)')

        self.setLayout(self.lay)

    def connects(self):
        self.button1.clicked.connect(self.timer_test)
        self.button2.clicked.connect(self.timer_test2)
        self.button3.clicked.connect(self.timer_test3)
        self.buttonFinish.clicked.connect(self.next_click)

    def next_click(self):
        self.ex = Ex(self.line1.text(), int(self.line2.text()), int(self.line3.text()),
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
        self.media_player.play()
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
        self.media_player.play()
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
            self.media_player.play()
            self.t.setStyleSheet('color: rgb(0,200,0)')
        elif int(time.toString('hh:mm:ss')[6:8]) <= 15:
            self.media_player.play()
            self.t.setStyleSheet('color: rgb(0,200,0)')
        else:
            self.t.setStyleSheet('color: rgb(0,0,0)')

        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()


class Main(QWidget):
    def __init__(self):
        super().__init__()

        # Устанавливает, как будет выглядеть окно(надпись, размер, место)
        self.set_appear()

        # Создание и настройка графических элементов
        self.unitUI()

        # Устанавливаем связи между элементами
        self.connects()

        # Старт
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def unitUI(self):
        self.hello = QLabel('Приветствуем!')
        self.hello.setFont(QFont('Times', 25))
        self.instruction = QLabel(instruction)
        self.button_next = QPushButton(txt_next, self)
        self.instruction.setStyleSheet(QSS_LabelBold)
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.instruction, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.button_next, alignment=Qt.AlignCenter)

        self.setLayout(self.layout_line)
        self.button_next.setStyleSheet('background: rgb(150,200,250)')

    def connects(self):
        self.button_next.clicked.connect(self.next_click)

    def next_click(self):
        self.tw = SecondWin()
        self.hide()


win = Main()


class Finish(QWidget):
    def __init__(self, ex,):
        super().__init__()
        self.ex = ex
        self.appear()
        self.unit()
        self.show()
        self.again()

    def res(self):
        if self.ex.age < 7:
            self.index = 0
        self.index = (4*(int(self.ex.res1)+int(self.ex.res2) +
                         int(self.ex.res3)) - 200)/10
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
        if self.ex.age == 13 or self.ex.age == 14:
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

    def appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def unit(self):

        self.name = self.ex.name.split()
        print(self.name)
        self.button_again = QPushButton('Пройти тест заново')
        self.heart = self.res()
        self.index = (4*(int(self.ex.res1)+int(self.ex.res2) +
                         int(self.ex.res3))-200)/10
        try:
            self.txt2 = QLabel(
                self.name[1] + ', ваша работоспособность сердца: ' + self.heart)
            self.txt = QLabel('Индекс Руфье: '+str(self.index))
            self.button_again = QPushButton('Пройти тест заново')
        except TypeError:
            self.txt2 = QLabel(
                'Для получения результатов теста необходим ваш возраст. ')
            self.txt = QLabel('')
            self.button_again = QPushButton('Пройти тест заново')

        self.line = QVBoxLayout()
        self.line.addWidget(self.txt, alignment=Qt.AlignCenter)
        self.line.addWidget(self.txt2, alignment=Qt.AlignCenter)
        self.line.addWidget(self.button_again, alignment=Qt.AlignCenter)
        self.setLayout(self.line)

    def again2(self):

        self.hide()

        self.tw = SecondWin()

    def again(self):
        self.button_again.clicked.connect(self.again2)


app.exec_()
