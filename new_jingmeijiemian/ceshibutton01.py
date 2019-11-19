#__author__:"wanghui"
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import  *
from PyQt5.QtWidgets import *

class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("QPushButton Demo")
        layout=QVBoxLayout()

        self.button1=QPushButton("第一个按钮")
        self.button1.setText("First Button1")
        self.button1.setCheckable(True)
        self.button1.toggle()
        layout.addWidget(self.button1)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui=QPushButtonDemo()
    ui.show()
    sys.exit(app.exec_())



