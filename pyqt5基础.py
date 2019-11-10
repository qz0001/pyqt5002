#__author__:"wanghui"
import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    #创建一个QApplication类的实例
    app=QApplication(sys.argv)
    #创建一个窗口
    w=QWidget()
    w.resize(300,150)
    #移动窗口
    w.move(300,300)
    #设置窗口的标题
    w.setWindowTitle("wanghui的第一个pyqt5窗口")
    #现实窗口
    w.show()
    #进入程序的主循环
    sys.exit(app.exec_())







