# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Code\Python\Morning Notification\morning.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

#From Qt
from PyQt5 import QtCore, QtGui, QtWidgets

#Weather modules
import pyowm
from datetime import date, datetime, timedelta

#File modules
from os import listdir
from os.path import isfile, join
import webbrowser
path = "E:\\Code\\Python\\Morning Notification\\notes" #remember need two \ due to regex
files = [x for x in listdir(path) if isfile(join(path, x)) and ".txt" in x]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 563))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setObjectName("tabWidget")
        self.home_tab = QtWidgets.QWidget()
        self.home_tab.setStyleSheet("")
        self.home_tab.setObjectName("home_tab")
        self.home_image = QtWidgets.QLabel(self.home_tab)
        self.home_image.setGeometry(QtCore.QRect(0, -30, 941, 621))
        self.home_image.setStyleSheet("image: url(:/newPrefix/760894.png);")
        self.home_image.setText("")
        self.home_image.setObjectName("home_image")
        self.home_date = QtWidgets.QLabel(self.home_tab)
        self.home_date.setGeometry(QtCore.QRect(390, 0, 371, 61))
        font = QtGui.QFont()
        font.setFamily("Source Serif Pro Light")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.home_date.setFont(font)
        self.home_date.setStyleSheet("color: rgb(255, 255, 255);")
        self.home_date.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.home_date.setObjectName("home_date")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Stamp61.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.home_tab, icon, "")
        self.status_tab = QtWidgets.QWidget()
        self.status_tab.setObjectName("status_tab")
        self.current_image = QtWidgets.QLabel(self.status_tab)
        self.current_image.setGeometry(QtCore.QRect(-30, -40, 991, 601))
        self.current_image.setStyleSheet("image: url(:/newPrefix/959820.jpg);")
        self.current_image.setText("")
        self.current_image.setObjectName("current_image")
        self.frame_2 = QtWidgets.QFrame(self.status_tab)
        self.frame_2.setGeometry(QtCore.QRect(10, 20, 311, 361))
        self.frame_2.setStyleSheet("background-color: rgb(89, 89, 89);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.title = QtWidgets.QLabel(self.frame_2)
        self.title.setGeometry(QtCore.QRect(10, 10, 291, 41))
        self.title.setStyleSheet("font: 75 20pt \"Noto Serif\";\n"
"color: rgb(255, 255, 255);")
        self.title.setObjectName("title")
        self.status = QtWidgets.QLabel(self.frame_2)
        self.status.setGeometry(QtCore.QRect(10, 60, 291, 21))
        self.status.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Sitka Display\";")
        self.status.setObjectName("status")
        self.min_temp = QtWidgets.QLabel(self.frame_2)
        self.min_temp.setGeometry(QtCore.QRect(10, 110, 291, 21))
        self.min_temp.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Sitka Display\";")
        self.min_temp.setObjectName("min_temp")
        self.max_temp = QtWidgets.QLabel(self.frame_2)
        self.max_temp.setGeometry(QtCore.QRect(10, 160, 291, 21))
        self.max_temp.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Sitka Display\";")
        self.max_temp.setObjectName("max_temp")
        self.wind = QtWidgets.QLabel(self.frame_2)
        self.wind.setGeometry(QtCore.QRect(10, 210, 291, 21))
        self.wind.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Sitka Display\";")
        self.wind.setObjectName("wind")
        self.sunrise = QtWidgets.QLabel(self.frame_2)
        self.sunrise.setGeometry(QtCore.QRect(10, 260, 291, 21))
        self.sunrise.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Sitka Display\";")
        self.sunrise.setObjectName("sunrise")
        self.sunset = QtWidgets.QLabel(self.frame_2)
        self.sunset.setGeometry(QtCore.QRect(10, 310, 291, 21))
        self.sunset.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Sitka Display\";")
        self.sunset.setObjectName("sunset")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Stamp260.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.status_tab, icon1, "")
        self.weather_tab = QtWidgets.QWidget()
        self.weather_tab.setObjectName("weather_tab")
        self.listWidget = QtWidgets.QListWidget(self.weather_tab)
        self.listWidget.setGeometry(QtCore.QRect(0, 40, 256, 192))
        #List 1
        self.listWidget.setObjectName("listWidget")
        for _ in range(8):
                item = QtWidgets.QListWidgetItem()
                self.listWidget.addItem(item)

        #list 2
        self.listWidget_2 = QtWidgets.QListWidget(self.weather_tab)
        self.listWidget_2.setGeometry(QtCore.QRect(270, 40, 256, 192))
        self.listWidget_2.setObjectName("listWidget_2")
        for _ in range(8):
                item = QtWidgets.QListWidgetItem()
                self.listWidget_2.addItem(item)

        #list 3
        self.listWidget_3 = QtWidgets.QListWidget(self.weather_tab)
        self.listWidget_3.setGeometry(QtCore.QRect(540, 40, 256, 192))
        self.listWidget_3.setObjectName("listWidget_3")
        for _ in range(8):
                item = QtWidgets.QListWidgetItem()
                self.listWidget_3.addItem(item)

        #dates
        self.date_1 = QtWidgets.QLabel(self.weather_tab)
        self.date_1.setGeometry(QtCore.QRect(6, 9, 241, 31))
        self.date_1.setStyleSheet("font: 75 20pt \"Linux Libertine G\";\n"
"color: rgb(255, 255, 255);")
        self.date_1.setAlignment(QtCore.Qt.AlignCenter)
        self.date_1.setObjectName("date_1")
        self.date_2 = QtWidgets.QLabel(self.weather_tab)
        self.date_2.setGeometry(QtCore.QRect(270, 10, 251, 31))
        self.date_2.setStyleSheet("font: 75 20pt \"Linux Libertine G\";\n"
"color: rgb(255, 255, 255);")
        self.date_2.setAlignment(QtCore.Qt.AlignCenter)
        self.date_2.setObjectName("date_2")
        self.date_3 = QtWidgets.QLabel(self.weather_tab)
        self.date_3.setGeometry(QtCore.QRect(540, 10, 261, 31))
        self.date_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Linux Libertine G\";")
        self.date_3.setAlignment(QtCore.Qt.AlignCenter)
        self.date_3.setObjectName("date_3")
        self.date_4 = QtWidgets.QLabel(self.weather_tab)
        self.date_4.setGeometry(QtCore.QRect(420, 260, 251, 31))
        self.date_4.setStyleSheet("font: 75 20pt \"Linux Libertine G\";\n"
"color: rgb(255, 255, 255);")
        self.date_4.setAlignment(QtCore.Qt.AlignCenter)
        self.date_4.setObjectName("date_4")
        self.date_5 = QtWidgets.QLabel(self.weather_tab)
        self.date_5.setGeometry(QtCore.QRect(130, 260, 251, 31))
        self.date_5.setStyleSheet("font: 75 20pt \"Linux Libertine G\";\n"
"color: rgb(255, 255, 255);")
        self.date_5.setAlignment(QtCore.Qt.AlignCenter)
        self.date_5.setObjectName("date_5")
        self.weather_image = QtWidgets.QLabel(self.weather_tab)
        self.weather_image.setGeometry(QtCore.QRect(-10, -20, 841, 601))
        self.weather_image.setStyleSheet("image: url(:/newPrefix/IA.full.1934053.jpg);")
        self.weather_image.setText("")
        self.weather_image.setObjectName("weather_image")

        #list 4
        self.listWidget_4 = QtWidgets.QListWidget(self.weather_tab)
        self.listWidget_4.setGeometry(QtCore.QRect(420, 290, 256, 192))
        self.listWidget_4.setObjectName("listWidget_4")
        for _ in range(8):
                item = QtWidgets.QListWidgetItem()
                self.listWidget_4.addItem(item)

        #list 5
        self.listWidget_5 = QtWidgets.QListWidget(self.weather_tab)
        self.listWidget_5.setGeometry(QtCore.QRect(130, 290, 256, 192))
        self.listWidget_5.setObjectName("listWidget_5")
        for _ in range(8):
                item = QtWidgets.QListWidgetItem()
                self.listWidget_5.addItem(item)
                
        self.weather_image.raise_()
        self.listWidget.raise_()
        self.listWidget_2.raise_()
        self.listWidget_3.raise_()
        self.date_1.raise_()
        self.date_2.raise_()
        self.date_3.raise_()
        self.date_4.raise_()
        self.date_5.raise_()
        self.listWidget_4.raise_()
        self.listWidget_5.raise_()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/Stamp110.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.weather_tab, icon2, "")
        self.note_tab = QtWidgets.QWidget()
        self.note_tab.setObjectName("note_tab")
        self.frame = QtWidgets.QFrame(self.note_tab)
        self.frame.setGeometry(QtCore.QRect(480, 20, 311, 491))
        self.frame.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        #Note buttons
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 311, 31))
        self.pushButton.setObjectName(f"pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 30, 311, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 60, 311, 31))
        self.pushButton_3.setObjectName("pushButton_3")

        self.notes_image = QtWidgets.QLabel(self.note_tab)
        self.notes_image.setGeometry(QtCore.QRect(-110, -40, 1011, 631))
        self.notes_image.setStyleSheet("image: url(:/newPrefix/750496.jpg);\n"
"position: center;")
        self.notes_image.setText("")
        self.notes_image.setObjectName("notes_image")
        self.notes_image.raise_()
        self.frame.raise_()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/Stamp114.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.note_tab, icon3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 795, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #button press action
    def openFile(self):
        webbrowser.open(join(path, files[0]))
    def openFile_1(self):
        webbrowser.open(join(path, files[1]))
    def openFile_2(self):
        webbrowser.open(join(path, files[2]))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        #Home page
        today = date.today().strftime("%b-%d-%Y")
        self.home_date.setText(_translate("MainWindow", today))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home_tab), _translate("MainWindow", "Home"))

        #Current Status page
        #Add API key
        owm = pyowm.OWM('xxxxx')

        #obtain weather manager
        weather_mgr = owm.weather_manager()

        #declare location
        loc = weather_mgr.weather_at_place('Ottawa,CA')

        #obtain data
        weather = loc.weather #weather object

        temp = weather.temperature(unit='celsius') #temperature
        temp_min = temp['temp_min']
        temp_max = temp['temp_max']
        wind_speed = weather.wind()['speed'] #wind speed
        sunrise = weather.sunrise_time(timeformat='date') - timedelta(hours=4) #sunrise time
        sunset = weather.sunset_time(timeformat='date')  - timedelta(hours=4) #sunset time
        self.title.setText(_translate("MainWindow", "Current Forcast"))
        self.status.setText(_translate("MainWindow", f"Status: {weather.detailed_status}"))
        self.min_temp.setText(_translate("MainWindow", f"Min Temp: {temp_min}"))
        self.max_temp.setText(_translate("MainWindow", f"Max Temp: {temp_max}"))
        self.wind.setText(_translate("MainWindow", f"Wind: {wind_speed}m/s"))
        self.sunrise.setText(_translate("MainWindow", f"Sunrise: {sunrise}"))
        self.sunset.setText(_translate("MainWindow", f"Sunset: {sunset}"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.status_tab), _translate("MainWindow", "Current Status"))

        #Weather page
        #obtain data
        forecast_3h = weather_mgr.forecast_at_place('Ottawa,CA', '3h').forecast #forcast in 3h intervals (5 days)
        day_0 = datetime.today().date() - timedelta(hours=4)
        day_1 = day_0 + timedelta(days=1) - timedelta(hours=4)
        day_2 = day_0 + timedelta(days=2) - timedelta(hours=4)
        day_3 = day_0 + timedelta(days=3) - timedelta(hours=4)
        day_4 = day_0 + timedelta(days=4) - timedelta(hours=4)

        #sorting items
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        self.listWidget_3.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_4.isSortingEnabled()
        self.listWidget_4.setSortingEnabled(False)
        self.listWidget_4.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_5.isSortingEnabled()
        self.listWidget_5.setSortingEnabled(False)
        self.listWidget_5.setSortingEnabled(__sortingEnabled)

        index = 0
        day = 0
        last_day = day_0
        for forcast in forecast_3h:
                currentday = forcast.reference_time('date') - timedelta(hours=4)
                if last_day != currentday.date():
                        last_day = currentday.date()
                        index = 0
                        day += 1
                
                if day == 0:
                        item = self.listWidget.item(index)
                        item.setText(_translate("MainWindow", f"{currentday.time()} - {forcast.detailed_status}"))
                elif day == 1:
                        item = self.listWidget_2.item(index)
                        item.setText(_translate("MainWindow", f"{currentday.time()} - {forcast.detailed_status}"))
                elif day == 2:
                        item = self.listWidget_3.item(index)
                        item.setText(_translate("MainWindow", f"{currentday.time()} - {forcast.detailed_status}"))
                elif day == 3:
                        item = self.listWidget_4.item(index)
                        item.setText(_translate("MainWindow", f"{currentday.time()} - {forcast.detailed_status}"))
                elif day == 4:
                        item = self.listWidget_5.item(index)
                        item.setText(_translate("MainWindow", f"{currentday.time()} - {forcast.detailed_status}"))   
                index += 1
       
        self.date_1.setText(_translate("MainWindow", f"{day_0}"))
        self.date_2.setText(_translate("MainWindow", f"{day_1}"))
        self.date_3.setText(_translate("MainWindow", f"{day_2}"))
        self.date_4.setText(_translate("MainWindow", f"{day_4}"))
        self.date_5.setText(_translate("MainWindow", f"{day_3}"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.weather_tab), _translate("MainWindow", "Weather"))

        #Notes page
        self.pushButton.setText(_translate("MainWindow", files[0]))
        self.pushButton_2.setText(_translate("MainWindow", files[1]))
        self.pushButton_3.setText(_translate("MainWindow", files[2]))

        self.pushButton.clicked.connect(self.openFile)
        self.pushButton_2.clicked.connect(self.openFile_1)
        self.pushButton_3.clicked.connect(self.openFile_2)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.note_tab), _translate("MainWindow", "Notes"))

import source


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
