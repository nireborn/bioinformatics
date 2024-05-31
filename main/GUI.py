import sys
from datetime import datetime
from functools import partial

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFileDialog, QPushButton, QMessageBox
# from pyqt5_plugins.examplebuttonplugin import QtGui

from PyQt5 import QtGui

from function.bar_function import bar_plot
from function.fasta_function import single_base_substitution, get_length, reverse_complement_seq, complement_seq
from function.genetic_structure_function import genetic_structure
from function.genetic_tree_function import genetic_tree
from function.gff_function import filter_gff3
from function.heatmap_function import heatmap_plot
from function.line_function import line_plot
from function.pie_function import pie_plot
from function.scatterplot_function import scatter_plot
from function.seq_function import gc_calculation
from function.seq_function import slicing
from function.venn_function import venn_plot


# ------------------ 线程类--实现全部功能 --起始 ------------------
# function-1 -- 切割
class Thread_function_1(QThread):
    finished_signal = pyqtSignal()

    def run(self):
        slicing_tab1()
        self.finished_signal.emit()


# function-2 -- GC含量
class Thread_function_2(QThread):
    finished_signal = pyqtSignal()

    def run(self):
        gc_tab1()
        self.finished_signal.emit()


# function-3 --sbs --single_base_substitution
class Thread_function_3(QThread):
    finished_signal = pyqtSignal()

    def run(self):
        sbs_tab2()
        self.finished_signal.emit()


# function-4 --cs --complement_seq
class Thread_function_4(QThread):
    finished_signal = pyqtSignal()

    def run(self):
        cs_tab2()
        self.finished_signal.emit()


# function-5 --rcs --reverse_complement_seq
class Thread_function_5(QThread):
    finished_signal = pyqtSignal()

    def run(self):
        rcs_tab2()
        self.finished_signal.emit()


# function-6 --gl --get_length
class Thread_function_6(QThread):
    finished_signal = pyqtSignal()

    def run(self):
        gl_tab2()
        self.finished_signal.emit()


# function-7 --gff
class Thread_function_7(QThread):
    finished_signal = pyqtSignal()

    def run(self):
        gff_tab3()
        self.finished_signal.emit()


# function-8
class Thread_function_8(QThread):
    finished_signal = pyqtSignal()

    def run(self):
        scatter_tab4()
        self.finished_signal.emit()


# function-9
class Thread_function_9(QThread):
    finished_signal = pyqtSignal()

    def run(self):
        line_tab5()
        self.finished_signal.emit()


# function-10
class Thread_function_10(QThread):
    finished_signal = pyqtSignal()

    def run(self):
        bar_tab6()
        self.finished_signal.emit()


# function-11
class Thread_function_11(QThread):
    finished_signal = pyqtSignal()

    def run(self):
        pie_tab7()
        self.finished_signal.emit()


# function-12
class Thread_function_12(QThread):
    finished_signal = pyqtSignal()

    def run(self):
        heatmap_tab8()
        self.finished_signal.emit()


# function-13
class Thread_function_13(QThread):
    finished_signal = pyqtSignal()

    def run(self):
        venn_tab9()
        self.finished_signal.emit()


# function-14
class Thread_function_14(QThread):
    finished_signal = pyqtSignal()

    def run(self):
        stru_tab10()
        self.finished_signal.emit()


# function-15
class Thread_function_15(QThread):
    finished_signal = pyqtSignal()

    def run(self):
        tree_tab11()
        self.finished_signal.emit()


# ------------------ 线程类--实现全部功能 --终止 ------------------


