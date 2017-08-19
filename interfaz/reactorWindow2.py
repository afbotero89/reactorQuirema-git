# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Home
import calculadora2
import setUpBombaMainWindow
import sys
sys.path.append('../modbusComunication')
import serialClass
import threading
import serialClass
import time
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, sectionVector, socket, socketBomba):
        global valorVariableAModificar, setValueFromCalculadora
        self.contadorAlmacenaDatos = 0
        self.s = socket
        self.sBomba = socketBomba

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.MainWindow = MainWindow
        self.sectionVector = sectionVector
        self.instanciaModbus = serialClass.modbus(self.s)
        self.flag_DesactivaVista = False
        self.playHornos_flag = False
        self.playValve_flag = False

        valorVariableAModificar = "0"
        setValueFromCalculadora = False

        # Evalua estatus de de los botones para almacenamiento
        self.statusHorno1Reactor = 'False'
        self.statusHorno2Reactor = 'False'
        self.statusHorno3Reactor = 'False'
        self.statusHorno4Reactor = 'False'

        self.conn = sqlite3.connect('statusButtonsStart.db')
        self.c = self.conn.cursor()

        for row in self.c.execute("SELECT * FROM dispositivos WHERE 1"):
            if row[0] == "1":
                self.statusSolenoide = row[5]
                self.statusMantas = row[6]
                self.statusHorno1Reactor = row[7]
                self.statusHorno2Reactor = row[8]
                self.statusHorno3Reactor = row[9]
                self.statusHorno4Reactor = row[10]

        self.allVisibleMantas = False

        #MainWindow.setPalette(palette)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(750, 0, 51, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../images/quirema.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(630, 70, 41, 91))
        self.label_3.setStyleSheet("background-color : qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 51, 51, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(630, 160, 41, 31))
        self.label_4.setStyleSheet("")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../images/trapezoide1.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(640, 190, 21, 101))
        self.label_5.setStyleSheet("background-color : qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0 rgba(0, 51, 51, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(640, 310, 21, 31))
        self.label_6.setStyleSheet("background-color : qlineargradient(spread:pad, x1:1, y1:0.119318, x2:1, y2:1, stop:0 rgba(0, 51, 51, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")

        self.line_5 = QtWidgets.QFrame(self.centralWidget)
        self.line_5.setGeometry(QtCore.QRect(640, 340, 20, 81))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.line_5.setPalette(palette)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralWidget)
        self.line_6.setGeometry(QtCore.QRect(640, 50, 20, 21))

        self.line_6.setPalette(palette)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")

        self.buttonTime= QtWidgets.QPushButton(self.centralWidget)
        self.buttonTime.setGeometry(QtCore.QRect(600, 0, 90, 30))
        self.buttonTime.setObjectName("pushButtonTime")
        self.buttonTime.setStyleSheet("background-color:#2F4F4F; color: white")

        self.pushButton_SV1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_SV1.setEnabled(True)
        self.pushButton_SV1.setGeometry(QtCore.QRect(740, 35, 51, 20))
        self.pushButton_SV1.setStyleSheet("color:black;")
        self.pushButton_SV1.setObjectName("pushButton_SV1")
        self.pushButton_PV1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_PV1.setGeometry(QtCore.QRect(740, 56, 51, 20))
        self.pushButton_PV1.setStyleSheet("color:black;")
        self.pushButton_PV1.setObjectName("pushButton_PV1")
        self.pushButton_R1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_R1.setGeometry(QtCore.QRect(740, 77, 51, 20))
        self.pushButton_R1.setStyleSheet("color:black;")
        self.pushButton_R1.setObjectName("pushButton_R1")

        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(720, 40, 21, 16))
        self.label_8.setStyleSheet("color:white;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setGeometry(QtCore.QRect(720, 60, 21, 16))
        self.label_9.setStyleSheet("color:white;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralWidget)
        self.label_10.setGeometry(QtCore.QRect(720, 80, 21, 16))
        self.label_10.setStyleSheet("color:white;")
        self.label_10.setObjectName("label_10")

        self.label_12 = QtWidgets.QLabel(self.centralWidget)
        self.label_12.setGeometry(QtCore.QRect(720, 160, 21, 16))
        self.label_12.setStyleSheet("color:white;")
        self.label_12.setObjectName("label_12")

        self.pushButton_PV2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_PV2.setGeometry(QtCore.QRect(740, 156, 51, 20))
        self.pushButton_PV2.setStyleSheet("color:black;")
        self.pushButton_PV2.setObjectName("pushButton_PV2")
        self.pushButton_SV2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_SV2.setGeometry(QtCore.QRect(740, 135, 51, 20))
        self.pushButton_SV2.setStyleSheet("color:black;")
        self.pushButton_SV2.setObjectName("pushButton_SV2")
        self.pushButton_R2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_R2.setGeometry(QtCore.QRect(740, 177, 51, 20))
        self.pushButton_R2.setStyleSheet("color:black;")
        self.pushButton_R2.setObjectName("pushButton_R2")
        self.label_14 = QtWidgets.QLabel(self.centralWidget)
        self.label_14.setGeometry(QtCore.QRect(720, 140, 21, 16))
        self.label_14.setStyleSheet("color:white;")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralWidget)
        self.label_15.setGeometry(QtCore.QRect(720, 180, 21, 16))
        self.label_15.setStyleSheet("color:white;")
        self.label_15.setObjectName("label_15")

        self.label_17 = QtWidgets.QLabel(self.centralWidget)
        self.label_17.setGeometry(QtCore.QRect(720, 260, 21, 16))
        self.label_17.setStyleSheet("color:white;")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralWidget)
        self.label_18.setGeometry(QtCore.QRect(720, 280, 21, 16))
        self.label_18.setStyleSheet("color:white;")
        self.label_18.setObjectName("label_18")
        self.pushButton_PV3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_PV3.setGeometry(QtCore.QRect(740, 256, 51, 20))
        self.pushButton_PV3.setStyleSheet("color:black;")
        self.pushButton_PV3.setObjectName("pushButton_PV3")
        self.label_19 = QtWidgets.QLabel(self.centralWidget)
        self.label_19.setGeometry(QtCore.QRect(720, 240, 21, 16))
        self.label_19.setStyleSheet("color:white;")
        self.label_19.setObjectName("label_19")
        self.pushButton_SV3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_SV3.setGeometry(QtCore.QRect(740, 235, 51, 20))
        self.pushButton_SV3.setStyleSheet("color:black;")
        self.pushButton_SV3.setObjectName("pushButton_SV3")

        self.pushButton_R3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_R3.setGeometry(QtCore.QRect(740, 277, 51, 20))
        self.pushButton_R3.setStyleSheet("color:black;")
        self.pushButton_R3.setObjectName("pushButton_R3")
        self.label_20 = QtWidgets.QLabel(self.centralWidget)
        self.label_20.setGeometry(QtCore.QRect(720, 360, 21, 16))
        self.label_20.setStyleSheet("color:white")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralWidget)
        self.label_21.setGeometry(QtCore.QRect(720, 380, 21, 16))
        self.label_21.setStyleSheet("color:white")
        self.label_21.setObjectName("label_21")
        self.pushButton_PV4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_PV4.setGeometry(QtCore.QRect(740, 356, 51, 20))
        self.pushButton_PV4.setStyleSheet("color:black;")
        self.pushButton_PV4.setObjectName("pushButton_PV4")
        self.pushButton_R4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_R4.setGeometry(QtCore.QRect(740, 377, 51, 20))
        self.pushButton_R4.setStyleSheet("color:black;")
        self.pushButton_R4.setObjectName("pushButton_R4")
        self.pushButton_SV4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_SV4.setGeometry(QtCore.QRect(740, 335, 51, 20))
        self.pushButton_SV4.setStyleSheet("color:black;")
        self.pushButton_SV4.setObjectName("pushButton_SV4")

        self.label_23 = QtWidgets.QLabel(self.centralWidget)
        self.label_23.setGeometry(QtCore.QRect(720, 340, 21, 16))
        self.label_23.setStyleSheet("color:white")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralWidget)
        self.label_24.setGeometry(QtCore.QRect(580, 110, 21, 91))
        self.label_24.setStyleSheet("background-color : qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 51, 51, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralWidget)
        self.label_25.setGeometry(QtCore.QRect(380, 190, 211, 161))
        self.label_25.setStyleSheet("")
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("../images/valve.png"))
        self.label_25.setScaledContents(True)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralWidget)
        self.label_26.setGeometry(QtCore.QRect(640, 290, 21, 20))
        self.label_26.setStyleSheet("background-color : black")
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralWidget)
        self.label_27.setGeometry(QtCore.QRect(500, 370, 101, 31))
        self.label_27.setStyleSheet("color:black;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 51, 51, 255), stop:1 rgba(255, 255, 255, 255));\n"
"qproperty-alignment: AlignCenter;")
        self.label_27.setObjectName("label_27")
        self.line_7 = QtWidgets.QFrame(self.centralWidget)
        self.line_7.setGeometry(QtCore.QRect(530, 340, 20, 31))

        self.line_7.setPalette(palette)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralWidget)
        self.line_8.setGeometry(QtCore.QRect(570, 230, 21, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralWidget)
        self.line_9.setGeometry(QtCore.QRect(580, 200, 20, 41))

        self.line_9.setPalette(palette)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.label_28 = QtWidgets.QLabel(self.centralWidget)
        self.label_28.setGeometry(QtCore.QRect(120, 330, 81, 71))
        self.label_28.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 51, 51, 255), stop:1 rgba(255, 255, 255, 255)); \n"
