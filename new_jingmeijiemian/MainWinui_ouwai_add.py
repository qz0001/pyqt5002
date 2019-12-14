# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\wwwww.000\PycharmProjects\pyqt5\new_jingmeijiemian\MainWinui_ouwai_add.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys,pymysql
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(699, 579)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 651, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 2, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 10, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 9, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 12, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 12, 2, 1, 1)

        self.dateTimeEdit = QtWidgets.QDateTimeEdit(QtCore.QDateTime.currentDateTime(), self.gridLayoutWidget)

        self.dateTimeEdit.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout.addWidget(self.dateTimeEdit, 7, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 11, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 8, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 10, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 6, 2, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 2, 2, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_4.setSizeIncrement(QtCore.QSize(0, 50))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 5, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 11, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setMinimumSize(QtCore.QSize(200, 0))
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 3, 13, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 4, 2, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(470, 520, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBox.setItemText(0, _translate("Dialog", "在院"))
        self.comboBox.setItemText(1, _translate("Dialog", "出院"))
        self.comboBox.setItemText(2, _translate("Dialog", "其他"))
        self.label_8.setText(_translate("Dialog", "受理日期"))
        self.label_9.setText(_translate("Dialog", "联系方式"))
        self.label_2.setText(_translate("Dialog", "状态"))
        self.label_13.setText(_translate("Dialog", "备注"))
        self.label_4.setText(_translate("Dialog", "年龄"))
        self.label_12.setText(_translate("Dialog", "投诉建议"))
        self.label.setText(_translate("Dialog", "姓名"))
        self.label_7.setText(_translate("Dialog", "费用"))
        self.label_10.setText(_translate("Dialog", "接诊医生"))
        self.label_11.setText(_translate("Dialog", "保险公司"))
        self.label_3.setText(_translate("Dialog", "性别"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "男"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "女"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "其他"))
        self.label_5.setText(_translate("Dialog", "病历摘要"))
        self.label_14.setText(_translate("Dialog", "TextLabel"))
        self.label_6.setText(_translate("Dialog", "检查资料"))
        self.buttonBox.accepted.connect(self.accept) #按钮框buttonBox  按ok时，连接槽函数为accept
        self.buttonBox.rejected.connect(self.reject)#按钮框buttonBox  按ocancel时，连接槽函数为reject


    def accept(self):
        db = pymysql.connect("116.62.199.133", "root", "321456", "ouwai", charset='utf8')
        # 获取游标、数据
        cur = db.cursor() #获取游标
        state=self.comboBox.currentText()  #下面是读取各个空间中的值
        name01=self.lineEdit.text()
        print(name01)
        gender=self.comboBox_2.currentText()
        age=self.lineEdit_2.text()
        case_summary=self.textEdit.toPlainText()
        inspection_data=self.lineEdit_4.text()
        cost=self.lineEdit_5.text()
        print(cost)
        print(type(cost))

        accept_date=self.dateTimeEdit.dateTime().toString(QtCore.Qt.ISODate)  #获取时间编辑框里面的内容
        print(accept_date)
        #print(accept_date.toString(QtCore.Qt.ISODate))
        contact_information=self.lineEdit_6.text()
        attending_doctor=self.lineEdit_7.text()
        company=self.lineEdit_8.text()
        complaint=self.lineEdit_9.text()
        remarks=self.lineEdit_10.text()

        # state, name01, gender, age, case_summary,inspection_data, cost,accept_date, contact_information, attending_doctor, company, complaint,remarks))
        # state, name01, gender, str(age), case_summary,inspection_data, str(cost),accept_date, contact_information, attending_doctor, company, complaint,remarks))
        sql= 'insert into patient_record(state, name01, gender, age, case_summary,inspection_data,cost,accept_date, contact_information, attending_doctor, company, complaint,remarks) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        res = cur.execute(sql,(state, name01, gender, age , case_summary,inspection_data,cost,accept_date, contact_information, attending_doctor, company, complaint,remarks))  # 执行sql语句，返回sql影响成功的行数
        db.commit()
        cur.close()
        db.close()
        print(res)
        print(cur.lastrowid)

    def reject(self):
        pass




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QDialog()
    window = Ui_Dialog()
    window.setupUi(form)
    form.show()
    sys.exit(app.exec_())

