# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import scipy.io as scio
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        # self.init_plot()#打开App时可以初始化图片
        # self.plot()

    def plot(self):

        timer = QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(100)

    def init_plot(self, data, date=1):

        data[date * 96: (date + 1) * 96].plot(ax=self.axes)
        self.draw()

    def update_figure(self, data, start_time, end_time):

        self.axes.cla()
        data.loc[start_time:end_time].plot(ax=self.axes)
        self.draw()


class Ui_MainWindow_show_plot(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 60, 879, 3))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 371, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 470, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 80, 261, 37))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 340, 263, 66))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.dateTimeEdit_start = QtWidgets.QDateTimeEdit(self.layoutWidget1)
        self.dateTimeEdit_start.setDateTime(QtCore.QDateTime(QtCore.QDate(2017, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit_start.setObjectName("dateTimeEdit_start")
        self.horizontalLayout_3.addWidget(self.dateTimeEdit_start)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.dateTimeEdit_end = QtWidgets.QDateTimeEdit(self.layoutWidget1)
        self.dateTimeEdit_end.setDateTime(QtCore.QDateTime(QtCore.QDate(2017, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit_end.setObjectName("dateTimeEdit_end")
        self.horizontalLayout_2.addWidget(self.dateTimeEdit_end)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 190, 266, 74))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox_station = QtWidgets.QComboBox(self.widget)
        self.comboBox_station.setObjectName("comboBox_station")
        self.comboBox_station.addItem("")
        self.comboBox_station.setItemText(0, "")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.comboBox_station.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_station)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.comboBox_datatype = QtWidgets.QComboBox(self.widget)
        self.comboBox_datatype.setObjectName("comboBox_datatype")
        self.comboBox_datatype.addItem("")
        self.comboBox_datatype.setItemText(0, "")
        self.comboBox_datatype.addItem("")
        self.comboBox_datatype.addItem("")
        self.comboBox_datatype.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_datatype)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.m = PlotCanvas(self, width=5, height=4.05)  # 实例化一个画布对象
        self.m.move(300, 145)

        self.comboBox_station.currentIndexChanged[str].connect(
            self.get_station_name)  # 条目发生改变，发射信号，传递条目内容
        self.comboBox_datatype.currentIndexChanged[str].connect(
            self.get_data_name)  # 条目发生改变，发射信号，传递条目内容

        # self.pushButton.clicked.connect(self.print_)
        self.pushButton.clicked.connect(self.load_data)
        self.pushButton.clicked.connect(self.plot_)

        self.pushButton_2.clicked.connect(self.show_dir)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">风电/光伏发电功率超短期预测模块</span></p><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "开始导入"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">数据导入：</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "打开文件夹"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">开始时间：</span></p></body></html>"))
        self.dateTimeEdit_start.setDisplayFormat(_translate("MainWindow", "yyyy/MM/dd HH-mm-ss"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">截止时间：</span></p></body></html>"))
        self.dateTimeEdit_end.setDisplayFormat(_translate("MainWindow", "yyyy/MM/dd HH-mm-ss"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">电站：</span></p></body></html>"))
        self.comboBox_station.setItemText(1, _translate("MainWindow", "风电1"))
        self.comboBox_station.setItemText(2, _translate("MainWindow", "风电2"))
        self.comboBox_station.setItemText(3, _translate("MainWindow", "风电3"))
        self.comboBox_station.setItemText(4, _translate("MainWindow", "风电4"))
        self.comboBox_station.setItemText(5, _translate("MainWindow", "风电5"))
        self.comboBox_station.setItemText(6, _translate("MainWindow", "风电6"))
        self.comboBox_station.setItemText(7, _translate("MainWindow", "风电7"))
        self.comboBox_station.setItemText(8, _translate("MainWindow", "风电8"))
        self.comboBox_station.setItemText(9, _translate("MainWindow", "风电9"))
        self.comboBox_station.setItemText(10, _translate("MainWindow", "风电10"))
        self.comboBox_station.setItemText(11, _translate("MainWindow", "风电11"))
        self.comboBox_station.setItemText(12, _translate("MainWindow", "风电12"))
        self.comboBox_station.setItemText(13, _translate("MainWindow", "风电13"))
        self.comboBox_station.setItemText(14, _translate("MainWindow", "风电14"))
        self.comboBox_station.setItemText(15, _translate("MainWindow", "风电15"))
        self.comboBox_station.setItemText(16, _translate("MainWindow", "风电16"))
        self.comboBox_station.setItemText(17, _translate("MainWindow", "风电17"))
        self.comboBox_station.setItemText(18, _translate("MainWindow", "风电18"))
        self.comboBox_station.setItemText(19, _translate("MainWindow", "风电19"))
        self.comboBox_station.setItemText(20, _translate("MainWindow", "风电20"))
        self.comboBox_station.setItemText(21, _translate("MainWindow", "光伏501"))
        self.comboBox_station.setItemText(22, _translate("MainWindow", "光伏502"))
        self.comboBox_station.setItemText(23, _translate("MainWindow", "光伏503"))
        self.comboBox_station.setItemText(24, _translate("MainWindow", "光伏504"))
        self.comboBox_station.setItemText(25, _translate("MainWindow", "光伏505"))
        self.comboBox_station.setItemText(26, _translate("MainWindow", "光伏506"))
        self.comboBox_station.setItemText(27, _translate("MainWindow", "光伏507"))
        self.comboBox_station.setItemText(28, _translate("MainWindow", "光伏508"))
        self.comboBox_station.setItemText(29, _translate("MainWindow", "光伏509"))
        self.comboBox_station.setItemText(30, _translate("MainWindow", "光伏510"))
        self.comboBox_station.setItemText(31, _translate("MainWindow", "光伏511"))
        self.comboBox_station.setItemText(32, _translate("MainWindow", "光伏512"))
        self.comboBox_station.setItemText(33, _translate("MainWindow", "光伏513"))
        self.comboBox_station.setItemText(34, _translate("MainWindow", "光伏514"))
        self.comboBox_station.setItemText(35, _translate("MainWindow", "光伏515"))
        self.comboBox_station.setItemText(36, _translate("MainWindow", "光伏516"))
        self.comboBox_station.setItemText(37, _translate("MainWindow", "光伏517"))
        self.comboBox_station.setItemText(38, _translate("MainWindow", "光伏518"))
        self.comboBox_station.setItemText(39, _translate("MainWindow", "光伏519"))
        self.comboBox_station.setItemText(40, _translate("MainWindow", "光伏520"))
        self.comboBox_station.setItemText(41, _translate("MainWindow", "光伏521"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">导入数据类型：</span></p></body></html>"))
        self.comboBox_datatype.setItemText(1, _translate("MainWindow", "功率"))
        self.comboBox_datatype.setItemText(2, _translate("MainWindow", "NWP温度"))
        self.comboBox_datatype.setItemText(3, _translate("MainWindow", "NWP风速"))

    def get_data_name(self, i):
        # 获取数据类型
        global data_
        data_ = i

    def get_station_name(self, i):
        # 获取电站类型
        global station_
        station_ = i

    def print_(self):
        # print(data_, station_)
        s = self.lineEdit.text()
        t = self.dateTimeEdit.text()

        print(t)

    def show_dir(self):

        global openfile_name

        openfile_name = QFileDialog.getExistingDirectory(self, '选择文件', '')

        # self.pushButton_2.set

    def load_data(self):
        global input_data

        if data_ == "功率":
            # 导入光伏数据
            if station_[:2] == "光伏":
                # TODO
                openfile_name_ = 'Power/'
                input_data = pd.read_csv(
                    openfile_name_ +
                    '/' +
                    str(station_[2:]) +
                    '.csv',
                    index_col=0,
                    parse_dates=True)
                # print(input_data[:10])
            elif station_[:2] == "风电":
                # TODO
                Power = scio.loadmat("wind_power_jilin.mat")
                df_wind_power = pd.DataFrame(Power['Power'])
                df_wind_power.index = pd.date_range(start='2017-01-01', periods=len(df_wind_power[0]), freq='15min')
                input_data = df_wind_power.iloc[:,int(station_[2:]-1)]

        elif data_[:3] == "NWP":
            # 导入NWP
            if station_[:2] == "光伏":
                dict = {501: 'CN0094',
                        502: 'CN0680',
                        503: 'CN0094',
                        504: 'CN0512',
                        505: 'CN0091',
                        506: 'CN0093',
                        507: 'CN0145',
                        508: 'CN0003',
                        509: 'CN0317',
                        510: 'CN0092',
                        511: 'CN0091',
                        513: 'CN0391',
                        514: 'CN0512',
                        515: 'CN0716',
                        516: 'CN0356',
                        517: 'CN0391',
                        518: 'CN0688',
                        519: 'CN0356',
                        520: 'CN0096',
                        521: 'CN0688'}
                # TODO
                # change openfile
                path_openfile_name = 'NWP/'
                input_data = pd.read_csv(path_openfile_name +
                                         dict[int(station_[2:])] +
                                         '.csv', index_col=2, parse_dates=True)
                # print(input_data[:10])
                if data_[3:] == '风速':
                    input_data = pd.DataFrame(input_data['windspeed_30'])
                elif data_[3:] == '温度':
                    input_data = pd.DataFrame(input_data['temperature'])

            elif station_[:2] == "风电":
                dict = {1: 'CN0001',
                        2: 'CN0002',
                        3: 'CN0003',
                        4: 'CN0004',
                        5: 'CN0005',
                        6: 'CN0006',
                        7: 'CN0001',
                        8: 'CN0360',
                        9: 'CN0090',
                        10: 'CN0091',
                        11: 'CN0001',
                        12: 'CN0092',
                        13: 'CN0096',
                        14: 'CN0093',
                        15: 'CN0094',
                        16: 'CN0095',
                        17: 'CN0356',
                        18: 'CN0121',
                        19: 'CN0138',
                        20: 'CN0137'}
                # TODO
                # change openfile
                path_openfile_name = 'NWP/'
                input_data = pd.read_csv(path_openfile_name +
                                         dict[int(station_[2:])] +
                                         '.csv', index_col=2, parse_dates=True)
                # print(input_data[:10])
                if data_[3:] == '风速':
                    input_data = pd.DataFrame(input_data['windspeed_30'])
                elif data_[3:] == '温度':
                    input_data = pd.DataFrame(input_data['temperature'])

    def str_datetime(self, t):
        import datetime

        t1, t2 = t.split(' ')
        year, month, day = t1.split('/')
        hour, minute, second = t2.split('-')

        date1 = datetime.datetime(
            int(year),
            int(month),
            int(day),
            int(hour),
            int(minute),
            0)

        return pd.Timestamp(date1)

    def plot_(self):

        import datetime
        start_time = self.dateTimeEdit_start.text()
        end_time = self.dateTimeEdit_end.text()
        print(input_data[:10])
        self.m.update_figure(
            input_data,
            self.str_datetime(start_time),
            self.str_datetime(end_time))
        # time1 = pd.Timestamp(datetime.datetime(2017,1,2,0,0,00))
        # time2 = pd.Timestamp(datetime.datetime(2017,1,3,0,0,00))
        # self.m.update_figure(input_data, time1, time2)

class MyWindow_show_plot(QMainWindow, Ui_MainWindow_show_plot):
    def __init__(self, parent=None):
        super(MyWindow_show_plot, self).__init__(parent)
        self.setupUi(self)

import sys
if __name__ == '__main__':
    # 字体随分辨率自适应
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    myWin = MyWindow_show_plot()
    myWin.show()

    sys.exit(app.exec_())