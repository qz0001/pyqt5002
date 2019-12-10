# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\wwwww.000\PycharmProjects\pyqt5\new_jingmeijiemian\frmroundplot0002.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmRoundPlot(object):
    def setupUi(self, frmRoundPlot):
        frmRoundPlot.setObjectName("frmRoundPlot")
        frmRoundPlot.resize(318, 605)
        self.verticalLayout = QtWidgets.QVBoxLayout(frmRoundPlot)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget1 = RoundPlot(frmRoundPlot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget1.sizePolicy().hasHeightForWidth())
        self.widget1.setSizePolicy(sizePolicy)
        self.widget1.setObjectName("widget1")
        self.verticalLayout.addWidget(self.widget1)
        self.widget2 = RoundPlot(frmRoundPlot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget2.sizePolicy().hasHeightForWidth())
        self.widget2.setSizePolicy(sizePolicy)
        self.widget2.setObjectName("widget2")
        self.verticalLayout.addWidget(self.widget2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labMaxValue = QtWidgets.QLabel(frmRoundPlot)
        self.labMaxValue.setObjectName("labMaxValue")
        self.gridLayout.addWidget(self.labMaxValue, 0, 2, 1, 1)
        self.txtMaxValue = QtWidgets.QLineEdit(frmRoundPlot)
        self.txtMaxValue.setObjectName("txtMaxValue")
        self.gridLayout.addWidget(self.txtMaxValue, 0, 3, 1, 1)
        self.txtMinValue = QtWidgets.QLineEdit(frmRoundPlot)
        self.txtMinValue.setObjectName("txtMinValue")
        self.gridLayout.addWidget(self.txtMinValue, 0, 1, 1, 1)
        self.txtValue = QtWidgets.QLineEdit(frmRoundPlot)
        self.txtValue.setObjectName("txtValue")
        self.gridLayout.addWidget(self.txtValue, 1, 1, 1, 1)
        self.labUnit = QtWidgets.QLabel(frmRoundPlot)
        self.labUnit.setObjectName("labUnit")
        self.gridLayout.addWidget(self.labUnit, 1, 2, 1, 1)
        self.labValue = QtWidgets.QLabel(frmRoundPlot)
        self.labValue.setObjectName("labValue")
        self.gridLayout.addWidget(self.labValue, 1, 0, 1, 1)
        self.txtUnit = QtWidgets.QLineEdit(frmRoundPlot)
        self.txtUnit.setText("")
        self.txtUnit.setObjectName("txtUnit")
        self.gridLayout.addWidget(self.txtUnit, 1, 3, 1, 1)
        self.labMinValue = QtWidgets.QLabel(frmRoundPlot)
        self.labMinValue.setObjectName("labMinValue")
        self.gridLayout.addWidget(self.labMinValue, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.pushButton = QtWidgets.QPushButton(frmRoundPlot)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(frmRoundPlot)
        QtCore.QMetaObject.connectSlotsByName(frmRoundPlot)

    def retranslateUi(self, frmRoundPlot):
        _translate = QtCore.QCoreApplication.translate
        frmRoundPlot.setWindowTitle(_translate("frmRoundPlot", "widget"))
        self.labMaxValue.setText(_translate("frmRoundPlot", "最大值"))
        self.txtMaxValue.setText(_translate("frmRoundPlot", "100"))
        self.txtMinValue.setText(_translate("frmRoundPlot", "0"))
        self.txtValue.setText(_translate("frmRoundPlot", "88"))
        self.labUnit.setText(_translate("frmRoundPlot", "单位"))
        self.labValue.setText(_translate("frmRoundPlot", "当前值"))
        self.labMinValue.setText(_translate("frmRoundPlot", "最小值"))
        self.pushButton.setText(_translate("frmRoundPlot", "加载"))

from roundplot import RoundPlot
