#__author__:"wanghui"

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import  *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class VBoxLayout(QWidget):
    def __init__(self):
        super(VBoxLayout,self).__init__()
        self.initUI()
    def initUI(self):
        #self.setWindowFlag(Qt.FramelessWindowHint)#这只隐藏边框
        self.setWindowTitle("伸缩量 Demo")
        btn01=QPushButton(self) #在self里面创建按钮
        btn02 = QPushButton(self)
        btn03 = QPushButton(self)
        btn01.setText("按钮1")#设置按钮名称
        btn02.setText("按钮1")
        btn03.setText("按钮1")
        '''#创建布局'''
        layout=QHBoxLayout()
        '''设置布局与控件的距离'''
        layout.setSpacing(0)  # 控件间隔
        '''设置控件与控件的距离'''
        layout.setContentsMargins(0, 0, 0, 0)
        '''设置控件与控件的伸缩量，0代表靠左排列，其他伸缩量按addStretch值一次伸缩'''
        layout.addStretch(0)  #
        layout.addWidget(btn01)#按钮加入布局

        layout.addStretch(1)
        layout.addWidget(btn02)
        layout.addStretch(0)
        layout.addWidget(btn03)


        self.setLayout(layout)#设置self(实例)的布局
        # self.button1=QPushButton("第一个按钮")
        # self.button1.setText("First Button1")
        # self.button1.setCheckable(True)
        # self.button1.toggle()
        # layout.addWidget(self.button1)
        # self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui=VBoxLayout()
    ui.show()
    sys.exit(app.exec_())