"border-radius: 20px;\n"
"qproperty-alignment: AlignCenter;")
        self.label_28.setObjectName("label_28")
        self.label_30 = QtWidgets.QLabel(self.centralWidget)
        self.label_30.setGeometry(QtCore.QRect(20, 320, 61, 21))
        self.label_30.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 51, 51, 255), stop:1 rgba(255, 255, 255, 255));\n"
"qproperty-alignment: AlignCenter;")
        self.label_30.setObjectName("label_Mantas")

        self.pushButtonAllMantas = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonAllMantas.setGeometry(QtCore.QRect(450, 60, 61, 21))
        self.pushButtonAllMantas.setStyleSheet("color:black;")
        self.pushButtonAllMantas.setObjectName("pushButtonPresentValueMantas")

        self.pushButtonManta1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonManta1.setGeometry(QtCore.QRect(210, 30, 71, 32))
        self.pushButtonManta1.setStyleSheet("color:black;")
        self.pushButtonManta1.setObjectName("pushButtonManta1")

        self.pushButtonManta2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonManta2.setGeometry(QtCore.QRect(270, 30, 71, 32))
        self.pushButtonManta2.setStyleSheet("color:black;")
        self.pushButtonManta2.setObjectName("pushButtonManta2")

        self.pushButtonManta3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonManta3.setGeometry(QtCore.QRect(330, 30, 71, 32))
        self.pushButtonManta3.setStyleSheet("color:black;")
        self.pushButtonManta3.setObjectName("pushButtonManta3")

        self.pushButtonManta4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonManta4.setGeometry(QtCore.QRect(390, 30, 71, 32))
        self.pushButtonManta4.setStyleSheet("color:black;")
        self.pushButtonManta4.setObjectName("pushButtonManta4")

        self.pushButtonManta5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonManta5.setGeometry(QtCore.QRect(450, 30, 71, 32))
        self.pushButtonManta5.setStyleSheet("color:black;")
        self.pushButtonManta5.setObjectName("pushButtonManta5")

        self.pushButtonManta6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonManta6.setGeometry(QtCore.QRect(510, 30, 71, 32))
        self.pushButtonManta6.setStyleSheet("color:black;")
        self.pushButtonManta6.setObjectName("pushButtonManta6")

        self.pushButtonManta7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonManta7.setGeometry(QtCore.QRect(580, 30, 71, 32))
        self.pushButtonManta7.setStyleSheet("color:black;")
        self.pushButtonManta7.setObjectName("pushButtonManta7")

        self.pushButtonManta8 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonManta8.setGeometry(QtCore.QRect(650, 30, 71, 32))
        self.pushButtonManta8.setStyleSheet("color:black;")
        self.pushButtonManta8.setObjectName("pushButtonManta8")

        self.label_SV_mantas = QtWidgets.QLabel(self.centralWidget)
        self.label_SV_mantas.setGeometry(QtCore.QRect(450, 90, 41, 26))
        self.label_SV_mantas.setStyleSheet("color:white;")
        self.label_SV_mantas.setObjectName("label_SV_mantas")

        self.pushButtonSetValueMantas = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonSetValueMantas.setGeometry(QtCore.QRect(480, 90, 51, 20))
        self.pushButtonSetValueMantas.setStyleSheet("color:black;")
        self.pushButtonSetValueMantas.setObjectName("setValueMantas")

        self.label_PV_mantas = QtWidgets.QLabel(self.centralWidget)
        self.label_PV_mantas.setGeometry(QtCore.QRect(450, 120, 41, 26))
        self.label_PV_mantas.setStyleSheet("color:white;")
        self.label_PV_mantas.setObjectName("label_PV_mantas")

        self.pushButtonPresentValueMantas = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonPresentValueMantas.setGeometry(QtCore.QRect(480, 120, 51, 20))
        self.pushButtonPresentValueMantas.setStyleSheet("color:black;")
        self.pushButtonPresentValueMantas.setObjectName("pushButtonPresentValueMantas")

        self.pushButtonStart_StopMantas = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonStart_StopMantas.setGeometry(QtCore.QRect(480, 150, 51, 20))

        if(self.statusMantas == "True"):
            self.pushButtonStart_StopMantas.setStyleSheet("color:white;background-color:red")
            self.pushButtonStart_StopMantas.setText("OFF")
        else:
            self.pushButtonStart_StopMantas.setStyleSheet("color:white;background-color:green")
            self.pushButtonStart_StopMantas.setText("ON")
            
        self.pushButtonStart_StopMantas.setObjectName("pushButtonStart_StopMantas")

        self.pushButton_start_bomba = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_start_bomba.setGeometry(QtCore.QRect(20, 374, 51, 20))
        self.pushButton_start_bomba.setStyleSheet("color:white;background-color:green")
        self.pushButton_start_bomba.setObjectName("pushButton_start_bomba")

        self.pushButton_stop_bomba = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_stop_bomba.setGeometry(QtCore.QRect(20, 396, 51, 20))
        self.pushButton_stop_bomba.setStyleSheet("color:white;background-color:green")
        self.pushButton_stop_bomba.setObjectName("pushButton_stop_bomba")

        self.pushButton_pause_bomba = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_pause_bomba.setGeometry(QtCore.QRect(20, 418, 51, 20))
        self.pushButton_pause_bomba.setStyleSheet("color:white;background-color:green")
        self.pushButton_pause_bomba.setObjectName("pushButton_pause_bomba")

        self.pushButton_setUp_bomba = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_setUp_bomba.setGeometry(QtCore.QRect(20, 350, 51, 20))
        self.pushButton_setUp_bomba.setStyleSheet("color:black;")
        self.pushButton_setUp_bomba.setObjectName("pushButton_PV_bomba")

        self.label_31 = QtWidgets.QLabel(self.centralWidget)
        self.label_31.setGeometry(QtCore.QRect(250, 260, 81, 41))
        self.label_31.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 51, 51, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 20px;\n"
