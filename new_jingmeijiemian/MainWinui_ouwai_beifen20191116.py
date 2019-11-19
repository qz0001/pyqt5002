#__author__:"wanghui"

from PyQt5 import QtCore,QtGui,QtWidgets

import sys
import qtawesome
class QTitleLabel(QtWidgets.QLabel):
    """
    新建标题栏标签类
    """
    def __init__(self, *args):
        super(QTitleLabel, self).__init__(*args)
        self.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.setFixedHeight(30)

class QTitleButton(QtWidgets.QPushButton):
    """
    新建标题栏按钮类
    """
    def __init__(self, *args):
        super(QTitleButton, self).__init__(*args)
        self.setFont(QtGui.QFont("Webdings")) # 特殊字体以不借助图片实现最小化最大化和关闭按钮
        self.setFixedWidth(40)


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        #super(MainUi, self).__init__()
        super(MainUi, self).__init__(None, QtCore.Qt.FramelessWindowHint)  # 设置为顶级窗口，无边框

        self.init_ui()

    def init_ui(self):
        self._padding = 5 # 设置边界宽度为5
        self.setMinimumWidth(500)
        self.setMouseTracking(True)  # 设置widget鼠标跟踪
        self.initDrag()  # 设置鼠标跟踪判断默认值
        #self.setFixedSize(1024, 700)

        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件

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
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格，把布局加入窗体中



        self.main_layout.addWidget(self.left_widget,0,0,20,2) # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget,0,2,20,18) # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget) # 设置窗口主部件 #主窗体加入到主体里面？，现在上面都没有
        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

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
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
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
        self.right_bar_widget = QtWidgets.QWidget()  # 右侧顶部搜索框部件

        self.right_bar_layout = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget.setLayout(self.right_bar_layout) #网格布局加入到右侧窗体中
        self.search_icon = QtWidgets.QLabel(chr(0xf002) + ' ' + '搜索  ')
        self.search_icon.setFont(qtawesome.font('fa', 16))
        self.right_bar_widget_search_input = QtWidgets.QLineEdit()
        self.right_bar_widget_search_input.setPlaceholderText("输入歌手、歌曲或用户，回车进行搜索")
        self.right_bar_layout.addWidget(self.search_icon, 1, 0, 1, 1)
        self.right_bar_layout.addWidget(self.right_bar_widget_search_input, 1, 1, 1, 8)
        self.Label001=QtWidgets.QLabel()
        self.right_layout.addWidget(self.Label001, 0, 0, 1, 9)     #把label控件，加入网格布局的第一行，防止下面内容，挡住标题栏
        self.right_layout.addWidget(self.right_bar_widget, 1, 0, 1, 9)#把搜索窗体加入网格布局的第二行，占据9行，索索窗体内部用的也是网格布局
        self.right_recommend_label = QtWidgets.QLabel("今日推荐")                 #未来将加入到第三行
        self.right_recommend_label.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  # 推荐封面 窗体          #未来将加入第四行
        self.right_recommend_widget.setObjectName('right_recommend_widget')  # 标签名称
        self.right_recommend_widget.setStyleSheet('''
                    QWidget#right_recommend_widget{
                        background:#000000;
                        border-top:1px solid gray;
                        border-bottom:10px solid gray;
                        border-left:11px solid gray;
                        border-top-left-radius:10px;
                        border-bottom-left-radius:10px;
                    }
                    QWidget#right_recommend_widget:hover{background:#05f5f8;}
                ''')  # 标签设置为红色
        #self.right_recommend_widget.setStyleSheet('''{background-color:#ffffff;}''')
        #self.right_recommend_layout = QtWidgets.QGridLayout()  #                   #建立网格布局
        self.right_recommend_layout = QtWidgets.QHBoxLayout() #                    #改为水平网格布局
        self.right_recommend_layout.setContentsMargins(0,0,0,0)  #好像不行改变背景颜色
        self.right_recommend_widget.setLayout(self.right_recommend_layout)         #网格布局加入窗体

        self.recommend_button_1 = QtWidgets.QToolButton()                          #新建按钮部件
        self.recommend_button_1.setText("新增")                              # 设置按钮文本
        self.recommend_button_1.setIcon(QtGui.QIcon('./r1.png'))                 # 设置按钮图标
        self.recommend_button_1.setIconSize(QtCore.QSize(30, 30))               # 设置图标大小
        self.recommend_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文

        self.recommend_button_2 = QtWidgets.QToolButton()                         #同上
        self.recommend_button_2.setText("保存")
        self.recommend_button_2.setIcon(QtGui.QIcon('./r2.png'))
        self.recommend_button_2.setIconSize(QtCore.QSize(30, 30))
        self.recommend_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_3 = QtWidgets.QToolButton()                      #同上
        self.recommend_button_3.setText("删除")
        self.recommend_button_3.setIcon(QtGui.QIcon('./r3.png'))
        self.recommend_button_3.setIconSize(QtCore.QSize(30, 30))
        self.recommend_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_4 = QtWidgets.QToolButton()                          #同上
        self.recommend_button_4.setText("接诊")
        self.recommend_button_4.setIcon(QtGui.QIcon('./r4.png'))
        self.recommend_button_4.setIconSize(QtCore.QSize(30, 30))
        self.recommend_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_5 = QtWidgets.QToolButton()                        #同上
        self.recommend_button_5.setText("预约")
        self.recommend_button_5.setIcon(QtGui.QIcon('./r5.png'))
        self.recommend_button_5.setIconSize(QtCore.QSize(30, 30))
        self.recommend_button_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.right_recommend_layout.addWidget(self.recommend_button_1,0)         #向“推荐专辑”网格布局中加入按钮
        self.right_recommend_layout.addWidget(self.recommend_button_2,1)
        self.right_recommend_layout.addWidget(self.recommend_button_3,2)
        self.right_recommend_layout.addWidget(self.recommend_button_4,3)
        self.right_recommend_layout.addWidget(self.recommend_button_5,4)
        spacer001 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.right_recommend_layout.addItem(spacer001)#记住这里是用addItem，，，不是用addWidget
        self.right_recommend_layout.setContentsMargins(0, 0, 0,0)
        self.right_recommend_layout.setSpacing(0)

        self.right_layout.addWidget(self.right_recommend_label, 2, 0, 1,60)  #装入网格布局
        self.right_layout.addWidget(self.right_recommend_widget,3, 2, 1,10)  #装入网格布局

        self.right_newsong_lable = QtWidgets.QLabel("最新歌曲")
        self.right_newsong_lable.setObjectName('right_lable')

        self.right_playlist_lable = QtWidgets.QLabel("热门歌单")
        self.right_playlist_lable.setObjectName('right_lable')

        self.right_newsong_widget = QtWidgets.QWidget()  # 最新歌曲部件
        self.right_newsong_layout = QtWidgets.QGridLayout()  # 最新歌曲部件网格布局
        self.right_newsong_widget.setLayout(self.right_newsong_layout)

        self.newsong_button_1 = QtWidgets.QPushButton("夜机      陈慧娴      永远的朋友      03::29")
        self.newsong_button_2 = QtWidgets.QPushButton("夜机      陈慧娴      永远的朋友      03::29")
        self.newsong_button_3 = QtWidgets.QPushButton("夜机      陈慧娴      永远的朋友      03::29")
        self.newsong_button_4 = QtWidgets.QPushButton("夜机      陈慧娴      永远的朋友      03::29")
        self.newsong_button_5 = QtWidgets.QPushButton("夜机      陈慧娴      永远的朋友      03::29")
        self.newsong_button_6 = QtWidgets.QPushButton("夜机      陈慧娴      永远的朋友      03::29")
        self.right_newsong_layout.addWidget(self.newsong_button_1, 0, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_2, 1, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_3, 2, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_4, 3, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_5, 4, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_6, 5, 1, )
        self.right_playlist_widget = QtWidgets.QWidget()  # 播放歌单部件
        self.right_playlist_layout = QtWidgets.QGridLayout()  # 播放歌单网格布局
        self.right_playlist_widget.setLayout(self.right_playlist_layout)

        self.playlist_button_1 = QtWidgets.QToolButton()
        self.playlist_button_1.setText("无法释怀的整天循环音乐…")
        self.playlist_button_1.setIcon(QtGui.QIcon('./p1.jpg'))
        self.playlist_button_1.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.playlist_button_2 = QtWidgets.QToolButton()
        self.playlist_button_2.setText("不需要歌词,也可以打动你的心")
        self.playlist_button_2.setIcon(QtGui.QIcon('./p2.jpg'))
        self.playlist_button_2.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.playlist_button_3 = QtWidgets.QToolButton()
        self.playlist_button_3.setText("那些你熟悉又不知道名字…")
        self.playlist_button_3.setIcon(QtGui.QIcon('./p3.jpg'))
        self.playlist_button_3.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.playlist_button_4 = QtWidgets.QToolButton()
        self.playlist_button_4.setText("那些只听前奏就中毒的英文歌")
        self.playlist_button_4.setIcon(QtGui.QIcon('./p4.jpg'))
        self.playlist_button_4.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.right_playlist_layout.addWidget(self.playlist_button_1, 0, 0)
        self.right_playlist_layout.addWidget(self.playlist_button_2, 0, 1)
        self.right_playlist_layout.addWidget(self.playlist_button_3, 1, 0)
        self.right_playlist_layout.addWidget(self.playlist_button_4, 1, 1)
        self.right_layout.addWidget(self.right_newsong_lable, 5, 0, 1, 5)
        self.right_layout.addWidget(self.right_playlist_lable, 5, 5, 1, 4)
        self.right_layout.addWidget(self.right_newsong_widget, 6, 0, 1, 5)
        self.right_layout.addWidget(self.right_playlist_widget, 6, 5, 1, 4)
        self.right_process_bar = QtWidgets.QProgressBar()  # 播放进度部件
        self.right_process_bar.setValue(49)
        self.right_process_bar.setFixedHeight(3)  # 设置进度条高度
        self.right_process_bar.setTextVisible(False)  # 不显示进度条文字

        self.right_playconsole_widget = QtWidgets.QWidget()  # 播放控制部件
        self.right_playconsole_layout = QtWidgets.QGridLayout()  # 播放控制部件网格布局层
        self.right_playconsole_widget.setLayout(self.right_playconsole_layout)

        self.console_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.backward', color='#F76677'), "")
        self.console_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.forward', color='#F76677'), "")
        self.console_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.pause', color='#F76677', font=18), "")
        self.console_button_3.setIconSize(QtCore.QSize(30, 30))

        self.right_playconsole_layout.addWidget(self.console_button_1, 0, 0)
        self.right_playconsole_layout.addWidget(self.console_button_2, 0, 2)
        self.right_playconsole_layout.addWidget(self.console_button_3, 0, 1)
        self.right_playconsole_layout.setAlignment(QtCore.Qt.AlignCenter)  # 设置布局内部件居中显示

        self.right_layout.addWidget(self.right_process_bar, 9, 0, 1, 9)
        self.right_layout.addWidget(self.right_playconsole_widget, 10, 0, 1, 9)
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

        self.right_bar_widget_search_input.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
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
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')
        # self.right_recommend_widget.setStyleSheet(
        #     '''
        #         QToolButton{border:none;}
        #         QToolButton:hover{border-bottom:2px solid #F76677;}
        #     ''')
        self.right_playlist_widget.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')
        self.right_newsong_widget.setStyleSheet('''
            QPushButton{
                border:none;
                color:gray;
                font-size:12px;
                height:40px;
                padding-left:5px;
                padding-right:10px;
                text-align:left;
            }
            QPushButton:hover{
                color:black;
                border:1px solid #F3F3F5;
                border-radius:10px;
                background:LightGray;
            }
        ''')
        self.right_process_bar.setStyleSheet('''
            QProgressBar::chunk {
                background-color: #F76677;
            }
        ''')

        self.right_playconsole_widget.setStyleSheet('''
            QPushButton{
                border:none;
            }
        ''')
        #self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.main_layout.setSpacing(0)


        # 这里设置容器内顶部标签
        """这里是在right_widget里面创建标签，而且这个标签是用非原生类创建的"""
        self._TitleLabel = QTitleLabel(self.right_widget)
        self._TitleLabel.setMouseTracking(True)  # 设置标题栏标签鼠标跟踪（如不设，则标题栏内在widget上层，无法实现跟踪）
        self._TitleLabel.setIndent(30)  # 设置标题栏文本缩进，距离左边框的距离
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
                color:rgb(200,100,100,250);
                font-size:25px;
                font-weight:bold;
                font-family:Roman times;
                border-top:1px solid gray;
                border-right:1px solid gray;
            }
            QTitleLabel#right_lable:hover{background:#f5f5f5;}
        ''')# 标签设置为红色




        """这里是在左上角面创建图标，"""
        """这里是在左上角面创建图标，"""
        self.button_logo = QtWidgets.QToolButton(self.right_widget)
        #self.button_logo.setText("不需要歌词,也可以打动你的心")
        self.button_logo.setIcon(QtGui.QIcon('./001.png'))
        self.button_logo.setIconSize(QtCore.QSize(30, 30))
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
        self._TitleLabel.setStyleSheet('''
            QTitleLabel{
                background:#f5f5f5;
                color:rgb(200,100,100,250);
                font-size:25px;
                font-weight:bold;
                font-family:Roman times;
                border-top:1px solid gray;
                border-right:1px solid gray;
            }
            QTitleLabel#right_lable:hover{background:#f5f5f5;}
        ''')# 标签设置为红色


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

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open("./UnFrameStyle.qss").read())
    gui = MainUi()
    gui.setMinMaxButtons(True)
    gui.setCloseButton(True)
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()




