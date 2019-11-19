#__author__:"wanghui"

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import  *
from PyQt5.QtWidgets import *

class QAbsoluteLayout(QWidget):
    def __init__(self):
        super(QAbsoluteLayout,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("绝对布局 Demo")
        layout=QVBoxLayout()

        self.label001=QLabel("欢迎",self)
        self.label001.move(60,20)

        # self.button1=QPushButton("第一个按钮")
        # self.button1.setText("First Button1")
        # self.button1.setCheckable(True)
        # self.button1.toggle()
        # layout.addWidget(self.button1)
        # self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui=QAbsoluteLayout()
    ui.show()
    sys.exit(app.exec_())










