#__author__:"wanghui"

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import  *
from PyQt5.QtWidgets import *

class HBoxLayout(QWidget):
    def __init__(self):
        super(HBoxLayout,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("绝对布局 Demo")
        vlayout=QVBoxLayout()

        vlayout.addWidget(QPushButton("按钮001"))
        vlayout.addWidget(QPushButton("按钮001"))
        vlayout.addWidget(QPushButton("按钮001"))
        vlayout.addWidget(QPushButton("按钮001"))
        vlayout.addWidget(QPushButton("按钮001"))
        vlayout.addWidget(QPushButton("按钮001"))
        vlayout.setSpacing(40)#控件间隔
        self.setLayout(vlayout)

        # self.button1=QPushButton("第一个按钮")
        # self.button1.setText("First Button1")
        # self.button1.setCheckable(True)
        # self.button1.toggle()
        # layout.addWidget(self.button1)
        # self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui=HBoxLayout()
    ui.show()
    sys.exit(app.exec_())










