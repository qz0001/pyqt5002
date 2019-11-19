# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\wwwww.000\PycharmProjects\pyqt5\new_jingmeijiemian\ceshi.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)#创建控制窗口
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)#创建布局窗口
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(330, 250, 361, 171))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)#1.在布局窗口内创建布局
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)    #控件距离布局线距离为0
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)#2.在布局窗口内创建按钮2
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)                    #2.1按钮2加入布局
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget)          #3.在布局窗口创建垂直分割线1
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)                        #3.1垂直分割线加入加入布局
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)#4.在布局窗口内创建按钮1
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)                    #4.1--按钮1加入布局
        self.line_2 = QtWidgets.QFrame(self.horizontalLayoutWidget)         #5 .在布局窗口创建垂直分割线2
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)                     #5.1垂直分割线-2加入加入布局
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)                        #6.上面创建弹簧，下面用addItem把弹簧加入布局
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)                    #7.创建菜单
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)                             #7.1启用菜单
        self.statusbar = QtWidgets.QStatusBar(MainWindow)               #8.创建状态栏
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)                        #8.1启用状态栏

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

if __name__ == '__main__':
    app = Ui_MainWindow(sys.argv)
    mainWindow=Ui_MainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())