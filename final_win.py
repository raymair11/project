from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit
from instr import *
from second_win import *
class Finish(QWidget):
    def __init__(self):
        super().__init__()
        self.appear()
        self.unit()
        # self.connects()
        self.show()
    def appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def unit(self):
        self.res1 = QLabel()
        self.res2 = QLabel()
        self.line = QVBoxLayout()
        self.line.addWidget(self.res1,alignment = Qt.AlignCenter)
        self.line.addWidget(self.res2,alignment = Qt.AlignCenter)