# 定义 Ui_Form类
class Ui_Form:
    # 创建setupUi方法，用于设置界面的布局和组件
    def setupUi(self, Form):
        # 设置文本变量
        _translate = QtCore.QCoreApplication.translate

        """
        :param Form: 接受参数Form，该参数是界面的主窗体
        :return: None
        """
        # 获取主机的宽和高
        desktop = app.desktop()
        desktop_width = desktop.width()  # 获取电脑宽，为int类型
        desktop_height = desktop.height()  # 获取电脑宽
        # desktop_width, desktop_height = 3840, 2160

        # ------------------ Form主窗体 --起始 ------------------

        # 设置主窗体的对象名称为"Form"
        Form.setObjectName("Form")
        # 对主窗口设置大小，初始化为主机的一半，（1/4大小）
        Form.resize(desktop_width*2 //3, desktop_height*2 // 3)

        # 对于Form的布局：水平布局
        # 先创建，再命名
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")

        # ------------------ Form主窗体 --终止 ------------------

        """
        groupBox 与 tabWidget说明：
        groupBox 与 tabWidget为水平布局，均在Form中
        groupBox存放菜单功能按钮
        tabWidget存放选项卡
        """
        # ------------------ groupBox --起始 ------------------

        # 创建一个分组框对象，其父对象为Form
        self.groupBox = QtWidgets.QGroupBox(Form)

        # 设置按钮左上角的标题（暂时不需要，设置为空）
        self.groupBox.setTitle("")

        # 设置属性名groupBox
        self.groupBox.setObjectName("groupBox")

        # 设置groupBox布局为垂直布局
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # ------------------ groupBox --终止 ------------------

        # ------------------ groupBox-按钮PushButton --起始 ------------------

        self.pushButton_1 = QtWidgets.QPushButton(self.groupBox)
        # self.pushButton_1.setMinimumSize(QtCore.QSize(80, 25))
        # self.pushButton_1.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout_2.addWidget(self.pushButton_1)

        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        # self.pushButton_2.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        # self.pushButton_3.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        # self.pushButton_4.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        # self.pushButton_5.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        # self.pushButton_6.setMaximumSize(QtCore.QSize(80, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)

        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_2.addWidget(self.pushButton_8)

        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_2.addWidget(self.pushButton_9)

        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_2.addWidget(self.pushButton_10)

        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_2.addWidget(self.pushButton_11)

        # 建立createTab1~9槽函数，点击按钮的时候创建标签页tab_1~9
        self.pushButton_1.clicked.connect(self.createTab_1)
        self.pushButton_2.clicked.connect(self.createTab_2)
        self.pushButton_3.clicked.connect(self.createTab_3)
        self.pushButton_4.clicked.connect(self.createTab_4)
        self.pushButton_5.clicked.connect(self.createTab_5)
        self.pushButton_6.clicked.connect(self.createTab_6)
        self.pushButton_7.clicked.connect(self.createTab_7)
        self.pushButton_8.clicked.connect(self.createTab_8)
        self.pushButton_9.clicked.connect(self.createTab_9)
        self.pushButton_10.clicked.connect(self.createTab_10)
        self.pushButton_11.clicked.connect(self.createTab_11)

        # 设置按钮文本
        Form.setWindowTitle(_translate("Form", "生物信息平台"))
        font1 = QtGui.QFont()
        font1.setFamily("KaiTi")
        font1.setPointSize(12)
        font1.setBold(True)
        self.pushButton_1.setFont(font1)
        self.pushButton_1.setStyleSheet("color: blue;")
        self.pushButton_1.setText(_translate("Form", "序列"))

        font2 = QtGui.QFont()
        font2.setFamily("KaiTi")
        font2.setPointSize(12)
        font2.setBold(True)
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet("color: blue;")
        self.pushButton_2.setText(_translate("Form", "fasta"))

        font3 = QtGui.QFont()
        font3.setFamily("KaiTi")
        font3.setPointSize(12)
        font3.setBold(True)
        self.pushButton_3.setFont(font3)
        self.pushButton_3.setStyleSheet("color: blue;")
        self.pushButton_3.setText(_translate("Form", "gff"))

        font4 = QtGui.QFont()
        font4.setFamily("KaiTi")
        font4.setPointSize(12)
        font4.setBold(True)
        self.pushButton_4.setFont(font4)
        self.pushButton_4.setStyleSheet("color: blue;")
        self.pushButton_4.setText(_translate("Form", "散点图"))

        font5 = QtGui.QFont()
        font5.setFamily("KaiTi")
        font5.setPointSize(12)
        font5.setBold(True)
        self.pushButton_5.setFont(font5)
        self.pushButton_5.setStyleSheet("color: blue;")
        self.pushButton_5.setText(_translate("Form", "折线图"))

        font6 = QtGui.QFont()
        font6.setFamily("KaiTi")
        font6.setPointSize(12)
        font6.setBold(True)
        self.pushButton_6.setFont(font6)
        self.pushButton_6.setStyleSheet("color: blue;")
        self.pushButton_6.setText(_translate("Form", "柱状图"))

        font7 = QtGui.QFont()
        font7.setFamily("KaiTi")
        font7.setPointSize(12)
        font7.setBold(True)
        self.pushButton_7.setFont(font7)
        self.pushButton_7.setStyleSheet("color: blue;")
        self.pushButton_7.setText(_translate("Form", "饼状图"))

        font8 = QtGui.QFont()
        font8.setFamily("KaiTi")
        font8.setPointSize(12)
        font8.setBold(True)
        self.pushButton_8.setFont(font8)
        self.pushButton_8.setStyleSheet("color: blue;")
        self.pushButton_8.setText(_translate("Form", "热力图"))

        font9 = QtGui.QFont()
        font9.setFamily("KaiTi")
        font9.setPointSize(12)
        font9.setBold(True)
        self.pushButton_9.setFont(font9)
        self.pushButton_9.setStyleSheet("color: blue;")
        self.pushButton_9.setText(_translate("Form", "venn图"))

        font10 = QtGui.QFont()
        font10.setFamily("KaiTi")
        font10.setPointSize(12)
        font10.setBold(True)
        self.pushButton_10.setFont(font10)
        self.pushButton_10.setStyleSheet("color: blue;")
        self.pushButton_10.setText(_translate("Form", "基因结构"))

        font11 = QtGui.QFont()
        font11.setFamily("KaiTi")
        font11.setPointSize(12)
        font11.setBold(True)
        self.pushButton_11.setFont(font11)
        self.pushButton_11.setStyleSheet("color: blue;")
        self.pushButton_11.setText(_translate("Form", "进化树"))

        # 设置spacer，固定按钮
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)

        # 将groupBox加入水平布局
        self.verticalLayout.addWidget(self.groupBox)

        # ------------------ groupBox-按钮PushButton --终止 ------------------

        # ------------------ tabWidget-主体 --起始 ------------------

        # 创建一个标签页窗口部件 (QTabWidget)，并将其与主窗体关联。
        self.tabWidget = QtWidgets.QTabWidget(Form)

        # 允许标签页上的选项卡关闭
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")

        # 链接到槽函数closeTab() -- 进行关闭操作
        self.tabWidget.tabCloseRequested.connect(self.closeTab)

        # ------------------ tabWidget-主体 --终止 ------------------

        self.verticalLayout.addWidget(self.tabWidget)

        # self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)

        # ------------------ 创建标签页tab_0 --起始 ------------------
        self.createTab_0()
        # ------------------ 创建标签页-0 --终止 ------------------

        # QtCore.QMetaObject.connectSlotsByName(Form)

    # ------------------ 关闭选项卡的槽函数 --起始 ------------------
    def closeTab(self, index):
        # 获取关闭请求的标签页索引
        # 执行你需要的关闭操作，例如关闭标签页
        self.tabWidget.removeTab(index)

    # ------------------ 关闭选项卡的槽函数 --终止 ------------------

    # ------------------ 创建初始标签页tab_0 --起始 ------------------
    def createTab_0(self):
        _translate = QtCore.QCoreApplication.translate

        self.tab_0 = QtWidgets.QWidget()
        self.tab_0.setObjectName("tab_0")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit_0 = QtWidgets.QTextEdit(self.tab_0)
        self.textEdit_0.setObjectName("textEdit_0")
        self.verticalLayout_3.addWidget(self.textEdit_0)

        # 创建标签页 tab_0
        self.tabWidget.addTab(self.tab_0, "")

        self.textEdit_0.setStyleSheet("background-image:url(../background/background.png);")
        # 设置文本内容 -- 可以进行替换[*]
        self.textEdit_0.setHtml(_translate("Form",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">关于生物信息平台：</span></p>\n"
                                           "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">该平台是功能的集合，可用于医学和生物学领域中获得数据的处理。</span></p>\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\"><br /></p>\n"
                                           "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">现有功能概述：</span></p>\n"
                                           "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">（</span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt; font-weight:600;\">1</span><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">）序列编辑功能包括序列剪切和</span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt; font-weight:600;\">GC</span><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">含量统计。</span></p>\n"
                                           "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">①剪切序列主要是对序列的切片操作；</span></p>\n"
                                           "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">②计算</span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt; font-weight:600;\">GC</span><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">含量主要是对所提供的序列进行</span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt; font-weight:600;\">GC</span><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">含量的统计。</span></p>\n"
                                           "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">（</span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt; font-weight:600;\">2</span><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">）</span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt; font-weight:600;\">fasta/fastq</span><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">文件处理功能包括单碱基替换、互补序列、反向互补序列、长度计算等功能。</span></p>\n"
                                           "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">①单碱基替换主要是将所提供的</span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt; font-weight:600;\">fasta</span><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">文件中的需要进行替换的碱基全部替换为替换为碱基；</span></p>\n"
                                           "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">②互补序列主要是将所提供的</span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt; font-weight:600;\">fasta</span><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">文件中的序列全部替换为其互补序列；</span></p>\n"
                                           "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">③反向互补序列主要是将所提供的</span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt; font-weight:600;\">fasta</span><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">文件中的序列全部替换为其反向互补序列；</span></p>\n"
                                           "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">④计算长度主要是将所提供的</span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt; font-weight:600;\">fasta</span><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">文件中的序列的长度计算出来。</span></p>\n"
                                           "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">（</span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt; font-weight:600;\">3</span><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">）</span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt; font-weight:600;\">gff</span><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">文件处理功能主要为筛选出文件中染色体指定位置之间的基因，并输出基因的名字，染色体，起始位置。</span></p>\n"
                                           "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">（</span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt; font-weight:600;\">4</span><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">）可视化功能则包括散点图、折线图、柱状图、饼状图、热力图、</span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt; font-weight:600;\">Venn</span><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">图、基因结构和进化树等功能。</span></p>\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\"><br /></p>\n"
                                           "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">未来规划功能概述：</span></p>\n"
                                           "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">1、免疫细胞比例可视化、免疫浸润评分；</span></p>\n"
                                           "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'KaiTi, KaiTi, SimSun, sans-serif, sans-serif;\'; font-size:12pt; font-weight:600;\">2、机器学习对代谢组学数据进行模型建立，用于癌症的预测；</span></p></body></html>"))

        font_tab0 = QtGui.QFont()
        font_tab0.setFamily("KaiTi")
        font_tab0.setPointSize(12)
        font_tab0.setBold(True)
        self.tabWidget.setFont(font_tab0)
        # self.tabWidget.setStyleSheet("color: blue;")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_0), _translate("Form", "首页"))

    # ------------------ 创建初始标签页tab_0 --终止 ------------------

    # ------------------ 点击按钮创建标签页-1 --起始 ------------------

    def createTab_1(self):
        # tab_1创建，布局为水平--为了自由拉伸
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # 对整个布局进行一个水平布局 -- 对控件进行布局
        self.verticalLayout_tab1_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_tab1_1.setObjectName("verticalLayout_tab1_1")

        # text控件
        self.textEdit_tab1_1 = QtWidgets.QTextEdit(self.tab_1)
        self.textEdit_tab1_1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.textEdit_tab1_1.setObjectName("textEdit_tab1_1")
        self.verticalLayout_tab1_1.addWidget(self.textEdit_tab1_1)

        # spacer控件
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Fixed)  # 这里的0，0可以调整
        self.verticalLayout_tab1_1.addItem(spacerItem1)

        # horizontalLayout控件
        self.horizontalLayout_tab1_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab1_1.setObjectName("horizontalLayout_tab1_1")

        # horizontalLayout存放读取文本信息 + 按钮选择
        # line控件 -- lineEdit_tab1_1
        self.lineEdit_tab1_1 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_tab1_1.setObjectName("lineEdit_tab1_1")
        self.horizontalLayout_tab1_1.addWidget(self.lineEdit_tab1_1)
        # pushButton控件 -- pushButton_tab1_1
        # ------------------ # pushButton_tab1_1 --起始 ------------------

        self.pushButton_tab1_1 = QtWidgets.QPushButton(self.tab_1)
        # self.pushButton_tab1_1.setMaximumSize(QtCore.QSize(75, 25))
        self.pushButton_tab1_1.setObjectName("pushButton_tab1_1")

        # pushButton_tab1_1点击后，选择文件，显示在lineEdit_tab1_1中
        self.pushButton_tab1_1.clicked.connect(partial(self.select_file, "Text files (*.txt)", self.lineEdit_tab1_1))

        # self.pushButton_tab1_1.clicked.connect(self.select_txt_file_tab1_1)
        self.horizontalLayout_tab1_1.addWidget(self.pushButton_tab1_1)
        # ------------------ # pushButton_tab1_1 --终止 ------------------

        # 整个verticalLayout加入horizontalLayout控件
        self.verticalLayout_tab1_1.addLayout(self.horizontalLayout_tab1_1)

        # horizontalLayout控件 = 2*弹簧 + 2*文本 + 2*选择
        self.horizontalLayout_tab1_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab1_2.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_tab1_2.setObjectName("horizontalLayout_tab1_2")

        # spacer控件
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_tab1_2.addItem(spacerItem2)

        # label控件
        self.label_tab1_1 = QtWidgets.QLabel(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_tab1_1.sizePolicy().hasHeightForWidth())
        self.label_tab1_1.setSizePolicy(sizePolicy)
        self.label_tab1_1.setObjectName("label_tab1_1")
        self.horizontalLayout_tab1_2.addWidget(self.label_tab1_1)

        # spinBox控件
        self.spinBox_tab1_1 = QtWidgets.QSpinBox(self.tab_1)
        self.spinBox_tab1_1.setKeyboardTracking(False)
        self.spinBox_tab1_1.setMinimum(1)
        self.spinBox_tab1_1.setMaximum(1000000)
        self.spinBox_tab1_1.setObjectName("spinBox_tab1_1")
        self.horizontalLayout_tab1_2.addWidget(self.spinBox_tab1_1)

        # label控件
        self.label_tab1_2 = QtWidgets.QLabel(self.tab_1)
        self.label_tab1_2.setObjectName("label_tab1_2")
        self.horizontalLayout_tab1_2.addWidget(self.label_tab1_2)

        # spinBox控件
        self.spinBox_tab1_2 = QtWidgets.QSpinBox(self.tab_1)
        self.spinBox_tab1_2.setKeyboardTracking(False)
        self.spinBox_tab1_2.setMinimum(1)
        self.spinBox_tab1_2.setMaximum(1000000)
        self.spinBox_tab1_2.setObjectName("spinBox_tab1_2")
        self.horizontalLayout_tab1_2.addWidget(self.spinBox_tab1_2)

        # spacer控件
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_tab1_2.addItem(spacerItem3)
        # 整个verticalLayout加入horizontalLayout控件
        self.verticalLayout_tab1_1.addLayout(self.horizontalLayout_tab1_2)

        # 整个verticalLayout加入spacer控件
        spacerItem4 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab1_1.addItem(spacerItem4)

        # horizontalLayout控件-3
        self.horizontalLayout_tab1_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab1_3.setObjectName("horizontalLayout_tab1_3")
        # line控件
        self.lineEdit_tab1_2 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_tab1_2.setObjectName("lineEdit_tab1_2")
        self.horizontalLayout_tab1_3.addWidget(self.lineEdit_tab1_2)
        # pushButton控件 --pushButton_tab1_2
        self.pushButton_tab1_2 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_tab1_2.setObjectName("pushButton_tab1_2")
        self.horizontalLayout_tab1_3.addWidget(self.pushButton_tab1_2)
        # pushButton_tab1_2槽函数
        self.pushButton_tab1_2.clicked.connect(partial(self.select_dir, self.lineEdit_tab1_2))

        # 整个verticalLayout加入horizontalLayout控件
        self.verticalLayout_tab1_1.addLayout(self.horizontalLayout_tab1_3)

        # spacer控件
        spacerItem5 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab1_1.addItem(spacerItem5)

        # horizontalLayout-4
        self.horizontalLayout_tab1_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab1_4.setObjectName("horizontalLayout_tab1_4")
        # pushButton控件
        self.pushButton_tab1_3 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_tab1_3.setObjectName("pushButton_tab1_3")

        # pushButton_tab1_3槽函数 -- 剪切序列
        self.pushButton_tab1_3.clicked.connect(self.slic)

        self.horizontalLayout_tab1_4.addWidget(self.pushButton_tab1_3)

        # pushButton控件
        self.pushButton_tab1_4 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_tab1_4.setObjectName("pushButton_tab1_4")

        # pushButton_tab1_4槽函数 -- 计算GC含量
        self.pushButton_tab1_4.clicked.connect(self.gch)

        self.horizontalLayout_tab1_4.addWidget(self.pushButton_tab1_4)

        # 整个verticalLayout加入horizontalLayout控件
        self.verticalLayout_tab1_1.addLayout(self.horizontalLayout_tab1_4)

        # 整个verticalLayout放入tab的verticalLayout
        self.verticalLayout_2.addLayout(self.verticalLayout_tab1_1)

        # 创建标签页
        self.tabWidget.addTab(self.tab_1, "")
        # 转到tab_1
        self.tabWidget.setCurrentWidget(self.tab_1)

        # 设置文本内容
        _translate = QtCore.QCoreApplication.translate
        self.textEdit_tab1_1.setHtml(_translate("Form",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'KaiTi, SimSun, sans-serif\'; font-size:12pt; font-weight:bold; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">功能说明：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.<span style=\" font-family:\'KaiTi, SimSun, sans-serif\',\'monospace\'; color:#000000;\">文件处理：<br />    第一个输入框为：需要处理的</span><span style=\" font-family:\'JetBrains Mono\',\'monospace\'; color:#000000;\">txt</span><span style=\" font-family:\'KaiTi, SimSun, sans-serif\',\'monospace\'; color:#000000;\">文件的URL；<br />    第二个输入框为：将处理后新生成的</span><span style=\" font-family:\'JetBrains Mono\',\'monospace\'; color:#000000;\">txt</span><span style=\" font-family:\'KaiTi, SimSun, sans-serif\',\'monospace\'; color:#000000;\">文件存放所在文件夹的URL；<br />2.实现功能：<br />    ①剪切序列：对序列的切片操作，需要提供起始位置和终止位置；<br />    ②计算GC含量：计算所提供序列（txt文件中的序列）的</span><span style=\" font-family:\'JetBrains Mono\',\'monospace\'; color:#000000;\">GC%</span></p></body></html>"))

        self.pushButton_tab1_1.setText(_translate("Form", "..."))
        self.label_tab1_1.setText(_translate("Form", "起始位置："))
        self.label_tab1_2.setText(_translate("Form", "终止位置："))
        self.pushButton_tab1_2.setText(_translate("Form", "..."))
        self.pushButton_tab1_3.setText(_translate("Form", "剪切序列"))
        self.pushButton_tab1_4.setText(_translate("Form", "计算GC含量"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("Form", "序列"))

    # ------------------ 点击按钮创建标签页-1 --终止 ------------------

    # ------------------ 点击按钮创建标签页-2 --起始 ------------------
    def createTab_2(self):
        _translate = QtCore.QCoreApplication.translate

        # 主界面tab_2
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        # 设置布局
        self.verticalLayout_tab2_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_tab2_1.setObjectName("verticalLayout_tab2_1")

        # 文本框 -- 显示功能说明
        self.textEdit_tab2_1 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_tab2_1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.textEdit_tab2_1.setObjectName("textEdit_tab2_1")
        self.verticalLayout_tab2_1.addWidget(self.textEdit_tab2_1)

        # 弹簧控制布局
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab2_1.addItem(spacerItem6)

        # 垂直布局horizontalLayout_tab2_1 = 文本 + 按钮
        self.horizontalLayout_tab2_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab2_1.setObjectName("horizontalLayout_tab2_1")

        # 文本lineEdit_tab2_1
        self.lineEdit_tab2_1 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_tab2_1.setObjectName("lineEdit_tab2_1")
        self.horizontalLayout_tab2_1.addWidget(self.lineEdit_tab2_1)

        # 按钮 pushButton_tab2_1
        self.pushButton_tab2_1 = QtWidgets.QPushButton(self.tab_2)
        # self.pushButton_tab2_1.setMaximumSize(QtCore.QSize(75, 25))
        self.pushButton_tab2_1.setObjectName("pushButton_tab2_1")

        # 信号与槽
        self.pushButton_tab2_1.clicked.connect(partial(self.select_file, "Fasta files (*.fasta)", self.lineEdit_tab2_1))

        # 按钮布局
        self.horizontalLayout_tab2_1.addWidget(self.pushButton_tab2_1)

        # 添加verticalLayout_tab2_1布局
        self.verticalLayout_tab2_1.addLayout(self.horizontalLayout_tab2_1)

        # 垂直布局
        self.horizontalLayout_tab2_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab2_2.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_tab2_2.setObjectName("horizontalLayout_tab2_2")

        # 左弹簧
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_tab2_2.addItem(spacerItem7)

        # 说明文字 -- "需要进行替换的碱基："
        self.label_tab2_1 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_tab2_1.sizePolicy().hasHeightForWidth())
        self.label_tab2_1.setSizePolicy(sizePolicy)
        self.label_tab2_1.setObjectName("label_tab2_1")
        self.horizontalLayout_tab2_2.addWidget(self.label_tab2_1)

        # 数字选择框comboBox_tab2_1
        self.comboBox_tab2_1 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_tab2_1.setObjectName("comboBox_tab2_1")

        # 添加A、T、C、G四个选项
        self.comboBox_tab2_1.addItem("")
        self.comboBox_tab2_1.addItem("")
        self.comboBox_tab2_1.addItem("")
        self.comboBox_tab2_1.addItem("")
        self.horizontalLayout_tab2_2.addWidget(self.comboBox_tab2_1)

        # 数字选择框comboBox_tab2_2 同
        self.label_tab2_2 = QtWidgets.QLabel(self.tab_2)
        self.label_tab2_2.setObjectName("label_tab2_2")
        self.horizontalLayout_tab2_2.addWidget(self.label_tab2_2)
        self.comboBox_tab2_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_tab2_2.setObjectName("comboBox_tab2_2")
        self.comboBox_tab2_2.addItem("")
        self.comboBox_tab2_2.addItem("")
        self.comboBox_tab2_2.addItem("")
        self.comboBox_tab2_2.addItem("")
        self.horizontalLayout_tab2_2.addWidget(self.comboBox_tab2_2)

        # 右弹簧
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_tab2_2.addItem(spacerItem8)
        self.verticalLayout_tab2_1.addLayout(self.horizontalLayout_tab2_2)

        # 布局弹簧
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab2_1.addItem(spacerItem9)

        # 同垂直布局horizontalLayout_tab2_2 = 文本 + 按钮
        self.horizontalLayout_tab2_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab2_3.setObjectName("horizontalLayout_tab2_3")

        self.lineEdit_tab2_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_tab2_3.setObjectName("lineEdit_tab2_3")
        self.horizontalLayout_tab2_3.addWidget(self.lineEdit_tab2_3)

        # pushButton_tab2_3 按钮 内容输出到lineEdit_tab2_3
        self.pushButton_tab2_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_tab2_3.setObjectName("pushButton_tab2_3")
        self.pushButton_tab2_3.clicked.connect(partial(self.select_dir, self.lineEdit_tab2_3))
        self.horizontalLayout_tab2_3.addWidget(self.pushButton_tab2_3)

        self.verticalLayout_tab2_1.addLayout(self.horizontalLayout_tab2_3)

        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab2_1.addItem(spacerItem10)

        # 四个功能按钮
        self.horizontalLayout_tab2_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab2_4.setObjectName("horizontalLayout_tab2_4")

        # 单碱基替换sbs
        self.pushButton_tab2_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_tab2_4.setObjectName("pushButton_tab2_4")
        self.pushButton_tab2_4.clicked.connect(self.sbs)

        self.horizontalLayout_tab2_4.addWidget(self.pushButton_tab2_4)

        # 互补序列cs
        self.pushButton_tab2_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_tab2_5.setObjectName("pushButton_tab2_5")
        self.pushButton_tab2_5.clicked.connect(self.cs)

        self.horizontalLayout_tab2_4.addWidget(self.pushButton_tab2_5)

        # 反向互补序列rcs
        self.pushButton_tab2_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_tab2_6.setObjectName("pushButton_tab2_6")
        self.pushButton_tab2_6.clicked.connect(self.rcs)

        self.horizontalLayout_tab2_4.addWidget(self.pushButton_tab2_6)

        # 计算长度gl
        self.pushButton_tab2_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_tab2_7.setObjectName("pushButton_tab2_7")
        self.pushButton_tab2_7.clicked.connect(self.gl)

        self.horizontalLayout_tab2_4.addWidget(self.pushButton_tab2_7)

        # 调整布局
        self.verticalLayout_tab2_1.addLayout(self.horizontalLayout_tab2_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_tab2_1)

        # 创建tab_2
        self.tabWidget.addTab(self.tab_2, "")
        self.tabWidget.setCurrentWidget(self.tab_2)

        # 设置文本内容
        self.textEdit_tab2_1.setHtml(_translate("Form",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'KaiTi, SimSun, sans-serif\'; font-size:12pt; font-weight:bold; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">功能说明：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.fasta文件处理：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第一个输入框为：需要处理的fasta文件的URL；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第二个输入框为：将处理后新生成的fasta文件存放所在文件夹的URL；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.实现功能：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    ①单碱基替换：将提供的fasta文件中的&quot;需要进行替换的碱基&quot;全部替换为&quot;替换为碱基&quot;；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    ②互补序列：将提供的fasta文件中的序列全部替换为其互补序列；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    ③反向互补序列：将提供的fasta文件中的序列全部替换为其反向互补序列；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    ④计算长度：输出格式为&quot;id + 基因序列长度 + 基因序列&quot;；</p></body></html>"))
        self.pushButton_tab2_1.setText(_translate("Form", "..."))
        self.label_tab2_1.setText(_translate("Form", "需要进行替换的碱基："))
        self.comboBox_tab2_1.setCurrentText(_translate("Form", "A"))
        self.comboBox_tab2_1.setItemText(0, _translate("Form", "A"))
        self.comboBox_tab2_1.setItemText(1, _translate("Form", "T"))
        self.comboBox_tab2_1.setItemText(2, _translate("Form", "C"))
        self.comboBox_tab2_1.setItemText(3, _translate("Form", "G"))
        self.label_tab2_2.setText(_translate("Form", "替换为碱基："))
        self.comboBox_tab2_2.setItemText(0, _translate("Form", "A"))
        self.comboBox_tab2_2.setItemText(1, _translate("Form", "T"))
        self.comboBox_tab2_2.setItemText(2, _translate("Form", "C"))
        self.comboBox_tab2_2.setItemText(3, _translate("Form", "G"))
        self.pushButton_tab2_3.setText(_translate("Form", "..."))
        self.pushButton_tab2_4.setText(_translate("Form", "单碱基替换"))
        self.pushButton_tab2_5.setText(_translate("Form", "互补序列"))
        self.pushButton_tab2_6.setText(_translate("Form", "反向互补序列"))
        self.pushButton_tab2_7.setText(_translate("Form", "计算长度"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "fasta"))

    # ------------------ 点击按钮创建标签页-2 --终止 ------------------

    # ------------------ 点击按钮创建标签页-3 --起始 ------------------

    def createTab_3(self):
        _translate = QtCore.QCoreApplication.translate

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_3)

        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.verticalLayout_tab3_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_tab3_1.setObjectName("verticalLayout_tab3_1")

        self.textEdit_tab3_1 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_tab3_1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.textEdit_tab3_1.setObjectName("textEdit_tab3_1")
        self.verticalLayout_tab3_1.addWidget(self.textEdit_tab3_1)

        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab3_1.addItem(spacerItem11)

        self.horizontalLayout_tab3_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab3_1.setObjectName("horizontalLayout_tab3_1")

        self.lineEdit_tab3_1 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_tab3_1.setObjectName("lineEdit_tab3_1")
        self.horizontalLayout_tab3_1.addWidget(self.lineEdit_tab3_1)

        self.pushButton_tab3_1 = QtWidgets.QPushButton(self.tab_3)
        # self.pushButton_tab3_1.setMaximumSize(QtCore.QSize(75, 25))
        self.pushButton_tab3_1.setObjectName("pushButton_tab3_1")
        self.pushButton_tab3_1.clicked.connect(partial(self.select_file, "Gff3 files (*.gff3)", self.lineEdit_tab3_1))
        self.horizontalLayout_tab3_1.addWidget(self.pushButton_tab3_1)

        self.verticalLayout_tab3_1.addLayout(self.horizontalLayout_tab3_1)

        self.horizontalLayout_tab3_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab3_2.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_tab3_2.setObjectName("horizontalLayout_tab3_2")

        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_tab3_2.addItem(spacerItem12)

        self.label_tab3_1 = QtWidgets.QLabel(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_tab3_1.sizePolicy().hasHeightForWidth())
        self.label_tab3_1.setSizePolicy(sizePolicy)
        self.label_tab3_1.setObjectName("label_tab3_1")
        self.horizontalLayout_tab3_2.addWidget(self.label_tab3_1)

        self.spinBox_tab3_1 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_tab3_1.setMinimum(1)
        self.spinBox_tab3_1.setMaximum(1000000)
        self.spinBox_tab3_1.setObjectName("spinBox_tab3_1")
        self.horizontalLayout_tab3_2.addWidget(self.spinBox_tab3_1)

        self.label_tab3_2 = QtWidgets.QLabel(self.tab_3)
        self.label_tab3_2.setObjectName("label_tab3_2")
        self.horizontalLayout_tab3_2.addWidget(self.label_tab3_2)

        self.spinBox_tab3_2 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_tab3_2.setMinimum(1)
        self.spinBox_tab3_2.setMaximum(1000000)
        self.spinBox_tab3_2.setObjectName("spinBox_tab3_2")
        self.horizontalLayout_tab3_2.addWidget(self.spinBox_tab3_2)

        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_tab3_2.addItem(spacerItem13)

        self.verticalLayout_tab3_1.addLayout(self.horizontalLayout_tab3_2)

        spacerItem14 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab3_1.addItem(spacerItem14)

        self.horizontalLayout_tab3_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab3_3.setObjectName("horizontalLayout_tab3_3")

        self.lineEdit_tab3_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_tab3_2.setObjectName("lineEdit_tab3_2")
        self.horizontalLayout_tab3_3.addWidget(self.lineEdit_tab3_2)

        self.pushButton_tab3_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_tab3_2.setObjectName("pushButton_tab3_2")
        self.pushButton_tab3_2.clicked.connect(partial(self.select_dir, self.lineEdit_tab3_2))
        self.horizontalLayout_tab3_3.addWidget(self.pushButton_tab3_2)

        self.verticalLayout_tab3_1.addLayout(self.horizontalLayout_tab3_3)

        spacerItem15 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab3_1.addItem(spacerItem15)

        self.horizontalLayout_tab3_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab3_4.setObjectName("horizontalLayout_tab3_4")

        self.pushButton_tab3_4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_tab3_4.setObjectName("pushButton_tab3_4")
        self.pushButton_tab3_4.clicked.connect(self.gff)
        self.horizontalLayout_tab3_4.addWidget(self.pushButton_tab3_4)

        self.verticalLayout_tab3_1.addLayout(self.horizontalLayout_tab3_4)
        self.verticalLayout_5.addLayout(self.verticalLayout_tab3_1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tabWidget.setCurrentWidget(self.tab_3)

        self.textEdit_tab3_1.setHtml(_translate("Form",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'KaiTi, SimSun, sans-serif\'; font-size:12pt; font-weight:bold; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">功能说明：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.对gff3文件进行操作：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第一个输入框为：需要处理的gff3文件的URL；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第二个输入框为：将处理后新生成的txt文件存放所在文件夹的URL；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.实现功能：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    筛选出文件中染色体指定位置之间的基因，并输出染色体编号 + 基因起始位置 + 基因终止位置 + 基因ID；</p></body></html>"))
        self.pushButton_tab3_1.setText(_translate("Form", "..."))
        self.label_tab3_1.setText(_translate("Form", "起始位置："))
        self.label_tab3_2.setText(_translate("Form", "终止位置："))
        self.pushButton_tab3_2.setText(_translate("Form", "..."))
        self.pushButton_tab3_4.setText(_translate("Form", "处理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "gff"))

    # ------------------ 点击按钮创建标签页-3 --终止 ------------------

    # ------------------ 点击按钮创建标签页-4 --起始 ------------------

    def createTab_4(self):
        _translate = QtCore.QCoreApplication.translate

        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_tab4_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_tab4_1.setObjectName("verticalLayout_tab4_1")
        self.textEdit_tab4_1 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_tab4_1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.textEdit_tab4_1.setObjectName("textEdit_tab4_1")
        self.verticalLayout_tab4_1.addWidget(self.textEdit_tab4_1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab4_1.addItem(spacerItem16)
        self.horizontalLayout_tab4_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab4_1.setObjectName("horizontalLayout_tab4_1")

        self.lineEdit_tab4_1 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_tab4_1.setObjectName("lineEdit_tab4_1")
        self.horizontalLayout_tab4_1.addWidget(self.lineEdit_tab4_1)

        self.pushButton_tab4_1 = QtWidgets.QPushButton(self.tab_4)
        # self.pushButton_tab4_1.setMaximumSize(QtCore.QSize(75, 25))
        self.pushButton_tab4_1.clicked.connect(partial(self.select_file, "Text files (*.txt)", self.lineEdit_tab4_1))
        self.pushButton_tab4_1.setObjectName("pushButton_tab4_1")
        self.horizontalLayout_tab4_1.addWidget(self.pushButton_tab4_1)

        self.verticalLayout_tab4_1.addLayout(self.horizontalLayout_tab4_1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab4_1.addItem(spacerItem17)
        self.horizontalLayout_tab4_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab4_2.setObjectName("horizontalLayout_tab4_2")
        self.lineEdit_tab4_2 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_tab4_2.setObjectName("lineEdit_tab4_2")
        self.horizontalLayout_tab4_2.addWidget(self.lineEdit_tab4_2)

        self.pushButton_tab4_2 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_tab4_2.setObjectName("pushButton_tab4_2")
        self.pushButton_tab4_2.clicked.connect(partial(self.select_dir, self.lineEdit_tab4_2))
        self.horizontalLayout_tab4_2.addWidget(self.pushButton_tab4_2)

        self.verticalLayout_tab4_1.addLayout(self.horizontalLayout_tab4_2)
        spacerItem18 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab4_1.addItem(spacerItem18)
        self.horizontalLayout_tab4_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab4_3.setObjectName("horizontalLayout_tab4_3")

        self.pushButton_tab4_3 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_tab4_3.setObjectName("pushButton_tab4_3")
        self.pushButton_tab4_3.clicked.connect(self.scatter)
        self.horizontalLayout_tab4_3.addWidget(self.pushButton_tab4_3)

        self.verticalLayout_tab4_1.addLayout(self.horizontalLayout_tab4_3)
        self.verticalLayout_6.addLayout(self.verticalLayout_tab4_1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tabWidget.setCurrentWidget(self.tab_4)

        self.textEdit_tab4_1.setHtml(_translate("Form",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'KaiTi, SimSun, sans-serif\'; font-size:12pt; font-weight:bold; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">功能说明：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.对数据文件要求：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    存放数据的文件为txt文件；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第一列数值为x轴；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第二列数值为y轴；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第三列数值为分类属性；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.输入输出说明：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第一个输入框为：需要处理的txt文件的URL；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第二个输入框为：将处理后新生成的txt文件存放所在文件夹的URL；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.实现功能：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    按照分类属性对每一类进行上色，同一类为同一种颜色；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    按x,y分别为横轴和纵轴，进行散点的绘制；</p></body></html>"))
        self.pushButton_tab4_1.setText(_translate("Form", "..."))
        self.pushButton_tab4_2.setText(_translate("Form", "..."))
        self.pushButton_tab4_3.setText(_translate("Form", "处理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "散点图"))

    # ------------------ 点击按钮创建标签页-4 --终止 ------------------

    # ------------------ 点击按钮创建标签页-5 --起始 ------------------

    def createTab_5(self):
        _translate = QtCore.QCoreApplication.translate

        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_tab5_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_tab5_1.setObjectName("verticalLayout_tab5_1")
        self.textEdit_tab5_1 = QtWidgets.QTextEdit(self.tab_5)
        self.textEdit_tab5_1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.textEdit_tab5_1.setObjectName("textEdit_tab5_1")
        self.verticalLayout_tab5_1.addWidget(self.textEdit_tab5_1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab5_1.addItem(spacerItem19)
        self.horizontalLayout_tab5_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab5_1.setObjectName("horizontalLayout_tab5_1")

        self.lineEdit_tab5_1 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_tab5_1.setObjectName("lineEdit_tab5_1")
        self.horizontalLayout_tab5_1.addWidget(self.lineEdit_tab5_1)

        self.pushButton_tab5_1 = QtWidgets.QPushButton(self.tab_5)
        # self.pushButton_tab5_1.setMaximumSize(QtCore.QSize(75, 25))
        self.pushButton_tab5_1.setObjectName("pushButton_tab5_1")
        self.pushButton_tab5_1.clicked.connect(partial(self.select_file, "Text files (*.txt)", self.lineEdit_tab5_1))
        self.horizontalLayout_tab5_1.addWidget(self.pushButton_tab5_1)

        self.verticalLayout_tab5_1.addLayout(self.horizontalLayout_tab5_1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab5_1.addItem(spacerItem20)
        self.horizontalLayout_tab5_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab5_2.setObjectName("horizontalLayout_tab5_2")

        self.lineEdit_tab5_2 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_tab5_2.setObjectName("lineEdit_tab5_2")
        self.horizontalLayout_tab5_2.addWidget(self.lineEdit_tab5_2)

        self.pushButton_tab5_2 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_tab5_2.setObjectName("pushButton_tab5_2")
        self.pushButton_tab5_2.clicked.connect(partial(self.select_dir, self.lineEdit_tab5_2))
        self.horizontalLayout_tab5_2.addWidget(self.pushButton_tab5_2)

        self.verticalLayout_tab5_1.addLayout(self.horizontalLayout_tab5_2)
        spacerItem21 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab5_1.addItem(spacerItem21)
        self.horizontalLayout_tab5_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab5_3.setObjectName("horizontalLayout_tab5_3")

        self.pushButton_tab5_3 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_tab5_3.setObjectName("pushButton_tab5_3")
        self.pushButton_tab5_3.clicked.connect(self.line)
        self.horizontalLayout_tab5_3.addWidget(self.pushButton_tab5_3)

        self.verticalLayout_tab5_1.addLayout(self.horizontalLayout_tab5_3)
        self.verticalLayout_7.addLayout(self.verticalLayout_tab5_1)

        self.tabWidget.addTab(self.tab_5, "")
        self.tabWidget.setCurrentWidget(self.tab_5)

        self.textEdit_tab5_1.setHtml(_translate("Form",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'KaiTi, SimSun, sans-serif\'; font-size:12pt; font-weight:bold; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">功能说明：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.对数据文件要求：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    存放数据的文件为txt文件；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第一列数值为x轴；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第二列数值为分类属性；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第三列数值为y轴（数据）；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.输入输出说明：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第一个输入框为：需要处理的txt文件的URL；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第二个输入框为：将处理后新生成的txt文件存放所在文件夹的URL；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.实现功能：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    按照分类属性对每一类进行上色，同一类为同一种颜色；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    按x,y分别为横轴和纵轴，进行折线的绘制；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    在每类最高点标上数据；</p></body></html>"))
        self.pushButton_tab5_1.setText(_translate("Form", "..."))
        self.pushButton_tab5_2.setText(_translate("Form", "..."))
        self.pushButton_tab5_3.setText(_translate("Form", "处理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "折线图"))

    # ------------------ 点击按钮创建标签页-5 --终止 ------------------

    # ------------------ 点击按钮创建标签页-6 --起始 ------------------

    def createTab_6(self):
        _translate = QtCore.QCoreApplication.translate

        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_tab6_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_tab6_1.setObjectName("verticalLayout_tab6_1")
        self.textEdit_tab6_1 = QtWidgets.QTextEdit(self.tab_6)
        self.textEdit_tab6_1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.textEdit_tab6_1.setObjectName("textEdit_tab6_1")
        self.verticalLayout_tab6_1.addWidget(self.textEdit_tab6_1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab6_1.addItem(spacerItem22)
        self.horizontalLayout_tab6_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab6_1.setObjectName("horizontalLayout_tab6_1")

        self.lineEdit_tab6_1 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_tab6_1.setObjectName("lineEdit_tab6_1")
        self.horizontalLayout_tab6_1.addWidget(self.lineEdit_tab6_1)

        self.pushButton_tab6_1 = QtWidgets.QPushButton(self.tab_6)
        # self.pushButton_tab6_1.setMaximumSize(QtCore.QSize(75, 25))
        self.pushButton_tab6_1.setObjectName("pushButton_tab6_1")
        self.pushButton_tab6_1.clicked.connect(partial(self.select_file, "Text files (*.txt)", self.lineEdit_tab6_1))

        self.horizontalLayout_tab6_1.addWidget(self.pushButton_tab6_1)

        self.verticalLayout_tab6_1.addLayout(self.horizontalLayout_tab6_1)
        spacerItem23 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab6_1.addItem(spacerItem23)
        self.horizontalLayout_tab6_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab6_2.setObjectName("horizontalLayout_tab6_2")

        self.lineEdit_tab6_2 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_tab6_2.setObjectName("lineEdit_tab6_2")
        self.horizontalLayout_tab6_2.addWidget(self.lineEdit_tab6_2)

        self.pushButton_tab6_2 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_tab6_2.setObjectName("pushButton_tab6_2")
        self.pushButton_tab6_2.clicked.connect(partial(self.select_dir, self.lineEdit_tab6_2))
        self.horizontalLayout_tab6_2.addWidget(self.pushButton_tab6_2)

        self.verticalLayout_tab6_1.addLayout(self.horizontalLayout_tab6_2)
        spacerItem24 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab6_1.addItem(spacerItem24)
        self.horizontalLayout_tab6_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab6_3.setObjectName("horizontalLayout_tab6_3")
        self.pushButton_tab6_3 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_tab6_3.setObjectName("pushButton_tab6_3")
        self.pushButton_tab6_3.clicked.connect(self.bar)
        self.horizontalLayout_tab6_3.addWidget(self.pushButton_tab6_3)
        self.verticalLayout_tab6_1.addLayout(self.horizontalLayout_tab6_3)
        self.verticalLayout_8.addLayout(self.verticalLayout_tab6_1)

        self.tabWidget.addTab(self.tab_6, "")
        self.tabWidget.setCurrentWidget(self.tab_6)

        self.textEdit_tab6_1.setHtml(_translate("Form",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'KaiTi, SimSun, sans-serif\'; font-size:12pt; font-weight:bold; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">功能说明：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.对数据文件要求：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    存放数据的文件为txt文件；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第一列数值为y轴（数据）；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第二列数值为分类小组（对比柱状）；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第三列数值为分类大组（并列柱状）；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.输入输出说明：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第一个输入框为：需要处理的txt文件的URL；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第二个输入框为：将处理后新生成的txt文件存放所在文件夹的URL；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.实现功能：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    按照分类属性对每一柱状进行上色，同一大组为同一种颜色；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    按x,y分别为横轴和纵轴，横轴进行组号的标识，纵轴是数据，进行折线的绘制；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    在每一柱状的顶端标上数据；</p></body></html>"))
        self.pushButton_tab6_1.setText(_translate("Form", "..."))
        self.pushButton_tab6_2.setText(_translate("Form", "..."))
        self.pushButton_tab6_3.setText(_translate("Form", "处理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "柱状图"))

    # ------------------ 点击按钮创建标签页-6 --终止 ------------------

    # ------------------ 点击按钮创建标签页-7 --起始 ------------------

    def createTab_7(self):
        _translate = QtCore.QCoreApplication.translate

        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.tab_7)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.verticalLayout_tab7_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_tab7_1.setObjectName("verticalLayout_tab7_1")
        self.textEdit_tab7_1 = QtWidgets.QTextEdit(self.tab_7)
        self.textEdit_tab7_1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.textEdit_tab7_1.setObjectName("textEdit_tab7_1")
        self.verticalLayout_tab7_1.addWidget(self.textEdit_tab7_1)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab7_1.addItem(spacerItem25)
        self.horizontalLayout_tab7_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab7_1.setObjectName("horizontalLayout_tab7_1")
        self.lineEdit_tab7_1 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_tab7_1.setObjectName("lineEdit_tab7_1")
        self.horizontalLayout_tab7_1.addWidget(self.lineEdit_tab7_1)
        self.pushButton_tab7_1 = QtWidgets.QPushButton(self.tab_7)
        # self.pushButton_tab7_1.setMaximumSize(QtCore.QSize(75, 25))
        self.pushButton_tab7_1.setObjectName("pushButton_tab7_1")
        self.pushButton_tab7_1.clicked.connect(partial(self.select_file, "Text files (*.txt)", self.lineEdit_tab7_1))

        self.horizontalLayout_tab7_1.addWidget(self.pushButton_tab7_1)
        self.verticalLayout_tab7_1.addLayout(self.horizontalLayout_tab7_1)
        spacerItem26 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab7_1.addItem(spacerItem26)
        self.horizontalLayout_tab7_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab7_2.setObjectName("horizontalLayout_tab7_2")

        self.lineEdit_tab7_2 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_tab7_2.setObjectName("lineEdit_tab7_2")
        self.horizontalLayout_tab7_2.addWidget(self.lineEdit_tab7_2)

        self.pushButton_tab7_2 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_tab7_2.setObjectName("pushButton_tab7_2")
        self.pushButton_tab7_2.clicked.connect(partial(self.select_dir, self.lineEdit_tab7_2))
        self.horizontalLayout_tab7_2.addWidget(self.pushButton_tab7_2)

        self.verticalLayout_tab7_1.addLayout(self.horizontalLayout_tab7_2)
        spacerItem27 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab7_1.addItem(spacerItem27)
        self.horizontalLayout_tab7_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab7_3.setObjectName("horizontalLayout_tab7_3")
        self.pushButton_tab7_3 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_tab7_3.setObjectName("pushButton_tab7_3")
        self.pushButton_tab7_3.clicked.connect(self.pie)
        self.horizontalLayout_tab7_3.addWidget(self.pushButton_tab7_3)
        self.verticalLayout_tab7_1.addLayout(self.horizontalLayout_tab7_3)
        self.verticalLayout_17.addLayout(self.verticalLayout_tab7_1)

        self.tabWidget.addTab(self.tab_7, "")
        self.tabWidget.setCurrentWidget(self.tab_7)

        self.textEdit_tab7_1.setHtml(_translate("Form",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'KaiTi, SimSun, sans-serif\'; font-size:12pt; font-weight:bold; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">功能说明：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.对数据文件要求：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    存放数据的文件为txt文件；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第一列为数据；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第二列为分类；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.输入输出说明：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第一个输入框为：需要处理的txt文件的URL；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第二个输入框为：将处理后新生成的txt文件存放所在文件夹的URL；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.实现功能：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    按照分类对每一区域进行不同颜色的上色；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    每一区域标上百分比数据；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    区域外标明类别；</p></body></html>"))
        self.pushButton_tab7_1.setText(_translate("Form", "..."))
        self.pushButton_tab7_2.setText(_translate("Form", "..."))
        self.pushButton_tab7_3.setText(_translate("Form", "处理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Form", "饼状图"))

    # ------------------ 点击按钮创建标签页-7 --终止 ------------------

    # ------------------ 点击按钮创建标签页-8 --起始 ------------------

    def createTab_8(self):
        _translate = QtCore.QCoreApplication.translate

        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.tab_8)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.verticalLayout_tab8_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_tab8_1.setObjectName("verticalLayout_tab8_1")
        self.textEdit_tab8_1 = QtWidgets.QTextEdit(self.tab_8)
        self.textEdit_tab8_1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.textEdit_tab8_1.setObjectName("textEdit_tab8_1")
        self.verticalLayout_tab8_1.addWidget(self.textEdit_tab8_1)
        spacerItem28 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab8_1.addItem(spacerItem28)
        self.horizontalLayout_tab8_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab8_1.setObjectName("horizontalLayout_tab8_1")

        self.lineEdit_tab8_1 = QtWidgets.QLineEdit(self.tab_8)
        self.lineEdit_tab8_1.setObjectName("lineEdit_tab8_1")
        self.horizontalLayout_tab8_1.addWidget(self.lineEdit_tab8_1)

        self.pushButton_tab8_1 = QtWidgets.QPushButton(self.tab_8)
        # self.pushButton_tab8_1.setMaximumSize(QtCore.QSize(75, 25))
        self.pushButton_tab8_1.setObjectName("pushButton_tab8_1")
        self.pushButton_tab8_1.clicked.connect(partial(self.select_file, "Text files (*.txt)", self.lineEdit_tab8_1))
        self.horizontalLayout_tab8_1.addWidget(self.pushButton_tab8_1)

        self.verticalLayout_tab8_1.addLayout(self.horizontalLayout_tab8_1)
        spacerItem29 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab8_1.addItem(spacerItem29)
        self.horizontalLayout_tab8_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab8_2.setObjectName("horizontalLayout_tab8_2")
        self.lineEdit_tab8_2 = QtWidgets.QLineEdit(self.tab_8)
        self.lineEdit_tab8_2.setObjectName("lineEdit_tab8_2")
        self.horizontalLayout_tab8_2.addWidget(self.lineEdit_tab8_2)

        self.pushButton_tab8_2 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_tab8_2.setObjectName("pushButton_tab8_2")
        self.pushButton_tab8_2.clicked.connect(partial(self.select_dir, self.lineEdit_tab8_2))
        self.horizontalLayout_tab8_2.addWidget(self.pushButton_tab8_2)

        self.verticalLayout_tab8_1.addLayout(self.horizontalLayout_tab8_2)
        spacerItem30 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab8_1.addItem(spacerItem30)
        self.horizontalLayout_tab8_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab8_3.setObjectName("horizontalLayout_tab8_3")
        self.pushButton_tab8_3 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_tab8_3.setObjectName("pushButton_tab8_3")
        self.pushButton_tab8_3.clicked.connect(self.heatmap)
        self.horizontalLayout_tab8_3.addWidget(self.pushButton_tab8_3)

        self.verticalLayout_tab8_1.addLayout(self.horizontalLayout_tab8_3)
        self.verticalLayout_19.addLayout(self.verticalLayout_tab8_1)

        self.tabWidget.addTab(self.tab_8, "")
        self.tabWidget.setCurrentWidget(self.tab_8)

        self.textEdit_tab8_1.setHtml(_translate("Form",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'KaiTi, SimSun, sans-serif\'; font-size:12pt; font-weight:bold; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">功能说明：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.对数据文件要求：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    存放数据的文件为txt文件；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    数据必须为：转录组经RPKM/FPKM标准化的基因表达数据，但无需进行Person相关系数的计算；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第一列为基因名；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    其余列均为基因表达数据中的样本；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.输入输出说明：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第一个输入框为：需要处理的txt文件的URL；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第二个输入框为：将处理后新生成的txt文件存放所在文件夹的URL；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.实现功能：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    对数据进行Person相关系数的计算后，绘制热力图；</p></body></html>"))
        self.pushButton_tab8_1.setText(_translate("Form", "..."))
        self.pushButton_tab8_2.setText(_translate("Form", "..."))
        self.pushButton_tab8_3.setText(_translate("Form", "处理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("Form", "热力图"))

    # ------------------ 点击按钮创建标签页-8 --终止 ------------------

    # ------------------ 点击按钮创建标签页-9 --起始 ------------------

    def createTab_9(self):
        _translate = QtCore.QCoreApplication.translate

        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.tab_9)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.verticalLayout_tab9_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_tab9_1.setObjectName("verticalLayout_tab9_1")
        self.textEdit_tab9_1 = QtWidgets.QTextEdit(self.tab_9)
        self.textEdit_tab9_1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.textEdit_tab9_1.setObjectName("textEdit_tab9_1")
        self.verticalLayout_tab9_1.addWidget(self.textEdit_tab9_1)
        spacerItem31 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab9_1.addItem(spacerItem31)
        self.horizontalLayout_tab9_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab9_1.setObjectName("horizontalLayout_tab9_1")

        self.lineEdit_tab9_1 = QtWidgets.QLineEdit(self.tab_9)
        self.lineEdit_tab9_1.setObjectName("lineEdit_tab9_1")
        self.horizontalLayout_tab9_1.addWidget(self.lineEdit_tab9_1)

        self.pushButton_tab9_1 = QtWidgets.QPushButton(self.tab_9)
        # self.pushButton_tab9_1.setMaximumSize(QtCore.QSize(75, 25))
        self.pushButton_tab9_1.setObjectName("pushButton_tab9_1")
        self.pushButton_tab9_1.clicked.connect(partial(self.select_file, "Text files (*.txt)", self.lineEdit_tab9_1))
        self.horizontalLayout_tab9_1.addWidget(self.pushButton_tab9_1)

        self.verticalLayout_tab9_1.addLayout(self.horizontalLayout_tab9_1)
        spacerItem32 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab9_1.addItem(spacerItem32)
        self.horizontalLayout_tab9_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab9_2.setObjectName("horizontalLayout_tab9_2")
        self.lineEdit_tab9_2 = QtWidgets.QLineEdit(self.tab_9)
        self.lineEdit_tab9_2.setObjectName("lineEdit_tab9_2")
        self.horizontalLayout_tab9_2.addWidget(self.lineEdit_tab9_2)

        self.pushButton_tab9_2 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_tab9_2.setObjectName("pushButton_tab9_2")
        self.pushButton_tab9_2.clicked.connect(partial(self.select_dir, self.lineEdit_tab9_2))
        self.horizontalLayout_tab9_2.addWidget(self.pushButton_tab9_2)

        self.verticalLayout_tab9_1.addLayout(self.horizontalLayout_tab9_2)
        spacerItem33 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab9_1.addItem(spacerItem33)
        self.horizontalLayout_tab9_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab9_3.setObjectName("horizontalLayout_tab9_3")
        self.pushButton_tab9_3 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_tab9_3.setObjectName("pushButton_tab9_3")
        self.pushButton_tab9_3.clicked.connect(self.venn)
        self.horizontalLayout_tab9_3.addWidget(self.pushButton_tab9_3)

        self.verticalLayout_tab9_1.addLayout(self.horizontalLayout_tab9_3)
        self.verticalLayout_21.addLayout(self.verticalLayout_tab9_1)

        self.tabWidget.addTab(self.tab_9, "")
        self.tabWidget.setCurrentWidget(self.tab_9)

        self.textEdit_tab9_1.setHtml(_translate("Form",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'KaiTi, SimSun, sans-serif\'; font-size:12pt; font-weight:bold; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">功能说明：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.对数据文件要求：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    存放数据的文件为txt文件；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    每一列为基因的集合；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第一行为集合名；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.输入输出说明：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第一个输入框为：需要处理的txt文件的URL；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第二个输入框为：将处理后新生成的txt文件存放所在文件夹的URL；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.实现功能：</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    对所给数据进行venn图绘制；</p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    需要注意的是：暂时只能绘制6个集合以内包括6个集合的venn图；</p></body></html>"))
        self.pushButton_tab9_1.setText(_translate("Form", "..."))
        self.pushButton_tab9_2.setText(_translate("Form", "..."))
        self.pushButton_tab9_3.setText(_translate("Form", "处理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("Form", "venn图"))

    # ------------------ 点击按钮创建标签页-9 --终止 ------------------

    # ------------------ 点击按钮创建标签页-10 --起始 ------------------

    def createTab_10(self):
        _translate = QtCore.QCoreApplication.translate

        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")

        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.tab_10)
        self.verticalLayout_22.setObjectName("verticalLayout_22")

        self.verticalLayout_tab10_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_tab10_1.setObjectName("verticalLayout_tab10_1")

        self.textEdit_tab10_1 = QtWidgets.QTextEdit(self.tab_10)
        self.textEdit_tab10_1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.textEdit_tab10_1.setObjectName("textEdit_tab10_1")

        self.verticalLayout_tab10_1.addWidget(self.textEdit_tab10_1)

        spacerItem34 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab10_1.addItem(spacerItem34)

        self.horizontalLayout_tab10_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab10_1.setObjectName("horizontalLayout_tab10_1")

        self.lineEdit_tab10_1 = QtWidgets.QLineEdit(self.tab_10)
        self.lineEdit_tab10_1.setObjectName("lineEdit_tab10_1")
        self.horizontalLayout_tab10_1.addWidget(self.lineEdit_tab10_1)

        self.pushButton_tab10_1 = QtWidgets.QPushButton(self.tab_10)
        # self.pushButton_tab10_1.setMaximumSize(QtCore.QSize(75, 25))
        self.pushButton_tab10_1.setObjectName("pushButton_tab10_1")
        self.pushButton_tab10_1.clicked.connect(
            partial(self.select_file, "Text files (*.txt)", self.lineEdit_tab10_1))
        self.horizontalLayout_tab10_1.addWidget(self.pushButton_tab10_1)

        self.verticalLayout_tab10_1.addLayout(self.horizontalLayout_tab10_1)
        spacerItem35 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab10_1.addItem(spacerItem35)
        self.horizontalLayout_tab10_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab10_2.setObjectName("horizontalLayout_tab10_2")
        self.lineEdit_tab10_2 = QtWidgets.QLineEdit(self.tab_10)
        self.lineEdit_tab10_2.setObjectName("lineEdit_tab10_2")
        self.horizontalLayout_tab10_2.addWidget(self.lineEdit_tab10_2)

        self.pushButton_tab10_2 = QtWidgets.QPushButton(self.tab_10)
        self.pushButton_tab10_2.setObjectName("pushButton_tab10_2")
        self.pushButton_tab10_2.clicked.connect(partial(self.select_dir, self.lineEdit_tab10_2))
        self.horizontalLayout_tab10_2.addWidget(self.pushButton_tab10_2)

        self.verticalLayout_tab10_1.addLayout(self.horizontalLayout_tab10_2)
        spacerItem36 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab10_1.addItem(spacerItem36)
        self.horizontalLayout_tab10_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab10_3.setObjectName("horizontalLayout_tab10_3")
        self.pushButton_tab10_3 = QtWidgets.QPushButton(self.tab_10)
        self.pushButton_tab10_3.setObjectName("pushButton_tab10_3")
        self.pushButton_tab10_3.clicked.connect(self.stru)
        self.horizontalLayout_tab10_3.addWidget(self.pushButton_tab10_3)

        self.verticalLayout_tab10_1.addLayout(self.horizontalLayout_tab10_3)
        self.verticalLayout_22.addLayout(self.verticalLayout_tab10_1)

        self.tabWidget.addTab(self.tab_10, "")
        self.tabWidget.setCurrentWidget(self.tab_10)

        self.textEdit_tab10_1.setHtml(_translate("Form",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'KaiTi, SimSun, sans-serif\'; font-size:12pt; font-weight:bold; font-style:normal;\">\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">功能说明：</p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.对数据文件要求：</p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    存放数据的文件为txt文件；</p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    每一行均为基因名+染色体+起始位置+终止位置+链方向+一个包含外显子坐标的列表，用单个空格分开；</p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.输入输出说明：</p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第一个输入框为：需要处理的txt文件的URL；</p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第二个输入框为：将处理后新生成的txt文件存放所在文件夹的URL；</p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.实现功能：</p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    横坐标为基因位置，纵坐标为基因名；</p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    同一基因中的每个外显子用不同颜色表示；</p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    根据链方向不同，正链剪头向右，负链剪头向左；</p></body></html>"))
        self.pushButton_tab10_1.setText(_translate("Form", "..."))
        self.pushButton_tab10_2.setText(_translate("Form", "..."))
        self.pushButton_tab10_3.setText(_translate("Form", "处理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("Form", "基因结构"))

        # ------------------ 点击按钮创建标签页-10 --终止 ------------------

        # ------------------ 点击按钮创建标签页-11 --起始 ------------------

    def createTab_11(self):
        _translate = QtCore.QCoreApplication.translate

        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.tab_11)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.verticalLayout_tab11_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_tab11_1.setObjectName("verticalLayout_tab11_1")
        self.textEdit_tab11_1 = QtWidgets.QTextEdit(self.tab_11)
        self.textEdit_tab11_1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.textEdit_tab11_1.setObjectName("textEdit_tab11_1")
        self.verticalLayout_tab11_1.addWidget(self.textEdit_tab11_1)
        spacerItem37 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab11_1.addItem(spacerItem37)
        self.horizontalLayout_tab11_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab11_1.setObjectName("horizontalLayout_tab11_1")

        self.lineEdit_tab11_1 = QtWidgets.QLineEdit(self.tab_11)
        self.lineEdit_tab11_1.setObjectName("lineEdit_tab11_1")
        self.horizontalLayout_tab11_1.addWidget(self.lineEdit_tab11_1)

        self.pushButton_tab11_1 = QtWidgets.QPushButton(self.tab_11)
        # self.pushButton_tab11_1.setMaximumSize(QtCore.QSize(75, 25))
        self.pushButton_tab11_1.setObjectName("pushButton_tab11_1")
        self.pushButton_tab11_1.clicked.connect(
            partial(self.select_file, "Text files (*.txt)", self.lineEdit_tab11_1))
        self.horizontalLayout_tab11_1.addWidget(self.pushButton_tab11_1)

        self.verticalLayout_tab11_1.addLayout(self.horizontalLayout_tab11_1)
        spacerItem38 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab11_1.addItem(spacerItem38)
        self.horizontalLayout_tab11_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab11_2.setObjectName("horizontalLayout_tab11_2")
        self.lineEdit_tab11_2 = QtWidgets.QLineEdit(self.tab_11)
        self.lineEdit_tab11_2.setObjectName("lineEdit_tab11_2")
        self.horizontalLayout_tab11_2.addWidget(self.lineEdit_tab11_2)

        self.pushButton_tab11_2 = QtWidgets.QPushButton(self.tab_11)
        self.pushButton_tab11_2.setObjectName("pushButton_tab11_2")
        self.pushButton_tab11_2.clicked.connect(partial(self.select_dir, self.lineEdit_tab11_2))
        self.horizontalLayout_tab11_2.addWidget(self.pushButton_tab11_2)

        self.verticalLayout_tab11_1.addLayout(self.horizontalLayout_tab11_2)
        spacerItem39 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_tab11_1.addItem(spacerItem39)
        self.horizontalLayout_tab11_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tab11_3.setObjectName("horizontalLayout_tab11_3")

        self.pushButton_tab11_3 = QtWidgets.QPushButton(self.tab_11)
        self.pushButton_tab11_3.setObjectName("pushButton_tab11_3")
        self.pushButton_tab11_3.clicked.connect(self.tree)
        self.horizontalLayout_tab11_3.addWidget(self.pushButton_tab11_3)

        self.verticalLayout_tab11_1.addLayout(self.horizontalLayout_tab11_3)
        self.verticalLayout_23.addLayout(self.verticalLayout_tab11_1)

        self.tabWidget.addTab(self.tab_11, "")
        self.tabWidget.setCurrentWidget(self.tab_11)

        self.textEdit_tab11_1.setHtml(_translate("Form",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'KaiTi, SimSun, sans-serif\'; font-size:12pt; font-weight:bold; font-style:normal;\">\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">功能说明：</p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.对数据文件要求：</p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    存放数据的文件为txt文件；</p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    每一行均为基因名+染色体+起始位置+终止位置+链方向+一个包含外显子坐标的列表，坐标用双引号引起来，用逗号分开，数据之间用单个空格分开；</p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    倒数第二行格式为：&quot;<span style=\" text-decoration: underline;\">#GENE TREE</span>&quot;；</p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    最后一行为基因树结构，同一棵树的基因用(A,B)形式标识；</p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.输入输出说明：</p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第一个输入框为：需要处理的txt文件的URL；</p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    第二个输入框为：将处理后新生成的txt文件存放所在文件夹的URL；</p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.实现功能：</p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    绘制基因树和基因，并为基因上色；</p></body></html>"))
        self.pushButton_tab11_1.setText(_translate("Form", "..."))
        self.pushButton_tab11_2.setText(_translate("Form", "..."))
        self.pushButton_tab11_3.setText(_translate("Form", "处理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), _translate("Form", "进化树"))

    # ------------------ 点击按钮创建标签页-11 --终止 ------------------

    # ------------------  文件和文件夹选择功能--起始 ------------------
    # 文件选择
    def select_file(self, format, wid):
        # 创建一个文件选择对话框
        file_dialog = QFileDialog()
        # 设置文件选择模式为 ExistingFile，表示只能选择已存在的文件
        file_dialog.setFileMode(QFileDialog.ExistingFile)

        # 设置文件过滤器 Text files (*.txt);;Fasta files (*.fasta);;GFF3 files (*.gff3);;
        # file_dialog.setFileMode(QFileDialog.DirectoryOnly) 只显示文件夹
        file_dialog.setNameFilter(format)

        # 设置文件选择对话框的视图模式为详细信息
        file_dialog.setViewMode(QFileDialog.Detail)

        # 打开文件选择对话框，并等待用户选择
        if file_dialog.exec_():
            # 获取用户选择的文件路径列表
            selected_files = file_dialog.selectedFiles()  # 列表的形式
            # 如果用户选择了文件，则将文件路径设置为 QLineEdit 的文本
            if selected_files:
                file_path_tab_1_1 = selected_files[0]  # 获取列表[0]，即文件路径
                wid.setText(file_path_tab_1_1)

    # 文件夹选择
    def select_dir(self, wid):
        # 创建一个文件选择对话框
        file_dialog = QFileDialog()
        # 设置文件选择模式为 ExistingFile，表示只能选择已存在的文件
        file_dialog.setFileMode(QFileDialog.ExistingFile)

        # 设置文件过滤器 Text files (*.txt);;Fasta files (*.fasta);;GFF3 files (*.gff3);;
        # file_dialog.setFileMode(QFileDialog.DirectoryOnly) 只显示文件夹
        file_dialog.setFileMode(QFileDialog.DirectoryOnly)

        # 设置文件选择对话框的视图模式为详细信息
        file_dialog.setViewMode(QFileDialog.Detail)

        # 打开文件选择对话框，并等待用户选择
        if file_dialog.exec_():
            # 获取用户选择的文件路径列表
            selected_files = file_dialog.selectedFiles()  # 列表的形式
            # 如果用户选择了文件，则将文件路径设置为 QLineEdit 的文本
            if selected_files:
                file_path = selected_files[0]  # 获取列表[0]，即文件路径
                wid.setText(file_path)

    # ------------------  文件和文件夹选择功能--终止 ------------------

    # ------------------ 读取属性值函数 --起始 ------------------

    def get_lineEdit_tab1_1_text(self):
        return self.lineEdit_tab1_1.text()

    def get_lineEdit_tab1_2_text(self):
        return self.lineEdit_tab1_2.text()

    def get_spinBox_tab1_1_value(self):
        return self.spinBox_tab1_1.value()

    def get_spinBox_tab1_2_value(self):
        return self.spinBox_tab1_2.value()

    def get_lineEdit_tab2_1_text(self):
        return self.lineEdit_tab2_1.text()

    def get_lineEdit_tab2_3_text(self):
        return self.lineEdit_tab2_3.text()

    def get_comboBox_tab2_1_text(self):
        return self.comboBox_tab2_1.currentText()

    def get_comboBox_tab2_2_text(self):
        return self.comboBox_tab2_2.currentText()

    def get_lineEdit_tab3_1_text(self):
        return self.lineEdit_tab3_1.text()

    def get_lineEdit_tab3_2_text(self):
        return self.lineEdit_tab3_2.text()

    def get_spinBox_tab3_1_value(self):
        return self.spinBox_tab3_1.value()

    def get_spinBox_tab3_2_value(self):
        return self.spinBox_tab3_2.value()

    def get_lineEdit_tab4_1_text(self):
        return self.lineEdit_tab4_1.text()

    def get_lineEdit_tab4_2_text(self):
        return self.lineEdit_tab4_2.text()

    def get_lineEdit_tab5_1_text(self):
        return self.lineEdit_tab5_1.text()

    def get_lineEdit_tab5_2_text(self):
        return self.lineEdit_tab5_2.text()

    def get_lineEdit_tab6_1_text(self):
        return self.lineEdit_tab6_1.text()

    def get_lineEdit_tab6_2_text(self):
        return self.lineEdit_tab6_2.text()

    def get_lineEdit_tab7_1_text(self):
        return self.lineEdit_tab7_1.text()

    def get_lineEdit_tab7_2_text(self):
        return self.lineEdit_tab7_2.text()

    def get_lineEdit_tab8_1_text(self):
        return self.lineEdit_tab8_1.text()

    def get_lineEdit_tab8_2_text(self):
        return self.lineEdit_tab8_2.text()

    def get_lineEdit_tab9_1_text(self):
        return self.lineEdit_tab9_1.text()

    def get_lineEdit_tab9_2_text(self):
        return self.lineEdit_tab9_2.text()

    def get_lineEdit_tab10_1_text(self):
        return self.lineEdit_tab10_1.text()

    def get_lineEdit_tab10_2_text(self):
        return self.lineEdit_tab10_2.text()

    def get_lineEdit_tab11_1_text(self):
        return self.lineEdit_tab11_1.text()

    def get_lineEdit_tab11_2_text(self):
        return self.lineEdit_tab11_2.text()

    # ------------------ 读取属性值函数 --终止 ------------------

    # ------------------ 线程函数 --起始 ------------------

    # 截取函数
    def slic(self):
        # 创建并启动工作线程
        self.worker_thread_1 = Thread_function_1()
        self.worker_thread_1.finished_signal.connect(self.fileCreationFinished)
        self.worker_thread_1.start()

    # 计算GC含量函数
    def gch(self):
        self.worker_thread_2 = Thread_function_2()
        self.worker_thread_2.finished_signal.connect(self.fileCreationFinished)
        self.worker_thread_2.start()

    def sbs(self):
        # 创建并启动工作线程
        self.worker_thread_3 = Thread_function_3()
        self.worker_thread_3.finished_signal.connect(self.fileCreationFinished)
        self.worker_thread_3.start()

    def cs(self):
        # 创建并启动工作线程
        self.worker_thread_4 = Thread_function_4()
        self.worker_thread_4.finished_signal.connect(self.fileCreationFinished)
        self.worker_thread_4.start()

    def rcs(self):
        # 创建并启动工作线程
        self.worker_thread_5 = Thread_function_5()
        self.worker_thread_5.finished_signal.connect(self.fileCreationFinished)
        self.worker_thread_5.start()

    def gl(self):
        # 创建并启动工作线程
        self.worker_thread_6 = Thread_function_6()
        self.worker_thread_6.finished_signal.connect(self.fileCreationFinished)
        self.worker_thread_6.start()

    def gff(self):
        # 创建并启动工作线程
        self.worker_thread_7 = Thread_function_7()
        self.worker_thread_7.finished_signal.connect(self.fileCreationFinished)
        self.worker_thread_7.start()

    def scatter(self):
        # 创建并启动工作线程
        self.worker_thread_8 = Thread_function_8()
        self.worker_thread_8.finished_signal.connect(self.fileCreationFinished)
        self.worker_thread_8.start()

    def line(self):
        # 创建并启动工作线程
        self.worker_thread_9 = Thread_function_9()
        self.worker_thread_9.finished_signal.connect(self.fileCreationFinished)
        self.worker_thread_9.start()

    def bar(self):
        # 创建并启动工作线程
        self.worker_thread_10 = Thread_function_10()
        self.worker_thread_10.finished_signal.connect(self.fileCreationFinished)
        self.worker_thread_10.start()

    def pie(self):
        # 创建并启动工作线程
        self.worker_thread_11 = Thread_function_11()
        self.worker_thread_11.finished_signal.connect(self.fileCreationFinished)
        self.worker_thread_11.start()

    def heatmap(self):
        # 创建并启动工作线程
        self.worker_thread_12 = Thread_function_12()
        self.worker_thread_12.finished_signal.connect(self.fileCreationFinished)
        self.worker_thread_12.start()

    def venn(self):
        # 创建并启动工作线程
        self.worker_thread_13 = Thread_function_13()
        self.worker_thread_13.finished_signal.connect(self.fileCreationFinished)
        self.worker_thread_13.start()

    def stru(self):
        # 创建并启动工作线程
        self.worker_thread_14 = Thread_function_14()
        self.worker_thread_14.finished_signal.connect(self.fileCreationFinished)
        self.worker_thread_14.start()

    def tree(self):
        # 创建并启动工作线程
        self.worker_thread_15 = Thread_function_15()
        self.worker_thread_15.finished_signal.connect(self.fileCreationFinished)
        self.worker_thread_15.start()

    # 处理完成后，线程结束，执行函数
    def fileCreationFinished(self):
        # 处理文件创建完成后操作
        # ------------------ 提示对话框 --起始 ------------------
        # 创建 QMessageBox
        msg_box = QMessageBox()

        # 设置标题
        msg_box.setWindowTitle("")

        # 设置消息文本
        msg_text = "处理完成！"
        msg_box.setText(msg_text)

        # 设置字体大小
        font = QFont()
        font.setPointSize(16)  # 设置字体大小
        msg_box.setFont(font)

        # 设置图标
        msg_box.setIcon(QMessageBox.Information)

        # 添加 OK 按钮
        ok_button = QPushButton("OK")
        ok_button.setFont(font)
        ok_button.setStyleSheet("font-size: 12pt;")  # 设置按钮字体大小
        msg_box.addButton(ok_button, QMessageBox.AcceptRole)

        # 调整按钮布局，让 OK 按钮居中
        msg_box_layout = msg_box.layout()
        if msg_box_layout is not None:
            button_box = msg_box_layout.itemAt(msg_box_layout.count() - 1)
            if button_box is not None:
                button_box.setAlignment(Qt.AlignCenter)
        # 显示对话框
        msg_box.exec_()
        # ------------------ 提示对话框 --终止 ------------------
    # ------------------ 线程函数 --终止 ------------------


# 主程序
app = QtWidgets.QApplication(sys.argv)
Form_w = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form_w)
Form_w.show()


# ------------------ 功能函数 --起始 ------------------

# 截取序列函数
def slicing_tab1():
    text_value_tab1_1 = ui.get_lineEdit_tab1_1_text()
    text_value_tab1_2 = ui.get_lineEdit_tab1_2_text()

    read_tab1_1 = text_value_tab1_1

    # 获取当前时间的字符串表示（包含秒）
    current_time_str = datetime.now().strftime("%Y_%m_%d_%H%M%S")

    write_tab1_1 = str(text_value_tab1_2) + "/sling-" + current_time_str + ".txt"

    start_tab1_1 = str(ui.get_spinBox_tab1_1_value())
    # print(start, type(start))
    end_tab1_1 = str(ui.get_spinBox_tab1_2_value())

    slicing(read_tab1_1, write_tab1_1, start_tab1_1, end_tab1_1)


def gc_tab1():
    text_value_1_tab1_1 = ui.get_lineEdit_tab1_1_text()
    text_value_2_tab1_1 = ui.get_lineEdit_tab1_2_text()

    read_tab1_2 = text_value_1_tab1_1

    # 获取当前时间的字符串表示（包含秒）
    current_time_str = datetime.now().strftime("%Y_%m_%d_%H%M%S")

    write_tab1_2 = str(text_value_2_tab1_1) + "/gc-" + current_time_str + ".txt"

    gc_calculation(read_tab1_2, write_tab1_2)


def sbs_tab2():
    text_value_tab2_1 = ui.get_lineEdit_tab2_1_text()
    text_value_tab2_3 = ui.get_lineEdit_tab2_3_text()

    read_tab2_1 = text_value_tab2_1

    # 获取当前时间的字符串表示（包含秒）
    current_time_str = datetime.now().strftime("%Y_%m_%d_%H%M%S")

    write_tab2_1 = str(text_value_tab2_3) + "/sbs-" + current_time_str + ".fasta"

    raw_tab2_1 = str(ui.get_comboBox_tab2_1_text())

    process_tab2_1 = str(ui.get_comboBox_tab2_2_text())

    single_base_substitution(read_tab2_1, write_tab2_1, raw_tab2_1, process_tab2_1)


def cs_tab2():
    text_value_tab2_1 = ui.get_lineEdit_tab2_1_text()
    text_value_tab2_3 = ui.get_lineEdit_tab2_3_text()

    read_tab2_1 = text_value_tab2_1

    # 获取当前时间的字符串表示（包含秒）
    current_time_str = datetime.now().strftime("%Y_%m_%d_%H%M%S")

    write_tab2_1 = str(text_value_tab2_3) + "/cs-" + current_time_str + ".fasta"

    complement_seq(read_tab2_1, write_tab2_1)


def rcs_tab2():
    text_value_tab2_1 = ui.get_lineEdit_tab2_1_text()
    text_value_tab2_3 = ui.get_lineEdit_tab2_3_text()

    read_tab2_1 = text_value_tab2_1

    # 获取当前时间的字符串表示（包含秒）
    current_time_str = datetime.now().strftime("%Y_%m_%d_%H%M%S")

    write_tab2_1 = str(text_value_tab2_3) + "/rcs-" + current_time_str + ".fasta"

    reverse_complement_seq(read_tab2_1, write_tab2_1)


def gl_tab2():
    text_value_tab2_1 = ui.get_lineEdit_tab2_1_text()
    text_value_tab2_3 = ui.get_lineEdit_tab2_3_text()

    read_tab2_1 = text_value_tab2_1

    # 获取当前时间的字符串表示（包含秒）
    current_time_str = datetime.now().strftime("%Y_%m_%d_%H%M%S")

    write_tab2_1 = str(text_value_tab2_3) + "/gl-" + current_time_str + ".fasta"

    get_length(read_tab2_1, write_tab2_1)


def gff_tab3():
    text_value_tab3_1 = ui.get_lineEdit_tab3_1_text()
    text_value_tab3_2 = ui.get_lineEdit_tab3_2_text()

    read_tab3_1 = text_value_tab3_1

    # 获取当前时间的字符串表示（包含秒）
    current_time_str = datetime.now().strftime("%Y_%m_%d_%H%M%S")

    write_tab3_1 = str(text_value_tab3_2) + "/gff-" + current_time_str + ".txt"

    start_tab3_1 = int(ui.get_spinBox_tab3_1_value())

    end_tab3_1 = int(ui.get_spinBox_tab3_2_value())

    filter_gff3(read_tab3_1, write_tab3_1, start_tab3_1, end_tab3_1)


def scatter_tab4():
    text_value_tab4_1 = ui.get_lineEdit_tab4_1_text()
    text_value_tab4_2 = ui.get_lineEdit_tab4_2_text()

    read_tab4_1 = text_value_tab4_1

    # 获取当前时间的字符串表示（包含秒）
    current_time_str = datetime.now().strftime("%Y_%m_%d_%H%M%S")

    write_tab4_1 = str(text_value_tab4_2) + "/scatter-" + current_time_str + ".png"

    scatter_plot(read_tab4_1, write_tab4_1)


def line_tab5():
    text_value_tab5_1 = ui.get_lineEdit_tab5_1_text()
    text_value_tab5_2 = ui.get_lineEdit_tab5_2_text()

    read_tab5_1 = text_value_tab5_1

    # 获取当前时间的字符串表示（包含秒）
    current_time_str = datetime.now().strftime("%Y_%m_%d_%H%M%S")

    write_tab5_1 = str(text_value_tab5_2) + "/line-" + current_time_str + ".png"

    line_plot(read_tab5_1, write_tab5_1)


def bar_tab6():
    text_value_tab6_1 = ui.get_lineEdit_tab6_1_text()
    text_value_tab6_2 = ui.get_lineEdit_tab6_2_text()

    read_tab6_1 = text_value_tab6_1

    # 获取当前时间的字符串表示（包含秒）
    current_time_str = datetime.now().strftime("%Y_%m_%d_%H%M%S")

    write_tab6_1 = str(text_value_tab6_2) + "/bar-" + current_time_str + ".png"

    bar_plot(read_tab6_1, write_tab6_1)


def pie_tab7():
    text_value_tab7_1 = ui.get_lineEdit_tab7_1_text()
    text_value_tab7_2 = ui.get_lineEdit_tab7_2_text()

    read_tab7_1 = text_value_tab7_1

    # 获取当前时间的字符串表示（包含秒）
    current_time_str = datetime.now().strftime("%Y_%m_%d_%H%M%S")

    write_tab7_1 = str(text_value_tab7_2) + "/pie-" + current_time_str + ".png"

    pie_plot(read_tab7_1, write_tab7_1)


def heatmap_tab8():
    text_value_tab8_1 = ui.get_lineEdit_tab8_1_text()
    text_value_tab8_2 = ui.get_lineEdit_tab8_2_text()

    read_tab8_1 = text_value_tab8_1

    # 获取当前时间的字符串表示（包含秒）
    current_time_str = datetime.now().strftime("%Y_%m_%d_%H%M%S")

    write_tab8_1 = str(text_value_tab8_2) + "/heatmap-" + current_time_str + ".png"

    heatmap_plot(read_tab8_1, write_tab8_1)


def venn_tab9():
    text_value_tab9_1 = ui.get_lineEdit_tab9_1_text()
    text_value_tab9_2 = ui.get_lineEdit_tab9_2_text()

    read_tab9_1 = text_value_tab9_1

    # 获取当前时间的字符串表示（包含秒）
    current_time_str = datetime.now().strftime("%Y_%m_%d_%H%M%S")

    write_tab9_1 = str(text_value_tab9_2) + "/venn-" + current_time_str + ".png"

    venn_plot(read_tab9_1, write_tab9_1)


def stru_tab10():
    text_value_tab10_1 = ui.get_lineEdit_tab10_1_text()
    text_value_tab10_2 = ui.get_lineEdit_tab10_2_text()

    read_tab10_1 = text_value_tab10_1

    # 获取当前时间的字符串表示（包含秒）
    current_time_str = datetime.now().strftime("%Y_%m_%d_%H%M%S")

    write_tab10_1 = str(text_value_tab10_2) + "/stru-" + current_time_str + ".png"

    genetic_structure(read_tab10_1, write_tab10_1)


def tree_tab11():
    text_value_tab11_1 = ui.get_lineEdit_tab11_1_text()
    text_value_tab11_2 = ui.get_lineEdit_tab11_2_text()

    read_tab11_1 = text_value_tab11_1

    # 获取当前时间的字符串表示（包含秒）
    current_time_str = datetime.now().strftime("%Y_%m_%d_%H%M%S")

    write_tab11_1 = str(text_value_tab11_2) + "/tree-" + current_time_str + ".png"

    genetic_tree(read_tab11_1, write_tab11_1)


# ------------------ 功能函数 --终止 ------------------

# 结束程序
sys.exit(app.exec_())
