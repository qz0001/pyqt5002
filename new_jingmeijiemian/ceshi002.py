from PyQt5.QtWidgets import (QWidget, QCalendarWidget,
                             QLabel, QApplication, QVBoxLayout)
from PyQt5.QtCore import QDate
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()
        # 初始化UI
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout(self)
        # 创建日历小部件
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)
        # 添加日历控件到布局
        vbox.addWidget(cal)

        # 设置一个显示Label
        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        # 添加Label到布局
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)
        # 设置控件大小位置和标题
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('日历小控件')
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

