#__author__:"wanghui"
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self,parent=None):#初始化窗口，接收控件parent
        super(FirstMainWin,self).__init__(parent)
        #设置窗口标题
        self.setWindowTitle("第一个主窗口标题")
        #色湖之窗口尺寸
        self.resize(400,400)
        #得到状态栏
        self.status=self.statusBar()
        #再状态栏上显示消息
        self.status.showMessage("只存在5秒的消息",5000)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/wanghui.ico"))
    main=FirstMainWin()
    main.show()
    sys.exit(app.exec_())




