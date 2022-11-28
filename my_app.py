from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit
from instr import *
from second_win import *

class Main(QWidget):
    def __init__(self):
        super().__init__()

        #Устанавливает, как будет выглядеть окно(надпись, размер, место)
        self.set_appear()

        #Создание и настройка графических элементов
        self.unitUI()

        #Устанавливаем связи между элементами
        self.connects()

        #Старт
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def unitUI(self):
        self.hello = QLabel('welcome')
        self.instruction = QLabel('instructions')
        self.button_next = QPushButton(txt_next, self)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello,alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.instruction,alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.button_next,alignment = Qt.AlignCenter)

        self.setLayout(self.layout_line)
        
    def connects(self):
        self.button_next.clicked.connect(self.next_click)

    def next_click(self):
        self.tw = SecondWin()
        self.hide()

app = QApplication([])
win = Main()
app.exec_()


