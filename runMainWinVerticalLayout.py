# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\wwwww.000\PycharmProjects\pyqt5\MainWinVerticalLayout.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

import sys

import MainWinVerticalLayout
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow=QMainWindow()
    ui=MainWinVerticalLayout.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())