"qproperty-alignment: AlignCenter;")
        self.label_31.setObjectName("label_31")

        self.pushButtonSolenoide = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonSolenoide.setGeometry(QtCore.QRect(210, 295, 50, 20))
        if(self.statusSolenoide == 'True'):
            self.pushButtonSolenoide.setStyleSheet("color:white;background-color:red")
            self.pushButtonSolenoide.setText("OFF")
        else:
            self.pushButtonSolenoide.setStyleSheet("color:white;background-color:green")
            self.pushButtonSolenoide.setText("ON")

        self.pushButtonSolenoide.setObjectName("pushButton_PV_flujo2")

        self.label_LoadSolenoide = QtWidgets.QLabel(self.centralWidget)
        self.label_LoadSolenoide.setGeometry(QtCore.QRect(265, 293, 41, 26))
        self.label_LoadSolenoide.setStyleSheet("color:white;")
        self.label_LoadSolenoide.setObjectName("label_LoadSolenoide")

        self.pushButtonLoadSolenoide = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonLoadSolenoide.setGeometry(QtCore.QRect(265, 315, 51, 20))
        self.pushButtonLoadSolenoide.setStyleSheet("color:black;background-color:white")
        self.pushButtonLoadSolenoide.setObjectName("pushButton_LoadSolenoide")

        self.label_InjectionSolenoide = QtWidgets.QLabel(self.centralWidget)
        self.label_InjectionSolenoide.setGeometry(QtCore.QRect(320, 293, 61, 26))
        self.label_InjectionSolenoide.setStyleSheet("color:white;")
        self.label_InjectionSolenoide.setObjectName("label_InjectionSolenoide")

        self.pushButtonInjectionSolenoide = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonInjectionSolenoide.setGeometry(QtCore.QRect(320, 315, 51, 20))
        self.pushButtonInjectionSolenoide.setStyleSheet("color:black;background-color:white")
        self.pushButtonInjectionSolenoide.setObjectName("pushButton_InjectionSolenoide")

        self.label_32 = QtWidgets.QLabel(self.centralWidget)
        self.label_32.setGeometry(QtCore.QRect(90, 250, 41, 31))
        self.label_32.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 51, 51, 255), stop:1 rgba(255, 255, 255, 255));\n"
"qproperty-alignment: AlignCenter;")
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.centralWidget)
        self.label_33.setGeometry(QtCore.QRect(165, 60, 46, 21))
        self.label_33.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(76, 76, 76, 255), stop:1 rgba(0, 128, 128, 255));color:white;\n"
"qproperty-alignment: AlignCenter;")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.centralWidget)
        self.label_34.setGeometry(QtCore.QRect(195, 90, 46, 21))
        self.label_34.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(76, 76, 76, 255), stop:1 rgba(0, 128, 128, 255));color:white;\n"
"qproperty-alignment: AlignCenter;")
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.centralWidget)
        self.label_35.setGeometry(QtCore.QRect(195, 130, 46, 21))
        self.label_35.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(76, 76, 76, 255), stop:1 rgba(0, 128, 128, 255));color:white;\n"
"qproperty-alignment: AlignCenter;")
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.centralWidget)
        self.label_36.setGeometry(QtCore.QRect(165, 160, 46, 21))
        self.label_36.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(76, 76, 76, 255), stop:1 rgba(0, 128, 128, 255));color:white;\n"
"qproperty-alignment: AlignCenter;")
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.centralWidget)
        self.label_37.setGeometry(QtCore.QRect(185, 190, 46, 21))
        self.label_37.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(76, 76, 76, 255), stop:1 rgba(0, 128, 128, 255));color:white;\n"
"qproperty-alignment: AlignCenter;")
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.centralWidget)
        self.label_38.setGeometry(QtCore.QRect(160, 220, 46, 21))
        self.label_38.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(76, 76, 76, 255), stop:1 rgba(0, 128, 128, 255));color:white;\n"
