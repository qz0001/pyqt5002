#__author__:"wanghui"

from PyQt5 import QtCore,QtGui,QtWidgets

import sys,pymysql
import qtawesome
from new_jingmeijiemian import MainWinui_ouwai_tabel,MainWinui_ouwai_tab_widget,MainWinui_ouwai_add
class QTitleLabel(QtWidgets.QLabel):  #这个地方是重写了标签类，不对，是原有的标签类还在，这是自定义的标签类
    """
    新建标题栏标签类ceshi0001
    """
    def __init__(self, *args):
        super(QTitleLabel, self).__init__(*args) #继承原有标签类属性
        self.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)  #设置这种标签栏的 位置模式
        self.setFixedHeight(30)                                          #设置这种标签栏的 高度


class QTitleButton(QtWidgets.QPushButton):#自定义按钮类
    """
    新建标题栏按钮类
    """
    def __init__(self, *args):
        super(QTitleButton, self).__init__(*args)#继承按钮类的属性
        self.setFont(QtGui.QFont("Webdings")) # 特殊字体以不借助图片实现最小化最大化和关闭按钮？
        self.setFixedWidth(40)


class MainUi(QtWidgets.QMainWindow):#   主窗体类
    def __init__(self):  #初始化类
        #super(MainUi, self).__init__()
        super(MainUi, self).__init__(None, QtCore.Qt.FramelessWindowHint)  # 设置为顶级窗口，无边框

        self.init_ui()#调用初始化函数

    def init_ui(self):#初始化函数
        self._padding = 5 # 设置边界（边框？）宽度为5

        self.setMinimumWidth(500)#设置最小宽度
        self.setMouseTracking(True)  # 设置widget鼠标跟踪
        self.initDrag()  # 设置鼠标跟踪判断默认值
        #self.setFixedSize(1024, 700)

        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件（组件？）
        # self.main_widget.setStyleSheet(
        #     '''QWidget{background:#00f0f0;}''')

        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设 置窗口主部件布局为网格布局
        self.main_layout.setSpacing(0)

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout) # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget() # 创建右侧窗体
        self.right_widget.setObjectName('right_widget') #命名
        self.right_layout = QtWidgets.QGridLayout()#创建右侧布局
        #self.right_layout_chi=self.right_layout.addChildLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格，把布局加入窗体中


        self.main_layout.addWidget(self.left_widget, 0, 0, 20, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 20, 18 )  # 右侧部件在第0行第3列，占8行9列
        #self.main_layout.addWidget(self.right_widget, 0, 2, 8, 9, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.setCentralWidget(self.main_widget) # 设置窗口主部件 #主窗体加入到主体里面？，现在上面都没有
        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮
        self.left_logo = QtWidgets.QPushButton("")
        self.left_logo.setIcon(QtGui.QIcon('./ouwailogochang.png'))
        self.left_logo.move(0, 0)  # 标题栏安放到左上角
        self.left_logo.setObjectName('left_logo')  # 标签名称
        self.left_logo.setStyleSheet("QPushButton{border-image: url(./ouwailogochang.png)}"
                                  "QPushButton:hover{border-image: url(./ouwailogochang.png)}"
                                  "QPushButton:pressed{border-image: url(./ouwailogochang.png)}")


        self.left_logo.setMinimumSize(70,40)
        # self.left_logo.setStyleSheet(
        #     '''QToolButton#left_logo{
        #
        #     background:#000000;
        #     border-top:0px solid gray;
        #     border-right:0px solid gray;}
        #     QToolButton#left_logo:hover{background:red;}''')

        self.left_label_1 = QtWidgets.QPushButton("我的信息")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("分诊咨询管理")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("系统管理")
        self.left_label_3.setObjectName('left_label')

        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.comment-o', color='white'), "个人消息")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.bell', color='white'), "系统消息")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.cloud', color='white'), "资讯消息")
        self.left_button_3.setObjectName('left_button')
        ######
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.home', color='white'), "电话网络报单")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.download', color='white'), "客户资料维护")
        self.left_button_5.setObjectName('left_button')
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.heart', color='white'), "分诊接待管理")
        self.left_button_6.setObjectName('left_button')
        self.left_button_6_1 = QtWidgets.QPushButton(qtawesome.icon('fa.heart', color='white'), "医生排班管理")
        self.left_button_6_1.setObjectName('left_button')
        self.left_button_6_2 = QtWidgets.QPushButton(qtawesome.icon('fa.heart', color='white'), "客户投诉管理")
        self.left_button_6_2.setObjectName('left_button')
        #########
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='white'), "系统配置")
        self.left_button_7.setObjectName('left_button')
        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "系统报表")
        self.left_button_8.setObjectName('left_button')
        self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.question', color='white'), "智能统计")
        self.left_button_9.setObjectName('left_button')
        self.left_xxx = QtWidgets.QPushButton(" ")
        self.left_layout.addWidget(self.left_logo, 0, 0, 1, 3)
        # self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        # self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        #此处加入控制大小按钮？
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        #####
        self.left_layout.addWidget(self.left_label_2, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6_1, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6_2, 10, 0, 1, 3)
        ###
        self.left_layout.addWidget(self.left_label_3, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 12, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 13, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_9, 14, 0, 1, 3)

        '''顶部标签模块——排在第一行'''
        self.Label001 = QtWidgets.QLabel()
        self.right_layout.addWidget(self.Label001, 0, 0, 1, 9)  # 把label控件，加入网格布局的第一行，防止下面内容，挡住标题栏

        '''菜单工具栏——排在第二行'''
        self.right_recommend_widget = QtWidgets.QWidget()  # 推荐封面 窗体          #未来将加入第四行
        self.right_recommend_layout = QtWidgets.QHBoxLayout()  # 以前是网格布局 #改为水平网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)  # 窗体设置为水平布局
        self.right_recommend_layout.setContentsMargins(0, 0, 0, 0)
        self.right_recommend_layout.setSpacing(0)
        self.right_recommend_widget.setObjectName('right_recommend_widget')  # 标签名称
        self.right_recommend_widget.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')

        self.recommend_button_1 = QtWidgets.QToolButton()  # 新建按钮部件
        self.recommend_button_1.setText("新增")  # 设置按钮文本
        self.recommend_button_1.setIcon(qtawesome.icon('fa.file-o', color='#6DDF6D'))  # 设置按钮图标
        self.recommend_button_1.setIconSize(QtCore.QSize(30, 30))  # 设置图标大小
        self.recommend_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文
        self.recommend_button_1.clicked.connect(self.recommend_button_1_Clicked)
        #上面是按钮点击事件，槽函数微医class的最下面

        self.recommend_button_2 = QtWidgets.QToolButton()  # 同上
        self.recommend_button_2.setText("保存")
        self.recommend_button_2.setIcon(qtawesome.icon('fa.save', color='#aaaaff'))
        self.recommend_button_2.setIconSize(QtCore.QSize(30, 30))
        self.recommend_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.recommend_button_2.clicked.connect(self.ouwai_tabel_Save)
        self.recommend_button_2.clicked.connect(self.record_refresh)

        self.recommend_button_3 = QtWidgets.QToolButton()  # 同上
        self.recommend_button_3.setText("删除")
        self.recommend_button_3.setIcon(qtawesome.icon('fa.trash', color='#F7D674'))
        self.recommend_button_3.setIconSize(QtCore.QSize(30, 30))
        self.recommend_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.recommend_button_3.clicked.connect(self.record_delete)

        self.recommend_button_4 = QtWidgets.QToolButton()  # 同上
        self.recommend_button_4.setText("接诊")
        self.recommend_button_4.setIcon(qtawesome.icon('fa.user-md', color='#aa00ff'))
        self.recommend_button_4.setIconSize(QtCore.QSize(30, 30))
        self.recommend_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_5 = QtWidgets.QToolButton()  # 同上
        self.recommend_button_5.setText("预约")
        self.recommend_button_5.setIcon(qtawesome.icon('fa.phone-square', color='blue'))
        self.recommend_button_5.setIconSize(QtCore.QSize(30, 30))
        self.recommend_button_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_7 = QtWidgets.QToolButton()  # 同上
        self.recommend_button_7.setText("刷新")
        self.recommend_button_7.setIcon(qtawesome.icon('fa.refresh', color='green'))
        self.recommend_button_7.setIconSize(QtCore.QSize(30, 30))
        self.recommend_button_7.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.recommend_button_7.clicked.connect(self.record_refresh)

        self.recommend_button_6 = QtWidgets.QToolButton()  # 同上
        self.recommend_button_6.setText("退出")
        self.recommend_button_6.setIcon(qtawesome.icon('fa.sign-out', color='grea'))
        self.recommend_button_6.setIconSize(QtCore.QSize(30, 30))
        self.recommend_button_6.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        '''垂直分割线'''

        self.line1 = QtWidgets.QFrame()  # 3.在布局窗口创建垂直分割线1
        self.line1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line")

        self.line2 = QtWidgets.QFrame()  # 3.在布局窗口创建垂直分割线1
        self.line2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line")

        self.line3 = QtWidgets.QFrame()  # 3.在布局窗口创建垂直分割线1
        self.line3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line3.setObjectName("line")

        self.line4 = QtWidgets.QFrame()  # 3.在布局窗口创建垂直分割线1
        self.line4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line4.setObjectName("line")

        self.line5 = QtWidgets.QFrame()  # 3.在布局窗口创建垂直分割线1
        self.line5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line5.setObjectName("line")

        self.line6 = QtWidgets.QFrame()  # 3.在布局窗口创建垂直分割线1
        self.line6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line6.setObjectName("line")
        '''按钮和分割线 加入水平布局'''
        self.right_recommend_layout.addWidget(self.recommend_button_1)  # 向“推荐专辑”网格布局中加入按钮
        self.right_recommend_layout.addWidget(self.line1)  # 3.1垂直分割线加入加入布局
        self.right_recommend_layout.addWidget(self.recommend_button_2)
        self.right_recommend_layout.addWidget(self.line2)  # 3.1垂直分割线加入加入布局
        self.right_recommend_layout.addWidget(self.recommend_button_3)
        self.right_recommend_layout.addWidget(self.line3)  # 3.1垂直分割线加入加入布局
        self.right_recommend_layout.addWidget(self.recommend_button_4)
        self.right_recommend_layout.addWidget(self.line4)  # 3.1垂直分割线加入加入布局
        self.right_recommend_layout.addWidget(self.recommend_button_5)
        self.right_recommend_layout.addWidget(self.line5)  # 3.1垂直分割线加入加入布局
        self.right_recommend_layout.addWidget(self.recommend_button_7)
        self.right_recommend_layout.addWidget(self.line6)  # 3.1垂直分割线加入加入布局
        self.right_recommend_layout.addWidget(self.recommend_button_6)
        spacer001 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.right_recommend_layout.addItem(spacer001)  # 记住这里是用addItem，，，不是用addWidget
        '''弹簧排在第二行'''
        self.right_layout.addWidget(self.right_recommend_widget, 1, 0, 1, 9,QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)  # 装入网格布局
        '''一号水平线——排在第三行'''
        '''水平水平分割线'''

        self.vline1 = QtWidgets.QFrame()  # 3.在布局窗口创建垂直分割线1
        self.vline1.setFrameShape(QtWidgets.QFrame.HLine)
        self.vline1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vline1.setObjectName("line")

        self.vline2 = QtWidgets.QFrame()  # 3.在布局窗口创建垂直分割线1
        self.vline2.setFrameShape(QtWidgets.QFrame.HLine)
        self.vline2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vline2.setObjectName("line")

        self.vline3 = QtWidgets.QFrame()  # 3.在布局窗口创建垂直分割线1
        self.vline3.setFrameShape(QtWidgets.QFrame.HLine)
        self.vline3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vline3.setObjectName("line")

        self.vline4 = QtWidgets.QFrame()  # 3.在布局窗口创建垂直分割线1
        self.vline4.setFrameShape(QtWidgets.QFrame.HLine)
        self.vline4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vline4.setObjectName("line")

        self.vline5 = QtWidgets.QFrame()  # 3.在布局窗口创建垂直分割线1
        self.vline5.setFrameShape(QtWidgets.QFrame.HLine)
        self.vline5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vline5.setObjectName("line")
        '''排在第三行'''
        self.right_layout.addWidget(self.vline1, 2, 0, 1, 9)
        '''欧外搜索模块——排在第四行'''
        self.right_search_widget=QtWidgets.QWidget()
        self.right_search_layout=QtWidgets.QGridLayout()
        self.right_search_widget.setLayout(self.right_search_layout)
        self.right_search_layout.setContentsMargins(0, 0, 0, 0)#设置页边距为0
        self.right_search_layout.setSpacing(0)                 #设置控件间隔为0

        self.label_01=  QtWidgets.QLabel("受理日期")
        self.label_01.setObjectName("label_search")
        self.label_02 = QtWidgets.QLabel("预约日期")
        self.label_02.setObjectName("label_search")
        self.label_03 = QtWidgets.QLabel("到诊日期")
        self.label_03.setObjectName("label_search")
        self.label_04 = QtWidgets.QLabel("登记日期")
        self.label_04.setObjectName("label_search")
        self.label_05 = QtWidgets.QLabel("至")
        self.label_05.setObjectName("label_search")
        self.label_06 = QtWidgets.QLabel("至")
        self.label_06.setObjectName("label_search")
        self.label_07 = QtWidgets.QLabel("至")
        self.label_07.setObjectName("label_search")
        self.label_08 = QtWidgets.QLabel("至")
        self.label_08.setObjectName("label_search")
        self.label_09 = QtWidgets.QLabel("受理人员")
        self.label_09.setObjectName("label_search")
        self.label_10 = QtWidgets.QLabel("客户卡号")
        self.label_10.setObjectName("label_search")
        self.label_11 = QtWidgets.QLabel("受理电话")
        self.label_11.setObjectName("label_search")
        self.label_12 = QtWidgets.QLabel("开发人员")
        self.label_12.setObjectName("label_search")
        self.label_13 = QtWidgets.QLabel("部门")
        self.label_13.setObjectName("label_search")
        self.label_14 = QtWidgets.QLabel("姓名")
        self.label_14.setObjectName("label_search")
        self.label_15 = QtWidgets.QLabel("咨询项目")
        self.label_15.setObjectName("label_search")
        self.label_16 = QtWidgets.QLabel("受理内容")
        self.label_16.setObjectName("label_search")
        self.label_17 = QtWidgets.QLabel("受理类型")
        self.label_17.setObjectName("label_search")
        self.label_18 = QtWidgets.QLabel("开发渠道")
        self.label_18.setObjectName("label_search")
        self.label_19 = QtWidgets.QLabel("受理工具")
        self.label_19.setObjectName("label_search")
        self.label_20 = QtWidgets.QLabel("信息来源")
        self.label_20.setObjectName("label_search")
        self.label_21 = QtWidgets.QLabel("客户状态")
        self.label_21.setObjectName("label_search")
        self.label_22 = QtWidgets.QLabel("渠道名称")
        self.label_22.setObjectName("label_search")
        self.label_23 = QtWidgets.QLabel("状态")
        self.label_23.setObjectName("label_search")
        self.label_24 = QtWidgets.QLabel("QQ")
        self.label_24.setObjectName("label_search")
        self.comboBox_01 = QtWidgets.QComboBox()
        self.comboBox_01.setObjectName("comboBox_search")
        self.comboBox_02 = QtWidgets.QComboBox()
        self.comboBox_02.setObjectName("comboBox_search")
        self.comboBox_03 = QtWidgets.QComboBox()
        self.comboBox_03.setObjectName("comboBox_search")
        self.comboBox_04 = QtWidgets.QComboBox()
        self.comboBox_04.setObjectName("comboBox_search")
        self.comboBox_05 = QtWidgets.QComboBox()
        self.comboBox_05.setObjectName("comboBox_search")
        self.comboBox_06 = QtWidgets.QComboBox()
        self.comboBox_06.setObjectName("comboBox_search")
        self.comboBox_07 = QtWidgets.QComboBox()
        self.comboBox_07.setObjectName("comboBox_search")
        self.comboBox_08 = QtWidgets.QComboBox()
        self.comboBox_08.setObjectName("comboBox_search")
        self.comboBox_09 = QtWidgets.QComboBox()
        self.comboBox_09.setObjectName("comboBox_search")
        self.comboBox_10 = QtWidgets.QComboBox()
        self.comboBox_10.setObjectName("comboBox_search")
        self.comboBox_11 = QtWidgets.QComboBox()
        self.comboBox_11.setObjectName("comboBox_search")
        self.comboBox_12 = QtWidgets.QComboBox()
        self.comboBox_12.setObjectName("comboBox_search")
        self.comboBox_13 = QtWidgets.QComboBox()
        self.comboBox_13.setObjectName("comboBox_search")
        self.comboBox_14 = QtWidgets.QComboBox()
        self.comboBox_14.setObjectName("comboBox_search")
        self.comboBox_15 = QtWidgets.QComboBox()
        self.comboBox_15.setObjectName("comboBox_search")
        self.comboBox_16 = QtWidgets.QComboBox()
        self.comboBox_16.setObjectName("comboBox_search")
        self.comboBox_17 = QtWidgets.QComboBox()
        self.comboBox_17.setObjectName("comboBox_search")
        self.comboBox_18 = QtWidgets.QComboBox()
        self.comboBox_18.setObjectName("comboBox_search")
        self.comboBox_19 = QtWidgets.QComboBox()
        self.comboBox_19.setObjectName("comboBox_search")
        self.comboBox_20 = QtWidgets.QComboBox()
        self.comboBox_20.setObjectName("comboBox_search")
        self.comboBox_21 = QtWidgets.QComboBox()
        self.comboBox_21.setObjectName("comboBox_search")
        self.comboBox_22 = QtWidgets.QComboBox()
        self.comboBox_22.setObjectName("comboBox_search")
        self.comboBox_23 = QtWidgets.QComboBox()
        self.comboBox_23.setObjectName("comboBox_search")
        self.comboBox_24 = QtWidgets.QComboBox()
        self.comboBox_24.setObjectName("comboBox_search")


        self.right_search_layout.addWidget(self.label_01, 0, 0, 1, 1)
        self.right_search_layout.addWidget(self.label_02, 1, 0, 1, 1)
        self.right_search_layout.addWidget(self.label_03, 2, 0, 1, 1)
        self.right_search_layout.addWidget(self.label_04, 3, 0, 1, 1)
        self.right_search_layout.addWidget(self.label_05, 0, 2, 1, 1)
        self.right_search_layout.addWidget(self.label_06, 1, 2, 1, 1)
        self.right_search_layout.addWidget(self.label_07, 2, 2, 1, 1)
        self.right_search_layout.addWidget(self.label_08, 3, 2, 1, 1)
        self.right_search_layout.addWidget(self.label_09, 0, 4, 1, 1)
        self.right_search_layout.addWidget(self.label_10, 1, 4, 1, 1)
        self.right_search_layout.addWidget(self.label_11, 2, 4, 1, 1)
        self.right_search_layout.addWidget(self.label_12, 3, 4, 1, 1)
        self.right_search_layout.addWidget(self.label_13, 0, 6, 1, 1)
        self.right_search_layout.addWidget(self.label_14, 1, 6, 1, 1)
        self.right_search_layout.addWidget(self.label_15, 2, 6, 1, 1)
        self.right_search_layout.addWidget(self.label_16, 3, 6, 1, 1)
        self.right_search_layout.addWidget(self.label_17, 0, 8, 1, 1)
        self.right_search_layout.addWidget(self.label_18, 1, 8, 1, 1)
        self.right_search_layout.addWidget(self.label_19, 2, 8, 1, 1)
        self.right_search_layout.addWidget(self.label_20, 3, 8, 1, 1)
        self.right_search_layout.addWidget(self.label_21, 0, 10, 1, 1)
        self.right_search_layout.addWidget(self.label_22, 1, 10, 1, 1)
        self.right_search_layout.addWidget(self.label_23, 2, 10, 1, 1)
        self.right_search_layout.addWidget(self.label_24, 3, 10, 1, 1)

        self.right_search_layout.addWidget(self.comboBox_01, 0, 1, 1, 1)
        self.right_search_layout.addWidget(self.comboBox_02, 1, 1, 1, 1)
        self.right_search_layout.addWidget(self.comboBox_03, 2, 1, 1, 1)
        self.right_search_layout.addWidget(self.comboBox_04, 3, 1, 1, 1)
        self.right_search_layout.addWidget(self.comboBox_05, 0, 3, 1, 1)
        self.right_search_layout.addWidget(self.comboBox_06, 1, 3, 1, 1)
        self.right_search_layout.addWidget(self.comboBox_07, 2, 3, 1, 1)
        self.right_search_layout.addWidget(self.comboBox_08, 3, 3, 1, 1)
        self.right_search_layout.addWidget(self.comboBox_09, 0, 5, 1, 1)
        self.right_search_layout.addWidget(self.comboBox_10, 1, 5, 1, 1)
        self.right_search_layout.addWidget(self.comboBox_11, 2, 5, 1, 1)
        self.right_search_layout.addWidget(self.comboBox_12, 3, 5, 1, 1)
        self.right_search_layout.addWidget(self.comboBox_13, 0, 7, 1, 1)
        self.right_search_layout.addWidget(self.comboBox_14, 1, 7, 1, 1)
        self.right_search_layout.addWidget(self.comboBox_15, 2, 7, 1, 1)
        self.right_search_layout.addWidget(self.comboBox_16, 3, 7, 1, 1)
        self.right_search_layout.addWidget(self.comboBox_17, 0, 9, 1, 1)
        self.right_search_layout.addWidget(self.comboBox_18, 1, 9, 1, 1)
        self.right_search_layout.addWidget(self.comboBox_19, 2, 9, 1, 1)
        self.right_search_layout.addWidget(self.comboBox_20, 3, 9, 1, 1)
        self.right_search_layout.addWidget(self.comboBox_21, 0, 11, 1, 1)
        self.right_search_layout.addWidget(self.comboBox_22, 1, 11, 1, 1)
        self.right_search_layout.addWidget(self.comboBox_23, 2, 11, 1, 1)
        self.right_search_layout.addWidget(self.comboBox_24, 3, 11, 1, 1)
        self.clear_search_widget=QtWidgets.QWidget()  #在搜索右侧放置搜索清除按钮 垂直布局
        self.clear_search_layout=QtWidgets.QVBoxLayout()
        self.clear_search_widget.setLayout(self.clear_search_layout)
        self.clear_search_layout.setContentsMargins(0, 0, 0, 0)  # 设置页边距为0
        self.clear_search_layout.setSpacing(0)  # 设置控件间隔为0
        self.button_clear=QtWidgets.QToolButton()
        self.button_clear.setText("清除")
        self.button_clear.setIcon(qtawesome.icon('fa.eraser', color='green'))
        self.button_clear.setIconSize(QtCore.QSize(30, 30))
        self.button_clear.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.button_search = QtWidgets.QToolButton()
        self.button_search.setText("搜索")
        self.button_search.setIcon(qtawesome.icon('fa.search', color='green'))
        self.button_search.setIconSize(QtCore.QSize(30, 30))
        self.button_search.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.clear_search_layout.addWidget(self.button_clear,0)
        self.clear_search_layout.addWidget(self.button_search, 1)
        self.right_search_layout.addWidget(self.clear_search_widget,0, 12, 4, 1)
        '''排在第四行'''
        self.right_layout.addWidget(self.right_search_widget, 3, 0, 1, 9, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.right_search_widget.setStyleSheet('''
                    QLabel#label_search{border:1px;color:gray;}
                    QComboBox#comboBox_search{
                        border:1px solid gray;
                        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                        QComboBox::drop-down {
                        subcontrol-origin:paddind;  
                        subcontrol-position: top right;
                        width: 15px;
 
                        border-left-width: 1px;
                        border-left-color: darkgray;
                        border-left-style: solid; /* just a single line */
                        border-top-right-radius: 3px; /* same radius as the QComboBox */
                        border-bottom-right-radius: 3px;
 }
                    QWidget#left_widget{
                        background:white;
                        border-top:1px solid gray;
                        border-bottom:1px solid gray;
                        border-left:1px solid gray;
                        border-top-left-radius:0px;
                        border-radius:0px;
                    }
                ''')

        '''欧外搜索模块'''

        '''二号水平线——排在第五行'''
        '''水平水平分割线'''



        self.vline2 = QtWidgets.QFrame()  # 3.在布局窗口创建垂直分割线1
        self.vline2.setFrameShape(QtWidgets.QFrame.HLine)
        self.vline2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vline2.setObjectName("line")


        '''二号水平线排在第五行'''
        self.right_layout.addWidget(self.vline2, 4, 0, 1, 9)
        '''欧外表格——排在低6行'''
        self.ouwai_tabel_widget = QtWidgets.QWidget() #创建部件
        # self.ouwai_tabel_widget.setFixedSize(1500, 200)
        self.ouwai_tabel_widget.setMinimumSize(1200,260)
        self.ouwai_tabel_widget_layout=QtWidgets.QHBoxLayout()
        self.ouwai_tabel_widget.setLayout(self.ouwai_tabel_widget_layout)
        self.ouwai_tabel= MainWinui_ouwai_tabel.ouwai_table()#在部件中创建表格 #这是从外部引入的模块
        self.ouwai_tabel_widget_layout.addWidget(self.ouwai_tabel)
        self.ouwai_tabel_widget_layout.setContentsMargins(0, 0, 0, 0)  # 设置页边距为0
        self.ouwai_tabel_widget_layout.setSpacing(0)  # 设置控件间隔为0
        self.ouwai_tabel.clicked.connect(self.ouwai_tabel_Clicked)    #点击事件

        self.right_layout.addWidget(self.ouwai_tabel_widget, 5, 0, 1, 9) #表格加入布局

        '''单个推荐标签模块——排在第7行'''
        self.right_recommend_label = QtWidgets.QLabel("...")  # 未来将加入到第三行
        self.right_recommend_label.setObjectName('right_lable')
        self.right_layout.addWidget(self.right_recommend_label, 6, 0, 1, 9)
        '''选项卡布局——排在低8行'''
        self.ouwai_tab_widget=QtWidgets.QWidget()  #创建部件
        self.ouwai_tab_widget.setMinimumSize(1000,300) #设置大小
        self.ouwai_tab_widget_layout=QtWidgets.QHBoxLayout()#创建布局
        self.ouwai_tab_widget.setLayout(self.ouwai_tab_widget_layout)#设置布局
        self.ouwai_tab=MainWinui_ouwai_tab_widget.ouwai_table_tab_widget()#创建表格
        self.ouwai_tab_widget_layout.addWidget(self.ouwai_tab)#表格加入布局
        self.ouwai_tab_widget_layout.setContentsMargins(0,0,0,0)#设置页边距
        self.ouwai_tab_widget_layout.setSpacing(0)#设置控件间距
        self.right_layout.addWidget(self.ouwai_tab_widget,7, 0, 1,6)#加入总布局

        """设置关闭大小按钮"""
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
            QWidget#left_widget{
                background:gray;
                border-top:1px solid gray;
                border-bottom:1px solid gray;
                border-left:1px solid gray;
                border-top-left-radius:0px;
                border-bottom-left-radius:0px;
            }
        ''')

        # self.right_bar_widget_search_input.setStyleSheet(
        #     '''QLineEdit{
        #             border:1px solid gray;
        #             width:300px;
        #             border-radius:10px;
        #             padding:2px 4px;
        #     }''')
        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:0px;
                border-bottom-right-radius:0px;
            }
            QLabel#right_lable{
                border:none;
                font-size:10px;
                
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        # self.right_playlist_widget.setStyleSheet(
        #     '''
        #         QToolButton{border:none;}
        #         QToolButton:hover{border-bottom:2px solid #F76677;}
        #     ''')
        # self.right_newsong_widget.setStyleSheet('''
        #     QPushButton{
        #         border:none;
        #         color:gray;
        #         font-size:12px;
        #         height:40px;
        #         padding-left:5px;
        #         padding-right:10px;
        #         text-align:left;
        #     }
        #     QPushButton:hover{
        #         color:black;
        #         border:1px solid #F3F3F5;
        #         border-radius:10px;
        #         background:LightGray;
        #     }
        # ''')
        # self.right_process_bar.setStyleSheet('''
        #     QProgressBar::chunk {
        #         background-color: #F76677;
        #     }
        # ''')
        #
        # self.right_playconsole_widget.setStyleSheet('''
        #     QPushButton{
        #         border:none;
        #     }
        # ''')
        #self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.main_layout.setSpacing(0)


        # 这里设置容器内顶部标签
        """这里是在right_widget里面创建标签，而且这个标签是用非原生类创建的"""
        self._TitleLabel = QTitleLabel(self.right_widget)
        self._TitleLabel.setMouseTracking(True)  # 设置标题栏标签鼠标跟踪（如不设，则标题栏内在widget上层，无法实现跟踪）
        self._TitleLabel.setIndent(40)  # 设置标题栏文本缩进，距离左边框的距离
        self._TitleLabel.move(0, 0)  # 标题栏安放到左上角
        self._TitleLabel.setObjectName('right_lable')  # 标签名称
        # self._TitleLabel.setFixedSize(50,50)
        #self._TitleLabel.setPixmap(QtGui.QPixmap('001.png'))
        self._TitleLabel.setText("欧外健康云平")

        #self._TitleLabel.setText("<font color=%s>%s</font>" % ('#8968CD', "平凡之路"))
        #self._TitleLabel.setPixmap(QtGui.QPixmap('001.png'))
        self._TitleLabel.setStyleSheet('''
            QTitleLabel{
                background:#f5f5f5;
                color:#797979;
                font-size:15px;
                font-weight:bold;
                font-family:Roman times;
                border-top:1px solid gray;
                border-right:1px solid gray;
            }
            QTitleLabel#right_lable:hover{background:#f5f5f5;}
        ''')# 标签设置为红色？




        """这里是在左上角面创建图标，"""
        """这里是在左上角面创建图标，"""
        self.button_logo = QtWidgets.QToolButton(self.right_widget)
        #self.button_logo.setText("不需要歌词,也可以打动你的心")
        self.button_logo.setIcon(QtGui.QIcon(qtawesome.icon('fa.opera', color='#F76677')))
        self.button_logo.setIconSize(QtCore.QSize(20, 20))
        self.button_logo.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        # op = QtWidgets.QGraphicsOpacityEffect()# 设置透明度的值，0.0到1.0，最小值0是透明，1是不透明
        # op.setOpacity(0)
        # self.button_logo.setGraphicsEffect(op)
        #self._buton = QTitleLabel(self.right_widget)
        self.button_logo.setMouseTracking(True)  # 设置标题栏标签鼠标跟踪（如不设，则标题栏内在widget上层，无法实现跟踪）
        self.button_logo.move(0, 0)  # 标题栏安放到左上角
        self.button_logo.setObjectName('button_logo')  # 标签名称
        self.button_logo.setFixedSize(30, 30)  # 设置大小
        self.button_logo.setStyleSheet(
            '''QToolButton#button_logo{
            background: transparent;
            border-top:0px solid gray;
            border-right:0px solid gray;}
            QToolButton#button_logo:hover{background:red;}''')
        # self._TitleLabel.setStyleSheet('''
        #     QTitleLabel{
        #         background:#f5f5f5;
        #         color:rgb(200,100,100,250);
        #         font-size:25px;
        #         font-weight:bold;
        #         font-family:Roman times;
        #         border-top:1px solid gray;
        #         border-right:1px solid gray;
        #     }
        #     QTitleLabel#right_lable:hover{background:#f5f5f5;}
        # ''')# 标签设置为红色


    # def initTitleLabel(self):
        # 安放标题栏标签
        # self._TitleLabel = QTitleLabel(self)
        # self._TitleLabel.setMouseTracking(True)  # 设置标题栏标签鼠标跟踪（如不设，则标题栏内在widget上层，无法实现跟踪）
        # self._TitleLabel.setIndent(0)  # 设置标题栏文本缩进，距离左边框的距离
        # self._TitleLabel.move(0, 50)  # 标题栏安放到左上角
        # self._TitleLabel.setObjectName('right_lable')  # 标签名称
        # #self._TitleLabel.setFixedSize(50,50)
        # self._TitleLabel.setStyleSheet(
        #     '''QTitleLabel#right_lable{background:#F76677;border-radius:0px;} QTitleLabel#right_lable:hover{background:red;}''')  # 标签设置为红色


    def initDrag(self):
        # 设置鼠标跟踪判断扳机默认值
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False


    def initLayout(self):
        # 设置框架布局
        self._MainLayout = QtWidgets.QVBoxLayout()
        self._MainLayout.setSpacing(0)
        self._MainLayout.addWidget(QtWidgets.QLabel(), QtCore.Qt.AlignLeft)  # 顶一个QLabel在竖放框架第一行，以免正常内容挤占到标题范围里
        self._MainLayout.addStretch()
        self.setLayout(self._MainLayout)

    def addLayout(self, QLayout):
        # 给widget定义一个addLayout函数，以实现往竖放框架的正确内容区内嵌套Layout框架
        self._MainLayout.addLayout(QLayout)

    def _setTitleText(self, func):
        # 设置标题栏标签的装饰器函数
        def wrapper(*args):
            self._TitleLabel.setText(*args)
            return func(*args)

        return wrapper

    def setTitleAlignment(self, alignment):
        # 给widget定义一个setTitleAlignment函数，以实现标题栏标签的对齐方式设定
        self._TitleLabel.setAlignment(alignment | QtCore.Qt.AlignVCenter)

    def setCloseButton(self, bool):
        # 给widget定义一个setCloseButton函数，为True时设置一个关闭按钮
        if bool == True:
            self._CloseButton = QTitleButton(b'\xef\x81\xb2'.decode("utf-8"), self)
            self._CloseButton.setObjectName("CloseButton")  # 设置按钮的ObjectName以在qss样式表内定义不同的按钮样式
            self._CloseButton.setToolTip("关闭窗口")
            self._CloseButton.setMouseTracking(True)  # 设置按钮鼠标跟踪（如不设，则按钮在widget上层，无法实现跟踪）
            self._CloseButton.setFixedHeight(self._TitleLabel.height())  # 设置按钮高度为标题栏高度
            self._CloseButton.clicked.connect(self.close)  # 按钮信号连接到关闭窗口的槽函数

    def setMinMaxButtons(self, bool):
        # 给widget定义一个setMinMaxButtons函数，为True时设置一组最小化最大化按钮
        if bool == True:
            self._MinimumButton = QTitleButton(b'\xef\x80\xb0'.decode("utf-8"), self)
            self._MinimumButton.setObjectName("MinMaxButton")  # 设置按钮的ObjectName以在qss样式表内定义不同的按钮样式
            self._MinimumButton.setToolTip("最小化")
            self._MinimumButton.setMouseTracking(True)  # 设置按钮鼠标跟踪（如不设，则按钮在widget上层，无法实现跟踪）
            self._MinimumButton.setFixedHeight(self._TitleLabel.height())  # 设置按钮高度为标题栏高度
            self._MinimumButton.clicked.connect(self.showMinimized)  # 按钮信号连接到最小化窗口的槽函数
            self._MaximumButton = QTitleButton(b'\xef\x80\xb1'.decode("utf-8"), self)
            self._MaximumButton.setObjectName("MinMaxButton")  # 设置按钮的ObjectName以在qss样式表内定义不同的按钮样式
            self._MaximumButton.setToolTip("最大化")
            self._MaximumButton.setMouseTracking(True)  # 设置按钮鼠标跟踪（如不设，则按钮在widget上层，无法实现跟踪）
            self._MaximumButton.setFixedHeight(self._TitleLabel.height())  # 设置按钮高度为标题栏高度
            self._MaximumButton.clicked.connect(self._changeNormalButton)  # 按钮信号连接切换到恢复窗口大小按钮函数

    def _changeNormalButton(self):
        # 切换到恢复窗口大小按钮
        try:
            self.showMaximized()  # 先实现窗口最大化
            self._MaximumButton.setText(b'\xef\x80\xb2'.decode("utf-8"))  # 更改按钮文本
            self._MaximumButton.setToolTip("恢复")  # 更改按钮提示
            self._MaximumButton.disconnect()  # 断开原本的信号槽连接
            self._MaximumButton.clicked.connect(self._changeMaxButton)  # 重新连接信号和槽
        except:
            pass

    def _changeMaxButton(self):
        # 切换到最大化按钮
        try:
            self.showNormal()
            self._MaximumButton.setText(b'\xef\x80\xb1'.decode("utf-8"))
            self._MaximumButton.setToolTip("最大化")
            self._MaximumButton.disconnect()
            self._MaximumButton.clicked.connect(self._changeNormalButton)
        except:
            pass

    def resizeEvent(self, QResizeEvent):
        # 自定义窗口调整大小事件
        self._TitleLabel.setFixedWidth(self.width())  # 将标题标签始终设为窗口宽度
        # 分别移动三个按钮到正确的位置
        try:
            self._CloseButton.move(self.width() - self._CloseButton.width()-25, 9)
        except:
            pass
        try:
            self._MinimumButton.move(self.width() - (self._CloseButton.width() + 1) * 3 -24, 9)
        except:
            pass
        try:
            self._MaximumButton.move(self.width() - (self._CloseButton.width() + 1) * 2 -24, 9)
        except:
            pass
        # 重新调整边界范围以备实现鼠标拖放缩放窗口大小，采用三个列表生成式生成三个列表
        self._right_rect = [QtCore.QPoint(x, y) for x in range(self.width() - self._padding, self.width() + 1)
                            for y in range(1, self.height() - self._padding)]
        self._bottom_rect = [QtCore.QPoint(x, y) for x in range(1, self.width() - self._padding)
                             for y in range(self.height() - self._padding, self.height() + 1)]
        self._corner_rect = [QtCore.QPoint(x, y) for x in range(self.width() - self._padding, self.width() + 1)
                             for y in range(self.height() - self._padding, self.height() + 1)]

    def mousePressEvent(self, event):
        # 重写鼠标点击的事件
        if (event.button() == QtCore.Qt.LeftButton) and (event.pos() in self._corner_rect):
            # 鼠标左键点击右下角边界区域
            self._corner_drag = True
            event.accept()
        elif (event.button() == QtCore.Qt.LeftButton) and (event.pos() in self._right_rect):
            # 鼠标左键点击右侧边界区域
            self._right_drag = True
            event.accept()
        elif (event.button() == QtCore.Qt.LeftButton) and (event.pos() in self._bottom_rect):
            # 鼠标左键点击下侧边界区域
            self._bottom_drag = True
            event.accept()
        elif (event.button() == QtCore.Qt.LeftButton) and (event.y() < self._TitleLabel.height()):
            # 鼠标左键点击标题栏区域
            self._move_drag = True
            self.move_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        # 判断鼠标位置切换鼠标手势
        if QMouseEvent.pos() in self._corner_rect:
            self.setCursor(QtCore.Qt.SizeFDiagCursor)
        elif QMouseEvent.pos() in self._bottom_rect:
            self.setCursor(QtCore.Qt.SizeVerCursor)
        elif QMouseEvent.pos() in self._right_rect:
            self.setCursor(QtCore.Qt.SizeHorCursor)
        else:
            self.setCursor(QtCore.Qt.ArrowCursor)
        # 当鼠标左键点击不放及满足点击区域的要求后，分别实现不同的窗口调整
        # 没有定义左方和上方相关的5个方向，主要是因为实现起来不难，但是效果很差，拖放的时候窗口闪烁，再研究研究是否有更好的实现
        if QtCore.Qt.LeftButton and self._right_drag:
            # 右侧调整窗口宽度
            self.resize(QMouseEvent.pos().x(), self.height())
            QMouseEvent.accept()
        elif QtCore.Qt.LeftButton and self._bottom_drag:
            # 下侧调整窗口高度
            self.resize(self.width(), QMouseEvent.pos().y())
            QMouseEvent.accept()
        elif QtCore.Qt.LeftButton and self._corner_drag:
            # 右下角同时调整高度和宽度
            self.resize(QMouseEvent.pos().x(), QMouseEvent.pos().y())
            QMouseEvent.accept()
        elif QtCore.Qt.LeftButton and self._move_drag:
            # 标题栏拖放窗口位置
            self.move(QMouseEvent.globalPos() - self.move_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        # 鼠标释放后，各扳机复位
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False
    def recommend_button_1_Clicked(self):  #跳转窗口
        print("被点击啦")
        form_add= QtWidgets.QDialog()
        ui = MainWinui_ouwai_add.Ui_Dialog()
        ui.setupUi(form_add)
        form_add.show()
        form_add.exec_()
        self.show()

    def record_delete(self):  #删除按钮点击事件
        row_2 = self.ouwai_tabel.currentRow()
        if row_2 == -1:
            reply2 = QtWidgets.QMessageBox.question(self, 'Message', '请先选择被删除项目',
                                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                    QtWidgets.QMessageBox.No)
        # # 是否删除的对话框
        else:
            reply = QtWidgets.QMessageBox.question(self, 'Message', 'Are you sure to delete it ?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                #当前行
                print(self.ouwai_tabel.currentRow())
                row_2 = self.ouwai_tabel.currentRow()
                del_d = self.ouwai_tabel.item(row_2, 0).text()
                # print(row_2)
                # print(type(del_d))
                db = pymysql.connect("116.62.199.133", "root", "321456", "ouwai", charset='utf8')
                # 获取游标、数据
                cur = db.cursor()  # 获取游标
                #在数据库删除数据
                sql = 'DELETE FROM patient_record WHERE id =%s;'
                #sql = 'select * FROM patient_record;'
                cur.execute(sql,[del_d])  # 执行sql语句，返回sql影响成功的行数
                db.commit()
                cur.close()
                db.close()
                self.show()
                # 删除表格
                self.ouwai_tabel.removeRow(row_2)
#表格点击事件

    def ouwai_tabel_Clicked(self):  # 点击表格自动在tab1里面显示记录详细内容
        row_2 = self.ouwai_tabel.currentRow()
        if row_2 == -1:
            pass
        else:

            # 当前行
            print("当前行数",self.ouwai_tabel.currentRow())
            row_2 = self.ouwai_tabel.currentRow()
            del_d = self.ouwai_tabel.item(row_2, 0).text()
            global_id=del_d

            print("当前id",del_d)
            db = pymysql.connect("116.62.199.133", "root", "321456", "ouwai", charset='utf8')
            # 获取游标、数据
            cur = db.cursor()  # 获取游标
            # 在数据库删除数据
            sql = 'select * FROM patient_record WHERE id =%s;'
            # sql = 'select * FROM patient_record;'
            cur.execute(sql, [del_d])  # 执行sql语句，返回sql影响成功的行数
            data = cur.fetchall()
            print(data[0][2])
            print(type(data[0][7]))
            print(data[0][8])
            if data[0][1]=="在院":
                state_index=0
            elif data[0][1]=="出院":
                state_index = 1
            elif data[0][1]=="其他":
                state_index = 2
            if data[0][3]=="男":
                gender_index=0
            elif data[0][3]=="女":
                gender_index = 1
            elif data[0][3]=="其他":
                gender_index = 2
            print("数据库中id",data[0][0])
            self.ouwai_tab.lineEdit_id.setText(str(data[0][0]))   #必须用字符串形式，整数不行
            self.ouwai_tab.comboBox.setCurrentIndex(state_index)   #设置内容
            self.ouwai_tab.lineEdit.setText(data[0][2])  # 下面是通过查询表格--设置控件内容
            self.ouwai_tab.comboBox_2.setCurrentIndex(gender_index)

            self.ouwai_tab.lineEdit_2.setText(data[0][4])

            self.ouwai_tab.textEdit.setPlainText(data[0][5])
            self.ouwai_tab.lineEdit_4.setText(data[0][6])
            self.ouwai_tab.lineEdit_5.setText(str(data[0][7]))
            self.ouwai_tab.dateTimeEdit.setDateTime(data[0][8])
            self.ouwai_tab.lineEdit_6.setText(data[0][9])
            self.ouwai_tab.lineEdit_7.setText(data[0][10])
            self.ouwai_tab.lineEdit_8.setText(data[0][11])
            self.ouwai_tab.lineEdit_9.setText(data[0][12])
            self.ouwai_tab.lineEdit_10.setText(data[0][13])
            print(data)
            db.commit()
            cur.close()
            db.close()
            self.show()

    def ouwai_tabel_Save(self):
        id=self.ouwai_tab.lineEdit_id.text()
        state = self.ouwai_tab.comboBox.currentText()  # 下面是读取各个空间中的值
        name01 = self.ouwai_tab.lineEdit.text()

        print("当前姓名",name01)
        gender = self.ouwai_tab.comboBox_2.currentText()
        age = self.ouwai_tab.lineEdit_2.text()
        case_summary = self.ouwai_tab.textEdit.toPlainText()
        inspection_data = self.ouwai_tab.lineEdit_4.text()
        cost = self.ouwai_tab.lineEdit_5.text()
        if len(cost) == 0:
            cost = 0
        accept_date = self.ouwai_tab.dateTimeEdit.dateTime().toString(QtCore.Qt.ISODate)  # 获取时间编辑框里面的内容
        print(accept_date)
        # print(accept_date.toString(QtCore.Qt.ISODate))
        contact_information = self.ouwai_tab.lineEdit_6.text()
        attending_doctor = self.ouwai_tab.lineEdit_7.text()
        company = self.ouwai_tab.lineEdit_8.text()
        complaint = self.ouwai_tab.lineEdit_9.text()
        remarks = self.ouwai_tab.lineEdit_10.text()

        # state, name01, gender, age, case_summary,inspection_data, cost,accept_date, contact_information, attending_doctor, company, complaint,remarks))
        # state, name01, gender, str(age), case_summary,inspection_data, str(cost),accept_date, contact_information, attending_doctor, company, complaint,remarks))
        #sql = 'insert into patient_record(state, name01, gender, age, case_summary,inspection_data,cost,accept_date, contact_information, attending_doctor, company, complaint,remarks) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        sql = 'update patient_record set state=%s, name01=%s, gender=%s, age=%s, case_summary=%s,inspection_data=%s,cost=%s,accept_date=%s, contact_information=%s, attending_doctor=%s, company=%s, complaint=%s,remarks=%s where id =%s;'

        if len(name01) == 0:
            print("姓名不能为空")

        else:
            db = pymysql.connect("116.62.199.133", "root", "321456", "ouwai", charset='utf8')
            # 获取游标、数据
            cur = db.cursor()  # 获取游标

            res = cur.execute(sql, [state, name01, gender, age, case_summary, inspection_data, cost, accept_date,
                                    contact_information, attending_doctor, company, complaint,
                                    remarks,id])  # 执行sql语句，返回sql影响成功的行数
            db.commit()
            cur.close()
            db.close()
            self.ouwai_tab.lineEdit.setText(None)  # 下面是初始化控件内容
            self.ouwai_tab.lineEdit_2.setText(None)
            self.ouwai_tab.textEdit.setPlainText(None)
            self.ouwai_tab.lineEdit_4.setText(None)
            self.ouwai_tab.lineEdit_5.setText(None)
            self.ouwai_tab.lineEdit_6.setText(None)
            self.ouwai_tab.lineEdit_7.setText(None)
            self.ouwai_tab.lineEdit_8.setText(None)
            self.ouwai_tab.lineEdit_9.setText(None)
            self.ouwai_tab.lineEdit_10.setText(None)
    def record_refresh(self):
        self.ouwai_tabel.creat_table_view()










def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open("./UnFrameStyle.qss").read()) #读取css样式文件
    gui = MainUi()
    gui.setMinMaxButtons(True)
    gui.setCloseButton(True)
    gui.show()
    sys.exit(app.exec_())

#class ouwai_tabel():


if __name__ == '__main__':
    main()