"qproperty-alignment: AlignCenter;")
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.centralWidget)
        self.label_39.setGeometry(QtCore.QRect(140, 60, 21, 20))
        self.label_39.setStyleSheet("color:white;")
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.centralWidget)
        self.label_40.setGeometry(QtCore.QRect(140, 90, 51, 20))
        self.label_40.setStyleSheet("color:white;")
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.centralWidget)
        self.label_41.setGeometry(QtCore.QRect(140, 130, 51, 20))
        self.label_41.setStyleSheet("color:white;")
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.centralWidget)
        self.label_42.setGeometry(QtCore.QRect(140, 160, 21, 20))
        self.label_42.setStyleSheet("color:white;")
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.centralWidget)
        self.label_43.setGeometry(QtCore.QRect(140, 190, 41, 20))
        self.label_43.setStyleSheet("color:white;")
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.centralWidget)
        self.label_44.setGeometry(QtCore.QRect(140, 220, 21, 20))
        self.label_44.setStyleSheet("color:white;")
        self.label_44.setObjectName("label_44")
        self.line_10 = QtWidgets.QFrame(self.centralWidget)
        self.line_10.setGeometry(QtCore.QRect(200, 50, 191, 20))

        self.line_10.setPalette(palette)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralWidget)
        self.line_11.setGeometry(QtCore.QRect(230, 80, 141, 20))

        self.line_11.setPalette(palette)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.centralWidget)
        self.line_12.setGeometry(QtCore.QRect(230, 120, 161, 20))

        self.line_12.setPalette(palette)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.centralWidget)
        self.line_13.setGeometry(QtCore.QRect(200, 150, 191, 20))

        self.line_13.setPalette(palette)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.centralWidget)
        self.line_14.setGeometry(QtCore.QRect(220, 180, 171, 20))

        self.line_14.setPalette(palette)
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(self.centralWidget)
        self.line_15.setGeometry(QtCore.QRect(200, 220, 71, 20))

        self.line_15.setPalette(palette)
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.pushButton_SV_flujo1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_SV_flujo1.setGeometry(QtCore.QRect(10, 60, 61, 16))
        self.pushButton_SV_flujo1.setStyleSheet("color:black;")
        self.pushButton_SV_flujo1.setObjectName("pushButton_SV_flujo1")
        self.pushButton_PV_flujo1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_PV_flujo1.setGeometry(QtCore.QRect(80, 60, 51, 16))
        self.pushButton_PV_flujo1.setStyleSheet("color:black;")
        self.pushButton_PV_flujo1.setObjectName("pushButton_PV_flujo1")
        self.label_45 = QtWidgets.QLabel(self.centralWidget)
        self.label_45.setGeometry(QtCore.QRect(370, 80, 41, 31))
        self.label_45.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 51, 51, 255), stop:1 rgba(255, 255, 255, 255))")
        self.label_45.setText("")
        self.label_45.setObjectName("label_45")
        self.line_16 = QtWidgets.QFrame(self.centralWidget)
        self.line_16.setGeometry(QtCore.QRect(380, 61, 20, 20))

        self.line_16.setPalette(palette)
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.line_17 = QtWidgets.QFrame(self.centralWidget)
        self.line_17.setGeometry(QtCore.QRect(380, 110, 20, 81))

        self.line_17.setPalette(palette)
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.line_18 = QtWidgets.QFrame(self.centralWidget)
        self.line_18.setGeometry(QtCore.QRect(410, 180, 3, 61))

        self.line_18.setPalette(palette)
        self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.line_19 = QtWidgets.QFrame(self.centralWidget)
        self.line_19.setGeometry(QtCore.QRect(410, 170, 31, 16))

        self.line_19.setPalette(palette)
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.line_20 = QtWidgets.QFrame(self.centralWidget)
        self.line_20.setGeometry(QtCore.QRect(430, 100, 20, 81))

        self.line_20.setPalette(palette)
        self.line_20.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.line_21 = QtWidgets.QFrame(self.centralWidget)
        self.line_21.setGeometry(QtCore.QRect(410, 90, 31, 16))

        self.line_21.setPalette(palette)
        self.line_21.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")

        self.line_22 = QtWidgets.QFrame(self.centralWidget)
        self.line_22.setGeometry(QtCore.QRect(160, 410, 491, 20))

        self.line_22.setPalette(palette)
        self.line_22.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.line_23 = QtWidgets.QFrame(self.centralWidget)
        self.line_23.setGeometry(QtCore.QRect(150, 400, 20, 20))

        self.line_23.setPalette(palette)
        self.line_23.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.line_24 = QtWidgets.QFrame(self.centralWidget)
        self.line_24.setGeometry(QtCore.QRect(620, 40, 31, 20))

        self.line_24.setPalette(palette)
        self.line_24.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.line_25 = QtWidgets.QFrame(self.centralWidget)
        self.line_25.setGeometry(QtCore.QRect(610, 50, 20, 251))

        self.line_25.setPalette(palette)
        self.line_25.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_25.setObjectName("line_25")
        self.line_26 = QtWidgets.QFrame(self.centralWidget)
        self.line_26.setGeometry(QtCore.QRect(570, 290, 51, 20))

        self.line_26.setPalette(palette)
        self.line_26.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_26.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_26.setObjectName("line_26")
        self.line_27 = QtWidgets.QFrame(self.centralWidget)
        self.line_27.setGeometry(QtCore.QRect(580, 70, 20, 41))

        self.line_27.setPalette(palette)
        self.line_27.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_27.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_27.setObjectName("line_27")
        self.line_28 = QtWidgets.QFrame(self.centralWidget)
        self.line_28.setGeometry(QtCore.QRect(540, 60, 51, 20))

        self.line_28.setPalette(palette)
        self.line_28.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_28.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_28.setObjectName("line_28")
        self.line_29 = QtWidgets.QFrame(self.centralWidget)
        self.line_29.setGeometry(QtCore.QRect(530, 70, 20, 131))

        self.line_29.setPalette(palette)
        self.line_29.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_29.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_29.setObjectName("line_29")
        self.line_30 = QtWidgets.QFrame(self.centralWidget)
        self.line_30.setGeometry(QtCore.QRect(290, 340, 20, 31))

        self.line_30.setPalette(palette)
        self.line_30.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_30.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_30.setObjectName("line_30")
        self.line_31 = QtWidgets.QFrame(self.centralWidget)
        self.line_31.setGeometry(QtCore.QRect(300, 360, 191, 20))

        self.line_31.setPalette(palette)
        self.line_31.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_31.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_31.setObjectName("line_31")
        self.line_32 = QtWidgets.QFrame(self.centralWidget)
        self.line_32.setGeometry(QtCore.QRect(480, 350, 20, 21))

        self.line_32.setPalette(palette)
        self.line_32.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_32.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_32.setObjectName("line_32")
        self.line_33 = QtWidgets.QFrame(self.centralWidget)
        self.line_33.setGeometry(QtCore.QRect(110, 290, 91, 20))

        self.line_33.setPalette(palette)
        self.line_33.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_33.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_33.setObjectName("line_33")
        self.line_34 = QtWidgets.QFrame(self.centralWidget)
        self.line_34.setGeometry(QtCore.QRect(100, 280, 20, 21))

        self.line_34.setPalette(palette)
        self.line_34.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_34.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_34.setObjectName("line_34")
        self.line_35 = QtWidgets.QFrame(self.centralWidget)
        self.line_35.setGeometry(QtCore.QRect(230, 240, 121, 20))

        self.line_35.setPalette(palette)
        self.line_35.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_35.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_35.setObjectName("line_35")
        self.line_36 = QtWidgets.QFrame(self.centralWidget)
        self.line_36.setGeometry(QtCore.QRect(340, 250, 20, 41))

        self.line_36.setPalette(palette)
        self.line_36.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_36.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_36.setObjectName("line_36")
        self.line_37 = QtWidgets.QFrame(self.centralWidget)
        self.line_37.setGeometry(QtCore.QRect(220, 250, 20, 41))

        self.line_37.setPalette(palette)
        self.line_37.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_37.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_37.setObjectName("line_37")
        self.line_38 = QtWidgets.QFrame(self.centralWidget)
        self.line_38.setGeometry(QtCore.QRect(230, 280, 21, 16))

        self.line_38.setPalette(palette)
        self.line_38.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_38.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_38.setObjectName("line_38")
        self.line_39 = QtWidgets.QFrame(self.centralWidget)
        self.line_39.setGeometry(QtCore.QRect(330, 280, 21, 16))

        self.line_39.setPalette(palette)
        self.line_39.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_39.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_39.setObjectName("line_39")
        self.line_40 = QtWidgets.QFrame(self.centralWidget)
        self.line_40.setGeometry(QtCore.QRect(260, 230, 20, 31))

        self.line_40.setPalette(palette)
        self.line_40.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_40.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_40.setObjectName("line_40")
        self.line_41 = QtWidgets.QFrame(self.centralWidget)
        self.line_41.setGeometry(QtCore.QRect(380, 290, 31, 20))

        self.line_41.setPalette(palette)
        self.line_41.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_41.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_41.setObjectName("line_41")
        self.line_42 = QtWidgets.QFrame(self.centralWidget)
        self.line_42.setGeometry(QtCore.QRect(370, 230, 20, 71))

        self.line_42.setPalette(palette)
        self.line_42.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_42.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_42.setObjectName("line_42")
        self.line_43 = QtWidgets.QFrame(self.centralWidget)
        self.line_43.setGeometry(QtCore.QRect(300, 220, 81, 20))

        self.line_43.setPalette(palette)
        self.line_43.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_43.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_43.setObjectName("line_43")
        self.line_44 = QtWidgets.QFrame(self.centralWidget)
        self.line_44.setGeometry(QtCore.QRect(290, 230, 20, 31))

        self.line_44.setPalette(palette)
        self.line_44.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_44.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_44.setObjectName("line_44")
        self.line_45 = QtWidgets.QFrame(self.centralWidget)
        self.line_45.setGeometry(QtCore.QRect(370, 200, 71, 20))

        self.line_45.setPalette(palette)
        self.line_45.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_45.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_45.setObjectName("line_45")
        self.line_46 = QtWidgets.QFrame(self.centralWidget)
        self.line_46.setGeometry(QtCore.QRect(360, 210, 20, 181))
        
        self.line_46.setPalette(palette)
        self.line_46.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_46.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_46.setObjectName("line_46")
        self.line_47 = QtWidgets.QFrame(self.centralWidget)
        self.line_47.setGeometry(QtCore.QRect(200, 380, 171, 20))

        self.line_47.setPalette(palette)
        self.line_47.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_47.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_47.setObjectName("line_47")
        self.label_46 = QtWidgets.QLabel(self.centralWidget)
        self.label_46.setGeometry(QtCore.QRect(360, 360, 21, 21))
        self.label_46.setText("")
        self.label_46.setPixmap(QtGui.QPixmap("../images/cruceLineaHorizontal.png"))
        self.label_46.setScaledContents(True)
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.centralWidget)
        self.label_47.setGeometry(QtCore.QRect(400, 200, 21, 21))
        self.label_47.setText("")
        self.label_47.setPixmap(QtGui.QPixmap("../images/cruceLineaVertical.png"))
        self.label_47.setScaledContents(True)
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.centralWidget)
        self.label_48.setGeometry(QtCore.QRect(360, 220, 21, 21))
        self.label_48.setText("")
        self.label_48.setPixmap(QtGui.QPixmap("../images/cruceLineaVertical.png"))
        self.label_48.setScaledContents(True)
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.centralWidget)
        self.label_49.setGeometry(QtCore.QRect(290, 240, 21, 21))
        self.label_49.setText("")
        self.label_49.setPixmap(QtGui.QPixmap("../images/cruceLineaVertical.png"))
        self.label_49.setScaledContents(True)
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.centralWidget)
        self.label_50.setGeometry(QtCore.QRect(260, 240, 21, 21))
        self.label_50.setText("")
        self.label_50.setPixmap(QtGui.QPixmap("../../images/cruceLineaVertical.png"))
        self.label_50.setScaledContents(True)
        self.label_50.setObjectName("label_50")
        
        self.playButton = QtWidgets.QPushButton(self.centralWidget)
        self.playButton.setGeometry(QtCore.QRect(670, 290, 41, 32))

        if(self.statusHorno1Reactor == 'True'):
            self.playButton.setStyleSheet("color:white;background-color:red")
            self.playButton.setText("Stop 1")
        else:
            self.playButton.setStyleSheet("color:white;background-color:green")
            self.playButton.setText("Play 1")

        self.playButton.setObjectName("playButton")

        self.playButton1 = QtWidgets.QPushButton(self.centralWidget)
        self.playButton1.setGeometry(QtCore.QRect(670, 324, 41, 32))

        if(self.statusHorno2Reactor == 'True'):
            self.playButton1.setStyleSheet("color:white;background-color:red")
            self.playButton1.setText("Stop 2")
        else:
            self.playButton1.setStyleSheet("color:white;background-color:green")
            self.playButton1.setText("Play 2")

        self.playButton1.setObjectName("playButton")


        self.playButton2 = QtWidgets.QPushButton(self.centralWidget)
        self.playButton2.setGeometry(QtCore.QRect(670, 358, 41, 32))

        if(self.statusHorno3Reactor == 'True'):
            self.playButton2.setStyleSheet("color:white;background-color:red")
            self.playButton2.setText("Stop 3")
        else:
            self.playButton2.setStyleSheet("color:white;background-color:green")
            self.playButton2.setText("Play 3")

        self.playButton2.setObjectName("playButton")


        self.playButton3 = QtWidgets.QPushButton(self.centralWidget)
        self.playButton3.setGeometry(QtCore.QRect(670, 392, 41, 32))

        if(self.statusHorno4Reactor == 'True'):
            self.playButton3.setStyleSheet("color:white;background-color:red")
            self.playButton3.setText("Stop 4")
        else:
            self.playButton3.setStyleSheet("color:white;background-color:green")
            self.playButton3.setText("Play 4")

        self.playButton3.setObjectName("playButton")        

        self.label_51 = QtWidgets.QLabel(self.centralWidget)
        self.label_51.setGeometry(QtCore.QRect(10, 40, 21, 16))
        self.label_51.setStyleSheet("color:white;")
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.centralWidget)
        self.label_52.setGeometry(QtCore.QRect(80, 40, 21, 16))
        self.label_52.setStyleSheet("color:white;")
        self.label_52.setObjectName("label_52")
        self.pushButton_PV_flujo2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_PV_flujo2.setGeometry(QtCore.QRect(80, 90, 51, 16))
        self.pushButton_PV_flujo2.setStyleSheet("color:black;")
        self.pushButton_PV_flujo2.setObjectName("pushButton_PV_flujo2")
        self.pushButton_SV_flujo2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_SV_flujo2.setGeometry(QtCore.QRect(10, 90, 61, 16))
        self.pushButton_SV_flujo2.setStyleSheet("color:black;")
        self.pushButton_SV_flujo2.setObjectName("pushButton_SV_flujo2")
        self.pushButton_PV_flujo3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_PV_flujo3.setGeometry(QtCore.QRect(80, 130, 51, 16))
        self.pushButton_PV_flujo3.setStyleSheet("color:black;")
        self.pushButton_PV_flujo3.setObjectName("pushButton_PV_flujo3")
        self.pushButton_SV_flujo3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_SV_flujo3.setGeometry(QtCore.QRect(10, 130, 61, 16))
        self.pushButton_SV_flujo3.setStyleSheet("color:black;")
        self.pushButton_SV_flujo3.setObjectName("pushButton_SV_flujo3")
        self.pushButton_PV_flujo4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_PV_flujo4.setGeometry(QtCore.QRect(80, 160, 51, 16))
        self.pushButton_PV_flujo4.setStyleSheet("color:black")
        self.pushButton_PV_flujo4.setObjectName("pushButton_PV_flujo4")
        self.pushButton_SV_flujo4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_SV_flujo4.setGeometry(QtCore.QRect(10, 160, 61, 16))
        self.pushButton_SV_flujo4.setStyleSheet("color:black;")
        self.pushButton_SV_flujo4.setObjectName("pushButton_SV_flujo4")
        self.pushButton_PV_flujo5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_PV_flujo5.setGeometry(QtCore.QRect(80, 190, 51, 16))
        self.pushButton_PV_flujo5.setStyleSheet("color:black;")
        self.pushButton_PV_flujo5.setObjectName("pushButton_PV_flujo5")
        self.pushButton_SV_flujo5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_SV_flujo5.setGeometry(QtCore.QRect(10, 190, 61, 16))
        self.pushButton_SV_flujo5.setStyleSheet("color:black;")
        self.pushButton_SV_flujo5.setObjectName("pushButton_SV_flujo5")
        self.pushButton_PV_flujo6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_PV_flujo6.setGeometry(QtCore.QRect(80, 220, 51, 16))
        self.pushButton_PV_flujo6.setStyleSheet("color:black;")
        self.pushButton_PV_flujo6.setObjectName("pushButton_PV_flujo6")
        self.pushButton_SV_flujo6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_SV_flujo6.setGeometry(QtCore.QRect(10, 220, 61, 16))
        self.pushButton_SV_flujo6.setStyleSheet("color:black;")
        self.pushButton_SV_flujo6.setObjectName("pushButton_SV_flujo6")

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.pushButtonHome = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonHome.setGeometry(QtCore.QRect(10, 0, 31, 31))
        self.pushButtonHome.setStyleSheet("background-color: #222222; color:white; font-size: 22pt;")
        self.pushButtonHome.setIcon(QtGui.QIcon('../images/home.png'))
        self.pushButtonHome.setIconSize(QtCore.QSize(21,21))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quirema"))
        self.label.setText(_translate("MainWindow", "                   Quirema                                     Reactor"))
        #self.label_7.setText(_translate("MainWindow", "P"))
        self.pushButtonAllMantas.setText(_translate("MainWindow", "Mantas"))
        self.pushButtonAllMantas.setStyleSheet("background-color:green; color:white")

        self.pushButton_SV1.setText(_translate("MainWindow", "000.0"))
        self.pushButton_PV1.setText(_translate("MainWindow", "000.0"))
        self.pushButton_R1.setText(_translate("MainWindow", "000.0"))

        self.label_SV_mantas.setText(_translate("MainWindow","SV:"))
        self.label_PV_mantas.setText(_translate("MainWindow","PV:"))

        self.label_LoadSolenoide.setText(_translate("MainWindow","Load:"))
        self.label_InjectionSolenoide.setText(_translate("MainWindow","Injection:"))

        self.label_8.setText(_translate("MainWindow", "SV:"))
        self.label_9.setText(_translate("MainWindow", "PV:"))
        self.label_10.setText(_translate("MainWindow", "R:"))

        self.label_12.setText(_translate("MainWindow", "PV:"))

        self.pushButton_PV2.setText(_translate("MainWindow", "000.0"))
        self.pushButton_SV2.setText(_translate("MainWindow", "000.0"))
        self.pushButton_R2.setText(_translate("MainWindow", "000.0"))
        self.label_14.setText(_translate("MainWindow", "SV:"))
        self.label_15.setText(_translate("MainWindow", "R:"))

        self.label_17.setText(_translate("MainWindow", "PV:"))
        self.label_18.setText(_translate("MainWindow", "R:"))
        self.pushButton_PV3.setText(_translate("MainWindow", "000.0"))
        self.label_19.setText(_translate("MainWindow", "SV:"))
        self.pushButton_SV3.setText(_translate("MainWindow", "000.0"))

        self.pushButton_R3.setText(_translate("MainWindow", "000.0"))
        self.label_20.setText(_translate("MainWindow", "PV:"))
        self.label_21.setText(_translate("MainWindow", "R:"))
        self.pushButton_PV4.setText(_translate("MainWindow", "000.0"))
        self.pushButton_R4.setText(_translate("MainWindow", "000.0"))
        self.pushButton_SV4.setText(_translate("MainWindow", "000.0"))

        self.label_23.setText(_translate("MainWindow", "SV:"))
        self.label_27.setText(_translate("MainWindow", " Analizador vent"))
        self.label_28.setText(_translate("MainWindow", "4-way valve"))
        self.label_30.setText(_translate("MainWindow", "Bomba"))

        self.pushButtonSetValueMantas.setText(_translate("MainWindow", "SV:"))
        self.pushButtonPresentValueMantas.setText(_translate("MainWindow", "PV:"))
        #self.pushButtonStart_StopMantas.setText(_translate("MainWindow","ON"))
        self.pushButton_start_bomba.setText(_translate("MainWindow", "Start"))
        self.pushButton_stop_bomba.setText(_translate("MainWindow", "Stop"))
        self.pushButton_pause_bomba.setText(_translate("MainWindow", "Pause"))
        self.pushButton_setUp_bomba.setText(_translate("MainWindow", "Set up"))

        self.label_31.setText(_translate("MainWindow", "6-way valve"))
        self.label_32.setText(_translate("MainWindow", "Vent"))
        self.label_33.setText(_translate("MainWindow", "MFC 1"))
        self.label_34.setText(_translate("MainWindow", "MFC 2"))
        self.label_35.setText(_translate("MainWindow", "MFC 3"))
        self.label_36.setText(_translate("MainWindow", "MFC 4"))
        self.label_37.setText(_translate("MainWindow", "MFC 5"))
        self.label_38.setText(_translate("MainWindow", "MFC 6"))
        self.label_39.setText(_translate("MainWindow", "Ar"))
        self.label_40.setText(_translate("MainWindow", "CO2/O2"))
        self.label_41.setText(_translate("MainWindow", "H2/CH4"))
        self.label_42.setText(_translate("MainWindow", "CO"))
        self.label_43.setText(_translate("MainWindow", "Etileno"))
        self.label_44.setText(_translate("MainWindow", "Ar"))
        self.pushButton_SV_flujo1.setText(_translate("MainWindow", "0000.0"))
        self.pushButton_PV_flujo1.setText(_translate("MainWindow", "0000.0"))
        #self.playButton.setText(_translate("MainWindow", "Play 1"))
        #self.playButton1.setText(_translate("MainWindow", "Play 2"))
        #self.playButton2.setText(_translate("MainWindow", "Play 3"))
        #self.playButton3.setText(_translate("MainWindow", "Play 4"))
        self.label_51.setText(_translate("MainWindow", "SV:"))
        self.label_52.setText(_translate("MainWindow", "PV:"))
        self.pushButton_PV_flujo2.setText(_translate("MainWindow", "0000.0"))
        self.pushButton_SV_flujo2.setText(_translate("MainWindow", "0000.0"))
        self.pushButton_PV_flujo3.setText(_translate("MainWindow", "0000.0"))
        self.pushButton_SV_flujo3.setText(_translate("MainWindow", "0000.0"))
        self.pushButton_PV_flujo4.setText(_translate("MainWindow", "0000.0"))
        self.pushButton_SV_flujo4.setText(_translate("MainWindow", "0000.0"))
        self.pushButton_PV_flujo5.setText(_translate("MainWindow", "0000.0"))
        self.pushButton_SV_flujo5.setText(_translate("MainWindow", "0000.0"))
        self.pushButton_PV_flujo6.setText(_translate("MainWindow", "0000.0"))
        self.pushButton_SV_flujo6.setText(_translate("MainWindow", "0000.0"))


        self.pushButtonManta1.setVisible(False)
        self.pushButtonManta2.setVisible(False)
        self.pushButtonManta3.setVisible(False)
        self.pushButtonManta4.setVisible(False)
        self.pushButtonManta5.setVisible(False)
        self.pushButtonManta6.setVisible(False)
        self.pushButtonManta7.setVisible(False)
        self.pushButtonManta8.setVisible(False)

        #self.pushButtonSolenoide.setText(_translate("MainWindow", "ON"))
        self.pushButtonLoadSolenoide.setText(_translate("MainWindow","0000.0"))
        self.pushButtonInjectionSolenoide.setText(_translate("MainWindow","0000.0"))

        self.actionButtons()
        #self.actualizaValoresPIDTimer()
        self.t = threading.Thread(target = self.actualizaValoresPIDTimer)
        self.t.IsBackground = True;
        self.t.start()

    def actionButtons(self):
        self.pushButtonHome.clicked.connect(self.home)
        self.pushButton_SV1.clicked.connect(lambda: self.setValuesHorno('setValue','horno1'))
        #self.pushButton_PV1.clicked.connect(lambda: self.setValuesHorno('presentValue','horno1'))
        self.pushButton_R1.clicked.connect(lambda: self.setValuesHorno('rampa','horno1'))

        #self.pushButton_PV2.clicked.connect(lambda: self.setValuesHorno('presentValue','horno2'))
        self.pushButton_SV2.clicked.connect(lambda: self.setValuesHorno('setValue','horno2'))
        self.pushButton_R2.clicked.connect(lambda: self.setValuesHorno('rampa','horno2'))

        #self.pushButton_PV3.clicked.connect(lambda: self.setValuesHorno('presentValue','horno3'))
        self.pushButton_SV3.clicked.connect(lambda: self.setValuesHorno('setValue','horno3'))

        self.pushButton_R3.clicked.connect(lambda: self.setValuesHorno('rampa','horno3'))

        #self.pushButton_PV4.clicked.connect(lambda: self.setValuesHorno('presentValue','horno4'))
        self.pushButton_R4.clicked.connect(lambda: self.setValuesHorno('rampa','horno4'))
        self.pushButton_SV4.clicked.connect(lambda: self.setValuesHorno('setValue','horno4'))

        # Controladores de flujo
        # MFC1
        self.pushButton_SV_flujo1.clicked.connect(lambda: self.setValuesHorno('setValue_MFC','MFC1'))
        #self.pushButton_PV_flujo1.clicked.connect(lambda: self.setValuesHorno('presentValue_MFC','MFC1'))

        # MFC2
        self.pushButton_SV_flujo2.clicked.connect(lambda: self.setValuesHorno('setValue_MFC','MFC2'))
        #self.pushButton_PV_flujo2.clicked.connect(lambda: self.setValuesHorno('presentValue_MFC','MFC2'))

        # MFC3
        self.pushButton_SV_flujo3.clicked.connect(lambda: self.setValuesHorno('setValue_MFC','MFC3'))
        #self.pushButton_PV_flujo3.clicked.connect(lambda: self.setValuesHorno('presentValue_MFC','MFC3'))

        # MFC4
        self.pushButton_SV_flujo4.clicked.connect(lambda: self.setValuesHorno('setValue_MFC','MFC4'))

        # MFC5
        self.pushButton_SV_flujo5.clicked.connect(lambda: self.setValuesHorno('setValue_MFC','MFC5'))

        # MFC6
        self.pushButton_SV_flujo6.clicked.connect(lambda: self.setValuesHorno('setValue_MFC','MFC6'))
        #self.pushButton_PV_flujo4.clicked.connect(lambda: self.setValuesHorno('presentValue_MFC','MFC4'))

        self.playButton.clicked.connect(lambda: self.playHornos('horno1', self.playButton))
        self.playButton1.clicked.connect(lambda: self.playHornos('horno2', self.playButton1))
        self.playButton2.clicked.connect(lambda: self.playHornos('horno3', self.playButton2))
        self.playButton3.clicked.connect(lambda: self.playHornos('horno4', self.playButton3))
        
        # Actions Buttons solenoide
        self.pushButtonSolenoide.clicked.connect(lambda: self.playSolenoide_Mantas('Solenoide', self.pushButtonSolenoide))
        self.pushButtonLoadSolenoide.clicked.connect(lambda: self.setLoadSolenoide('Load','Solenoide'))
        self.pushButtonInjectionSolenoide.clicked.connect(lambda: self.setInjectionSolenoide('Injection','Solenoide'))
 
        # Action Buttons mantas
        self.pushButtonSetValueMantas.clicked.connect(lambda: self.setValueMantas('setValue_mantas','Mantas'))
        self.pushButtonPresentValueMantas.clicked.connect(self.presentValueMantas)
        self.pushButtonStart_StopMantas.clicked.connect(lambda: self.playSolenoide_Mantas('Mantas', self.pushButtonStart_StopMantas))

        # Actions buttons Bomba
        self.pushButton_setUp_bomba.clicked.connect(self.setUpBomba)
        self.pushButton_start_bomba.clicked.connect(self.startBomba)
        self.pushButton_stop_bomba.clicked.connect(self.stopBomba)
        self.pushButton_pause_bomba.clicked.connect(self.pauseBomba)

        self.pushButtonAllMantas.clicked.connect(self.seeAllMantas)

    def home(self):
        self.flag_DesactivaVista = True
        self.home = Home.Ui_MainWindow()
        self.home.setupUi(self.MainWindow, self.s, self.sBomba)
        #self.t.cancel()

    def seeAllMantas(self):
        if(self.allVisibleMantas == False):
            self.allVisibleMantas = True
            self.pushButtonManta1.setVisible(True)
            self.pushButtonManta2.setVisible(True)
            self.pushButtonManta3.setVisible(True)
            self.pushButtonManta4.setVisible(True)
            self.pushButtonManta5.setVisible(True)
            self.pushButtonManta6.setVisible(True)
            self.pushButtonManta7.setVisible(True)
            self.pushButtonManta8.setVisible(True)
        else:
            self.allVisibleMantas = False
            self.pushButtonManta1.setVisible(False)
            self.pushButtonManta2.setVisible(False)
            self.pushButtonManta3.setVisible(False)
            self.pushButtonManta4.setVisible(False)
            self.pushButtonManta5.setVisible(False)
            self.pushButtonManta6.setVisible(False)
            self.pushButtonManta7.setVisible(False)
            self.pushButtonManta8.setVisible(False)

    #Variable del horno o controlador de flujo (MFC) (variable): SV: set value, PV: present Value, R: rampa, X: por definir     
    # Equipo seleccionado: Se refiere que selecciono el usuario para modificar (hornos o controladores de flujo(MFC))
    def setValuesHorno(self, variable, equipoSeleccionado):
        self.variableSeleccionada = variable
        self.equipoSeleccionado = equipoSeleccionado
        self.MainWindow.setEnabled(False)
        MainWindow = QtWidgets.QMainWindow()
        self.calculadora = calculadora2.Ui_MainWindow()
        self.calculadora.setupUi_PID_reactor(MainWindow, variable, equipoSeleccionado, self.sectionVector, self.MainWindow, self.s)
        MainWindow.show()

    def playHornos(self, hornoSeleccionado, playButtonSelected):
        self.playHornos_flag = True 
        self.hornoSeleccionado_start = hornoSeleccionado
        self.playButtonSelected_start = playButtonSelected

    def playSolenoide_Mantas(self, solenoideOrManta, playButtonValve):
        self.playValve_flag = True
        self.valveSelected_start = solenoideOrManta
        self.playButtonValve = playButtonValve

    # Solenoide functions
    def playSolenoide(self):
        print("play Solenoide")

    def setLoadSolenoide(self, variable, equipoSeleccionado):
        self.variableSeleccionada = variable
        self.equipoSeleccionado = equipoSeleccionado
        self.MainWindow.setEnabled(False)
        MainWindow = QtWidgets.QMainWindow()
        self.calculadora = calculadora2.Ui_MainWindow()
        self.calculadora.setupUi_PID_reactor(MainWindow, variable, equipoSeleccionado, self.sectionVector, self.MainWindow, self.s)
        MainWindow.show()
        print("set load solenoide")

    def setInjectionSolenoide(self, variable, equipoSeleccionado):
        self.variableSeleccionada = variable
        self.equipoSeleccionado = equipoSeleccionado
        self.MainWindow.setEnabled(False)
        MainWindow = QtWidgets.QMainWindow()
        self.calculadora = calculadora2.Ui_MainWindow()
        self.calculadora.setupUi_PID_reactor(MainWindow, variable, equipoSeleccionado, self.sectionVector, self.MainWindow, self.s)
        MainWindow.show()
        print("set injection solenoide")

    # Mantas functions
    def setValueMantas(self, variable, equipoSeleccionado):

        self.variableSeleccionada = variable
        self.equipoSeleccionado = equipoSeleccionado
        self.MainWindow.setEnabled(False)
        MainWindow = QtWidgets.QMainWindow()
        self.calculadora = calculadora2.Ui_MainWindow()
        self.calculadora.setupUi_PID_reactor(MainWindow, variable, equipoSeleccionado, self.sectionVector, self.MainWindow, self.s)
        MainWindow.show()
        print("set value mantas")

    def presentValueMantas(self):
        print("present value mantas")

    def startStopMantas(self):
        print("Start stop mantas")

    # Bomba functions
    def startBomba(self):
        try:
            comando = bytes('start\r\n','UTF-8')
            self.sBomba.write(comando)
            lectura = self.sBomba.readline()
            print("leido start", lectura)
        except:
            pass

    def stopBomba(self):
        try:
            comando = bytes('stop\r\n','UTF-8')
            self.sBomba.write(comando)
            lectura = self.sBomba.readline()
            print("leido start", lectura)
        except:
            pass

    def pauseBomba(self):
        try:
            comando = bytes('pause\r\n','UTF-8')
            self.sBomba.write(comando)
            lectura = self.sBomba.readline()
            print("leido start", lectura)
        except:
            pass

    def setUpBomba(self):
        #self.MainWindow.setEnabled(False)
        print("set up bomba")
        self.MainWindow.setEnabled(False)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = setUpBombaMainWindow.Ui_MainWindow()
        self.ui.setupUi(MainWindow, self.sBomba, self.MainWindow)
        MainWindow.show()

    def actualizaValoresPIDTimer(self):
        global valorVariableAModificar, setValueFromCalculadora

        while True:
            if self.flag_DesactivaVista == True:
                break
            variablesReactor = self.instanciaModbus.readRegister_Reactor()

            self.variablesPIDReactor_MFC_PV = self.instanciaModbus.read_variablesVistaReactor_MFC_PV()

            try:
                setValue1String = self.decimalString(str(int(variablesReactor[27],16)))            
                self.pushButton_SV1.setText(setValue1String)
            except:
                pass  

            time.sleep(0.005)

            try:
                presentValue1String = self.decimalString(str(int(variablesReactor[26],16)))
                self.pushButton_PV1.setText(presentValue1String)
            except:
                pass

            time.sleep(0.005)

            try:
                rampa1 = self.decimalString(str(int(variablesReactor[31],16)))                   
                self.pushButton_R1.setText(rampa1)
            except:
                pass

            time.sleep(0.005)

            try:
                setValue2String = self.decimalString(str(int(variablesReactor[37],16)))
                self.pushButton_SV2.setText(setValue2String)
            except:
                pass  

            time.sleep(0.005)

            try:
                presentValue2String = self.decimalString(str(int(variablesReactor[36],16)))
                self.pushButton_PV2.setText(presentValue2String)
            except:
                pass

            time.sleep(0.005)

            try:
                rampa2 = self.decimalString(str(int(variablesReactor[41],16))) 
                self.pushButton_R2.setText(rampa2)
            except:
                pass

            time.sleep(0.005)

            try:
                setValue3String = self.decimalString(str(int(variablesReactor[47],16))) 
                self.pushButton_SV3.setText(setValue3String)
            except:
                pass

            time.sleep(0.005)

            try:
                presentValue3String = self.decimalString(str(int(variablesReactor[46],16)))  
                self.pushButton_PV3.setText(presentValue3String)
            except:
                pass

            time.sleep(0.005)

            try:
                rampa3 = self.decimalString(str(int(variablesReactor[51],16)))
                self.pushButton_R3.setText(rampa3)
            except:
                pass

            time.sleep(0.005)

            try:
                setValue4String = self.decimalString(str(int(variablesReactor[57],16)))
                self.pushButton_SV4.setText(setValue4String)
            except:
                pass

            time.sleep(0.005)

            try:
                presentValue4String = self.decimalString(str(int(variablesReactor[56],16))) 
                self.pushButton_PV4.setText(presentValue4String)
            except:
                pass

            time.sleep(0.005)

            try:
                rampa4 = self.decimalString(str(int(variablesReactor[61],16))) 
                self.pushButton_R4.setText(rampa4)
            except:
                pass

            time.sleep(0.005)

            try:
                svFlujo1String = self.decimalString(str(int(variablesReactor[0],16))) 
                self.pushButton_SV_flujo1.setText(svFlujo1String) 
            except:
                pass

            time.sleep(0.005)

            try:
                svFlujo2String = self.decimalString(str(int(variablesReactor[1],16))) 
                self.pushButton_SV_flujo2.setText(svFlujo2String)  
            except:
                pass

            time.sleep(0.005)

            try:
                svFLujo3String = self.decimalString(str(int(variablesReactor[2],16)))
                self.pushButton_SV_flujo3.setText(svFLujo3String)  
            except:
                pass

            time.sleep(0.005)

            try:
                svFlujo4String = self.decimalString(str(int(variablesReactor[3],16)))
                self.pushButton_SV_flujo4.setText(svFlujo4String) 
            except:
                pass

            time.sleep(0.005)

            try:
                svFlujo5String = self.decimalString(str(int(variablesReactor[4],16)))
                self.pushButton_SV_flujo5.setText(svFlujo5String) 
            except:
                pass

            time.sleep(0.005)

            try:
                svFlujo6String = self.decimalString(str(int(variablesReactor[5],16)))
                self.pushButton_SV_flujo6.setText(svFlujo6String) 
            except:
                pass

            time.sleep(0.005)

            try:
                pvFlujo1String = self.decimalString(str(int(self.variablesPIDReactor_MFC_PV[0],16)))
                self.pushButton_PV_flujo1.setText(pvFlujo1String) 
            except:
                pass

            time.sleep(0.005)

            try:
                pvFlujo2String = self.decimalString(str(int(self.variablesPIDReactor_MFC_PV[1],16))) 
                self.pushButton_PV_flujo2.setText(pvFlujo2String) 
            except:
                pass

            time.sleep(0.005)

            try:
                pvFlujo3String = self.decimalString(str(int(self.variablesPIDReactor_MFC_PV[2],16))) 
                self.pushButton_PV_flujo3.setText(pvFlujo3String)  
            except:
                pass

            time.sleep(0.005)

            try:
                pvFlujo4String = self.decimalString(str(int(self.variablesPIDReactor_MFC_PV[3],16)))
                self.pushButton_PV_flujo4.setText(pvFlujo4String) 
            except:
                pass

            time.sleep(0.005)

            try:
                pvFlujo5String = self.decimalString(str(int(self.variablesPIDReactor_MFC_PV[4],16)))
                self.pushButton_PV_flujo5.setText(pvFlujo5String) 
            except:
                pass

            time.sleep(0.005)

            try:
                pvFlujo6String = self.decimalString(str(int(self.variablesPIDReactor_MFC_PV[5],16)))
                self.pushButton_PV_flujo6.setText(pvFlujo6String) 
            except:
                pass

            time.sleep(0.005)

            # Injection solenoide vista reactor
            try:
                injectionSolenoideString = self.decimalString(str(int(variablesReactor[23],16)))
                self.pushButtonInjectionSolenoide.setText(injectionSolenoideString)
            except:
                pass

            time.sleep(0.005)

            # Load solenoide vista reactor
            try:
                loadSolenoideString = self.decimalString(str(int(variablesReactor[24],16))) 
                self.pushButtonLoadSolenoide.setText(loadSolenoideString) 
            except:
                pass

            time.sleep(0.005)

            # Present Value vista reactor
            try:
                presentValueMantasString = self.decimalString(str(int(variablesReactor[66],16)))
                self.pushButtonPresentValueMantas.setText(presentValueMantasString)
            except:
                pass

            time.sleep(0.005)

            # Set Value vista reactor
            try:
                setValueMantasString = self.decimalString(str(int(variablesReactor[67],16)))
                self.pushButtonSetValueMantas.setText(setValueMantasString)
            except:
                pass

            # Visualiza el valor de las mantas
            try:
                if(self.allVisibleMantas == True):
                    variablesMantas = self.instanciaModbus.readRegister_ReactorMantas()

                    setValueManta1String = "1:  " + self.decimalString(str(int(variablesMantas[0],16)))
                    self.pushButtonManta1.setText(setValueManta1String)

                    time.sleep(0.005)

                    setValueManta2String = "2:  " + self.decimalString(str(int(variablesMantas[1],16)))
                    self.pushButtonManta2.setText(setValueManta2String)

                    time.sleep(0.005)

                    setValueManta3String = "3:  " + self.decimalString(str(int(variablesMantas[2],16)))
                    self.pushButtonManta3.setText(setValueManta3String)

                    time.sleep(0.005)

                    setValueManta4String = "4:  " + self.decimalString(str(int(variablesMantas[3],16)))
                    self.pushButtonManta4.setText(setValueManta4String)

                    time.sleep(0.005)

                    setValueManta5String = "5:  " + self.decimalString(str(int(variablesMantas[4],16)))
                    self.pushButtonManta5.setText(setValueManta5String)

                    time.sleep(0.005)

                    setValueManta6String = "6:  " + self.decimalString(str(int(variablesMantas[5],16)))
                    self.pushButtonManta6.setText(setValueManta6String)

                    time.sleep(0.005)

                    setValueManta7String = "7:  " + self.decimalString(str(int(variablesMantas[6],16)))
                    self.pushButtonManta7.setText(setValueManta7String)

                    time.sleep(0.005)

                    setValueManta8String = "8:  " + self.decimalString(str(int(variablesMantas[7],16)))
                    self.pushButtonManta8.setText(setValueManta8String)

                    time.sleep(0.005)
            except:
                pass        


            hora = time.strftime("%H:%M:%S")
            date = time.strftime("%d-%m-%Y")

            try:
                self.buttonTime.setText(hora)
            except:
                pass
            
            # setvalues: horno1, horno2, horno3, horno4, MCF1, MCF2, MCF3, MCF4, MCF5, MCF6
            
            self.contadorAlmacenaDatos = self.contadorAlmacenaDatos + 1
            # Almacena datos aproximadamente cada minuto, el timer cuenta cada 0.2 seg (5 veces para un segundo), el contador llega a 300 = 5*60
            print(self.contadorAlmacenaDatos)

            if(self.contadorAlmacenaDatos >= 200):
                try:       
                    fileRegisters = open("/home/pi/Desktop/historicRegisters/" + str(date), "a")
                    fileRegistersRead = open("/home/pi/Desktop/historicRegisters/" + str(date))
                    #fileRegisters = open("/Users/EstebanGarcia/Desktop/historicRegisters/" + str(date), "a")
                    #fileRegistersRead = open("/Users/EstebanGarcia/Desktop/historicRegisters/" + str(date))
                    if(len(fileRegistersRead.read()) == 0):
                        fileRegisters.write("hora" + "      " + "SV_H1" + " " + "PV_H1" + " " +  "SV_H2" + " " + "PV_H2" + " " +  "SV_H3" + " " + "PV_H3" + " " +  "SV_H4" + " " + "PV_H4" + " " +  "SV_MFC1" + " " + "PV_MFC1" + " " +  "SV_MFC2" + " " + "PV_MFC2" + " " +  "SV_MFC3" + " " + "PV_MFC3" + " " +  "SV_MFC4" + " " + "PV_MFC4" + " " +  "SV_MFC5" + " " + "PV_MFC5" + " " +  "SV_MFC6" + " " + "PV_MFC6" + " " + "SV_Mantas" + " " + "PV_Mantas" + "\n")
                    else:
                        fileRegisters.write(hora + "  " + setValue1String + "   " +  presentValue1String + "   " +  setValue2String + "   " +  presentValue2String + "   " +  setValue3String + "   " +  presentValue3String + "   " +  setValue4String + "   " +  presentValue4String + "   " +  svFlujo1String + "     " +  pvFlujo1String + "     " +  svFlujo2String + "     " +  pvFlujo2String + "     " +  str(int(variablesReactor[2],16)) + "       " +  pvFlujo3String + "     " +  svFlujo4String + "     " +  pvFlujo4String + "     " +  svFlujo5String + "     " +  pvFlujo5String + "     " +  svFlujo6String + "     " +  pvFlujo6String + "     " + setValueMantasString + "       " + presentValueMantasString + "\n")
                    fileRegisters.close()
                except:
                    pass
                self.contadorAlmacenaDatos = 0

            print(hora) 
            if self.playHornos_flag == True:
                self.playHornos_flag = False
                self.instanciaModbus.startHorno_reactor(self.hornoSeleccionado_start,self.playButtonSelected_start) 

            if self.playValve_flag == True:
                self.playValve_flag = False
                self.instanciaModbus.start_Valve_reactor(self.valveSelected_start, self.playButtonValve)

            if (setValueFromCalculadora == True):
                setValueFromCalculadora = False
                try:
                    self.instanciaModbus.writeValuesPID(float(valorVariableAModificar),self.variableSeleccionada,self.equipoSeleccionado)    
                except:
                    pass
            time.sleep(0.1)

    def decimalString(self, stringValue):
        stringValueReturn = stringValue
        if len(stringValueReturn)==1:
            stringValueReturn = '0.' + stringValueReturn
        else:   
            stringValueReturn = stringValueReturn[0:(len(stringValueReturn)-1)] + '.' + stringValueReturn[len(stringValueReturn)-1]
        return stringValueReturn

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet('QMainWindow{background-color: #333333; border:2px solid black;}')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
