# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/EstebanGarcia/Developer/reactorQuirema/interfaz/interfazQT/mainwindow_copy_copy_copy1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Home
import calculadora2
import serialClass
import threading
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, sectionVector, socket, socketBomba):
        global valorVariableAModificar, setValueFromCalculadora
        self.s = socket
        self.sBomba = socketBomba

        self.MainWindow = MainWindow
        self.sectionVector = sectionVector
        self.flag_DesactivaVista = False
        valorVariableAModificar = "0"
        setValueFromCalculadora = False

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 123, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 102, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 54, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 123, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 102, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 54, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 123, 125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 102, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 54, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 41, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(81, 82, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 81))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"font: 25 24pt \"Helvetica Neue\";")
        self.label.setObjectName("label")
        self.label_TITLE_FLOW1 = QtWidgets.QLabel(self.centralWidget)
        self.label_TITLE_FLOW1.setGeometry(QtCore.QRect(120, 90, 81, 21))
        self.label_TITLE_FLOW1.setStyleSheet("color:white")
        self.label_TITLE_FLOW1.setObjectName("label_TITLE_FLOW1")
        self.label_TITLE_FLOW2 = QtWidgets.QLabel(self.centralWidget)
        self.label_TITLE_FLOW2.setGeometry(QtCore.QRect(290, 90, 81, 20))
        self.label_TITLE_FLOW2.setStyleSheet("color:white")
        self.label_TITLE_FLOW2.setObjectName("label_TITLE_FLOW2")
        self.label_TITLE_FLOW3 = QtWidgets.QLabel(self.centralWidget)
        self.label_TITLE_FLOW3.setGeometry(QtCore.QRect(470, 90, 91, 20))
        self.label_TITLE_FLOW3.setStyleSheet("color:white")
        self.label_TITLE_FLOW3.setObjectName("label_TITLE_FLOW3")
        self.label_TITLE_FLOW4 = QtWidgets.QLabel(self.centralWidget)
        self.label_TITLE_FLOW4.setGeometry(QtCore.QRect(650, 90, 81, 20))
        self.label_TITLE_FLOW4.setStyleSheet("color:white")
        self.label_TITLE_FLOW4.setObjectName("label_TITLE_FLOW4")
        self.pushButton_XMAX_IN_1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_XMAX_IN_1.setGeometry(QtCore.QRect(80, 140, 65, 25))
        self.pushButton_XMAX_IN_1.setObjectName("pushButton_XMAX_IN_1")
        self.pushButton_XMAX_OUT_1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_XMAX_OUT_1.setGeometry(QtCore.QRect(150, 140, 65, 25))
        self.pushButton_XMAX_OUT_1.setObjectName("pushButton_XMAX_OUT_1")
        self.pushButton_XMIN_IN_1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_XMIN_IN_1.setGeometry(QtCore.QRect(80, 170, 65, 25))
        self.pushButton_XMIN_IN_1.setObjectName("pushButton_XMIN_IN_1")
        self.pushButton_XMIN_OUT_1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_XMIN_OUT_1.setGeometry(QtCore.QRect(150, 170, 65, 25))
        self.pushButton_XMIN_OUT_1.setObjectName("pushButton_XMIN_OUT_1")
        self.pushButton_YMAX_IN_1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_YMAX_IN_1.setGeometry(QtCore.QRect(80, 200, 65, 25))
        self.pushButton_YMAX_IN_1.setObjectName("pushButton_YMAX_IN_1")
        self.pushButton_YMAX_OUT_1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_YMAX_OUT_1.setGeometry(QtCore.QRect(150, 200, 65, 25))
        self.pushButton_YMAX_OUT_1.setObjectName("pushButton_YMAX_OUT_1")
        self.pushButton_YMIN_IN_1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_YMIN_IN_1.setGeometry(QtCore.QRect(80, 230, 65, 25))
        self.pushButton_YMIN_IN_1.setObjectName("pushButton_YMIN_IN_1")
        self.pushButton_YMIN_OUT_1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_YMIN_OUT_1.setGeometry(QtCore.QRect(150, 230, 65, 25))
        self.pushButton_YMIN_OUT_1.setObjectName("pushButton_YMIN_OUT_1")
        self.pushButton_XMAX_IN_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_XMAX_IN_2.setGeometry(QtCore.QRect(260, 140, 65, 25))
        self.pushButton_XMAX_IN_2.setObjectName("pushButton_XMAX_IN_2")
        self.pushButton_XMAX_OUT_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_XMAX_OUT_2.setGeometry(QtCore.QRect(330, 140, 65, 25))
        self.pushButton_XMAX_OUT_2.setObjectName("pushButton_XMAX_OUT_2")
        self.pushButton_YMIN_IN_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_YMIN_IN_2.setGeometry(QtCore.QRect(260, 230, 65, 25))
        self.pushButton_YMIN_IN_2.setObjectName("pushButton_YMIN_IN_2")
        self.pushButton_XMIN_IN_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_XMIN_IN_2.setGeometry(QtCore.QRect(260, 170, 65, 25))
        self.pushButton_XMIN_IN_2.setObjectName("pushButton_XMIN_IN_2")
        self.pushButton_YMAX_OUT_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_YMAX_OUT_2.setGeometry(QtCore.QRect(330, 200, 65, 25))
        self.pushButton_YMAX_OUT_2.setObjectName("pushButton_YMAX_OUT_2")
        self.pushButton_YMIN_OUT_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_YMIN_OUT_2.setGeometry(QtCore.QRect(330, 230, 65, 25))
        self.pushButton_YMIN_OUT_2.setObjectName("pushButton_YMIN_OUT_2")
        self.pushButton_XMIN_OUT_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_XMIN_OUT_2.setGeometry(QtCore.QRect(330, 170, 65, 25))
        self.pushButton_XMIN_OUT_2.setObjectName("pushButton_XMIN_OUT_2")
        self.pushButton_YMAX_IN_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_YMAX_IN_2.setGeometry(QtCore.QRect(260, 200, 65, 25))
        self.pushButton_YMAX_IN_2.setObjectName("pushButton_YMAX_IN_2")
        self.pushButton_XMAX_IN_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_XMAX_IN_3.setGeometry(QtCore.QRect(440, 140, 65, 25))
        self.pushButton_XMAX_IN_3.setObjectName("pushButton_XMAX_IN_3")
        self.pushButton_XMAX_OUT_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_XMAX_OUT_3.setGeometry(QtCore.QRect(510, 140, 65, 25))
        self.pushButton_XMAX_OUT_3.setObjectName("pushButton_XMAX_OUT_3")
        self.pushButton_YMIN_IN_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_YMIN_IN_3.setGeometry(QtCore.QRect(440, 230, 65, 25))
        self.pushButton_YMIN_IN_3.setObjectName("pushButton_YMIN_IN_3")
        self.pushButton_XMIN_IN_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_XMIN_IN_3.setGeometry(QtCore.QRect(440, 170, 65, 25))
        self.pushButton_XMIN_IN_3.setObjectName("pushButton_XMIN_IN_3")
        self.pushButton_YMAX_OUT_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_YMAX_OUT_3.setGeometry(QtCore.QRect(510, 200, 65, 25))
        self.pushButton_YMAX_OUT_3.setObjectName("pushButton_YMAX_OUT_3")
        self.pushButton_YMIN_OUT_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_YMIN_OUT_3.setGeometry(QtCore.QRect(510, 230, 65, 25))
        self.pushButton_YMIN_OUT_3.setObjectName("pushButton_YMIN_OUT_3")
        self.pushButton_XMIN_OUT_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_XMIN_OUT_3.setGeometry(QtCore.QRect(510, 170, 65, 25))
        self.pushButton_XMIN_OUT_3.setObjectName("pushButton_XMIN_OUT_3")
        self.pushButton_YMAX_IN_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_YMAX_IN_3.setGeometry(QtCore.QRect(440, 200, 65, 25))
        self.pushButton_YMAX_IN_3.setObjectName("pushButton_YMAX_IN_3")
        self.pushButton_XMAX_IN_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_XMAX_IN_4.setGeometry(QtCore.QRect(610, 140, 65, 25))
        self.pushButton_XMAX_IN_4.setObjectName("pushButton_XMAX_IN_4")
        self.pushButton_XMAX_OUT_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_XMAX_OUT_4.setGeometry(QtCore.QRect(680, 140, 65, 25))
        self.pushButton_XMAX_OUT_4.setObjectName("pushButton_XMAX_OUT_4")
        self.pushButton_YMIN_IN_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_YMIN_IN_4.setGeometry(QtCore.QRect(610, 230, 65, 25))
        self.pushButton_YMIN_IN_4.setObjectName("pushButton_YMIN_IN_4")
        self.pushButton_XMIN_IN_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_XMIN_IN_4.setGeometry(QtCore.QRect(610, 170, 65, 25))
        self.pushButton_XMIN_IN_4.setObjectName("pushButton_XMIN_IN_4")
        self.pushButton_YMAX_OUT_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_YMAX_OUT_4.setGeometry(QtCore.QRect(680, 200, 65, 25))
        self.pushButton_YMAX_OUT_4.setObjectName("pushButton_YMAX_OUT_4")
        self.pushButton_YMIN_OUT_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_YMIN_OUT_4.setGeometry(QtCore.QRect(680, 230, 65, 25))
        self.pushButton_YMIN_OUT_4.setObjectName("pushButton_YMIN_OUT_4")
        self.pushButton_XMIN_OUT_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_XMIN_OUT_4.setGeometry(QtCore.QRect(680, 170, 65, 25))
        self.pushButton_XMIN_OUT_4.setObjectName("pushButton_XMIN_OUT_4")
        self.pushButton_YMAX_IN_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_YMAX_IN_4.setGeometry(QtCore.QRect(610, 200, 65, 25))
        self.pushButton_YMAX_IN_4.setObjectName("pushButton_YMAX_IN_4")
        self.label_XMAX = QtWidgets.QLabel(self.centralWidget)
        self.label_XMAX.setGeometry(QtCore.QRect(30, 145, 51, 21))
        self.label_XMAX.setStyleSheet("color:white")
        self.label_XMAX.setObjectName("label_XMAX")
        self.label_XMIN = QtWidgets.QLabel(self.centralWidget)
        self.label_XMIN.setGeometry(QtCore.QRect(30, 180, 51, 21))
        self.label_XMIN.setStyleSheet("color:white")
        self.label_XMIN.setObjectName("label_XMIN")
        self.label_YMAX = QtWidgets.QLabel(self.centralWidget)
        self.label_YMAX.setGeometry(QtCore.QRect(30, 210, 51, 21))
        self.label_YMAX.setStyleSheet("color:white")
        self.label_YMAX.setObjectName("label_YMAX")
        self.label_YMIN = QtWidgets.QLabel(self.centralWidget)
        self.label_YMIN.setGeometry(QtCore.QRect(30, 240, 51, 21))
        self.label_YMIN.setStyleSheet("color:white")
        self.label_YMIN.setObjectName("label_YMIN")
        self.label_IN_FLOW1 = QtWidgets.QLabel(self.centralWidget)
        self.label_IN_FLOW1.setGeometry(QtCore.QRect(90, 120, 60, 16))
        self.label_IN_FLOW1.setStyleSheet("color:white")
        self.label_IN_FLOW1.setObjectName("label_IN_FLOW1")
        self.label_OUT_FLOW1 = QtWidgets.QLabel(self.centralWidget)
        self.label_OUT_FLOW1.setGeometry(QtCore.QRect(160, 120, 60, 16))
        self.label_OUT_FLOW1.setStyleSheet("color:white")
        self.label_OUT_FLOW1.setObjectName("label_OUT_FLOW1")
        self.label_IN_FLOW2 = QtWidgets.QLabel(self.centralWidget)
        self.label_IN_FLOW2.setGeometry(QtCore.QRect(270, 120, 60, 16))
        self.label_IN_FLOW2.setStyleSheet("color:white")
        self.label_IN_FLOW2.setObjectName("label_IN_FLOW2")
        self.label_OUT_FLOW2 = QtWidgets.QLabel(self.centralWidget)
        self.label_OUT_FLOW2.setGeometry(QtCore.QRect(340, 120, 60, 16))
        self.label_OUT_FLOW2.setStyleSheet("color:white")
        self.label_OUT_FLOW2.setObjectName("label_OUT_FLOW2")
        self.label_IN_FLOW3 = QtWidgets.QLabel(self.centralWidget)
        self.label_IN_FLOW3.setGeometry(QtCore.QRect(450, 120, 60, 16))
        self.label_IN_FLOW3.setStyleSheet("color:white")
        self.label_IN_FLOW3.setObjectName("label_IN_FLOW3")
        self.label_OUT_FLOW3 = QtWidgets.QLabel(self.centralWidget)
        self.label_OUT_FLOW3.setGeometry(QtCore.QRect(520, 120, 60, 16))
        self.label_OUT_FLOW3.setStyleSheet("color:white")
        self.label_OUT_FLOW3.setObjectName("label_OUT_FLOW3")
        self.label_IN_FLOW4 = QtWidgets.QLabel(self.centralWidget)
        self.label_IN_FLOW4.setGeometry(QtCore.QRect(620, 120, 60, 16))
        self.label_IN_FLOW4.setStyleSheet("color:white")
        self.label_IN_FLOW4.setObjectName("label_IN_FLOW4")
        self.label_OUT_FLOW4 = QtWidgets.QLabel(self.centralWidget)
        self.label_OUT_FLOW4.setGeometry(QtCore.QRect(690, 120, 60, 16))
        self.label_OUT_FLOW4.setStyleSheet("color:white")
        self.label_OUT_FLOW4.setObjectName("label_OUT_FLOW4")
        self.label_XMIN_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_XMIN_2.setGeometry(QtCore.QRect(30, 340, 51, 21))
        self.label_XMIN_2.setStyleSheet("color:white")
        self.label_XMIN_2.setObjectName("label_XMIN_2")
        self.label_YMIN_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_YMIN_2.setGeometry(QtCore.QRect(30, 400, 51, 21))
        self.label_YMIN_2.setStyleSheet("color:white")
        self.label_YMIN_2.setObjectName("label_YMIN_2")
        self.pushButton_XMAX_IN_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_XMAX_IN_5.setGeometry(QtCore.QRect(80, 300, 65, 25))
        self.pushButton_XMAX_IN_5.setObjectName("pushButton_XMAX_IN_5")
        self.pushButton_XMAX_OUT_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_XMAX_OUT_5.setGeometry(QtCore.QRect(150, 300, 65, 25))
        self.pushButton_XMAX_OUT_5.setObjectName("pushButton_XMAX_OUT_5")
        self.label_XMAX_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_XMAX_2.setGeometry(QtCore.QRect(30, 305, 51, 21))
        self.label_XMAX_2.setStyleSheet("color:white")
        self.label_XMAX_2.setObjectName("label_XMAX_2")
        self.pushButton_YMIN_IN_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_YMIN_IN_5.setGeometry(QtCore.QRect(80, 390, 65, 25))
        self.pushButton_YMIN_IN_5.setObjectName("pushButton_YMIN_IN_5")
        self.pushButton_XMIN_IN_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_XMIN_IN_5.setGeometry(QtCore.QRect(80, 330, 65, 25))
        self.pushButton_XMIN_IN_5.setObjectName("pushButton_XMIN_IN_5")
        self.pushButton_YMAX_OUT_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_YMAX_OUT_5.setGeometry(QtCore.QRect(150, 360, 65, 25))
        self.pushButton_YMAX_OUT_5.setObjectName("pushButton_YMAX_OUT_5")
        self.pushButton_YMIN_OUT_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_YMIN_OUT_5.setGeometry(QtCore.QRect(150, 390, 65, 25))
        self.pushButton_YMIN_OUT_5.setObjectName("pushButton_YMIN_OUT_5")
        self.label_YMAX_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_YMAX_2.setGeometry(QtCore.QRect(30, 370, 51, 21))
        self.label_YMAX_2.setStyleSheet("color:white")
        self.label_YMAX_2.setObjectName("label_YMAX_2")
        self.pushButton_XMIN_OUT_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_XMIN_OUT_5.setGeometry(QtCore.QRect(150, 330, 65, 25))
        self.pushButton_XMIN_OUT_5.setObjectName("pushButton_XMIN_OUT_5")
        self.pushButton_YMAX_IN_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_YMAX_IN_5.setGeometry(QtCore.QRect(80, 360, 65, 25))
        self.pushButton_YMAX_IN_5.setObjectName("pushButton_YMAX_IN_5")
        self.pushButton_XMAX_IN_6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_XMAX_IN_6.setGeometry(QtCore.QRect(260, 300, 65, 25))
        self.pushButton_XMAX_IN_6.setObjectName("pushButton_XMAX_IN_6")
        self.pushButton_XMAX_OUT_6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_XMAX_OUT_6.setGeometry(QtCore.QRect(330, 300, 65, 25))
        self.pushButton_XMAX_OUT_6.setObjectName("pushButton_XMAX_OUT_6")
        self.pushButton_XMIN_IN_6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_XMIN_IN_6.setGeometry(QtCore.QRect(260, 330, 65, 25))
        self.pushButton_XMIN_IN_6.setObjectName("pushButton_XMIN_IN_6")
        self.pushButton_YMIN_IN_6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_YMIN_IN_6.setGeometry(QtCore.QRect(260, 390, 65, 25))
        self.pushButton_YMIN_IN_6.setObjectName("pushButton_YMIN_IN_6")
        self.pushButton_YMAX_OUT_6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_YMAX_OUT_6.setGeometry(QtCore.QRect(330, 360, 65, 25))
        self.pushButton_YMAX_OUT_6.setObjectName("pushButton_YMAX_OUT_6")
        self.pushButton_YMAX_IN_6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_YMAX_IN_6.setGeometry(QtCore.QRect(260, 360, 65, 25))
        self.pushButton_YMAX_IN_6.setObjectName("pushButton_YMAX_IN_6")
        self.pushButton_YMIN_OUT_6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_YMIN_OUT_6.setGeometry(QtCore.QRect(330, 390, 65, 25))
        self.pushButton_YMIN_OUT_6.setObjectName("pushButton_YMIN_OUT_6")
        self.pushButton_XMIN_OUT_6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_XMIN_OUT_6.setGeometry(QtCore.QRect(330, 330, 65, 25))
        self.pushButton_XMIN_OUT_6.setObjectName("pushButton_XMIN_OUT_6")
        self.label_TITLE_FLOW5 = QtWidgets.QLabel(self.centralWidget)
        self.label_TITLE_FLOW5.setGeometry(QtCore.QRect(110, 280, 81, 20))
        self.label_TITLE_FLOW5.setStyleSheet("color:white")
        self.label_TITLE_FLOW5.setObjectName("label_TITLE_FLOW5")
        self.label_TITLE_FLOW6 = QtWidgets.QLabel(self.centralWidget)
        self.label_TITLE_FLOW6.setGeometry(QtCore.QRect(290, 280, 81, 20))
        self.label_TITLE_FLOW6.setStyleSheet("color:white")
        self.label_TITLE_FLOW6.setObjectName("label_TITLE_FLOW6")
        self.label_26 = QtWidgets.QLabel(self.centralWidget)
        self.label_26.setGeometry(QtCore.QRect(650, 0, 151, 81))
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap("../images/quirema.png"))
        self.label_26.setScaledContents(True)
        self.label_26.setObjectName("label_26")
        self.pushButton_HOME = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_HOME.setGeometry(QtCore.QRect(0, 0, 91, 81))
        self.pushButton_HOME.setText("")
        self.pushButton_HOME.setObjectName("pushButton_HOME")
        self.label_27 = QtWidgets.QLabel(self.centralWidget)
        self.label_27.setGeometry(QtCore.QRect(480, 270, 241, 161))
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap("../images/ecuacion.jpg"))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
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

        self.buttonTime= QtWidgets.QPushButton(self.centralWidget)
        self.buttonTime.setGeometry(QtCore.QRect(500, 25, 90, 30))
        self.buttonTime.setObjectName("pushButtonTime")
        self.buttonTime.setStyleSheet("background-color:#2F4F4F; color: white")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quirema"))
        self.label.setText(_translate("MainWindow", "              Quirema                           Reactor"))
        self.label_TITLE_FLOW1.setText(_translate("MainWindow", "C. Flujo 1"))
        self.label_TITLE_FLOW2.setText(_translate("MainWindow", "C. Flujo 2"))
        self.label_TITLE_FLOW3.setText(_translate("MainWindow", "C. Flujo 3"))
        self.label_TITLE_FLOW4.setText(_translate("MainWindow", "C. Flujo 4"))
        self.pushButton_XMAX_IN_1.setText(_translate("MainWindow", "0.0"))
        self.pushButton_XMAX_OUT_1.setText(_translate("MainWindow", "0.0"))
        self.pushButton_XMIN_IN_1.setText(_translate("MainWindow", "0.0"))
        self.pushButton_XMIN_OUT_1.setText(_translate("MainWindow", "0.0"))
        self.pushButton_YMAX_IN_1.setText(_translate("MainWindow", "0.0"))
        self.pushButton_YMAX_OUT_1.setText(_translate("MainWindow", "0.0"))
        self.pushButton_YMIN_IN_1.setText(_translate("MainWindow", "0.0"))
        self.pushButton_YMIN_OUT_1.setText(_translate("MainWindow", "0.0"))
        self.pushButton_XMAX_IN_2.setText(_translate("MainWindow", "0.0"))
        self.pushButton_XMAX_OUT_2.setText(_translate("MainWindow", "0.0"))
        self.pushButton_YMIN_IN_2.setText(_translate("MainWindow", "0.0"))
        self.pushButton_XMIN_IN_2.setText(_translate("MainWindow", "0.0"))
        self.pushButton_YMAX_OUT_2.setText(_translate("MainWindow", "0.0"))
        self.pushButton_YMIN_OUT_2.setText(_translate("MainWindow", "0.0"))
        self.pushButton_XMIN_OUT_2.setText(_translate("MainWindow", "0.0"))
        self.pushButton_YMAX_IN_2.setText(_translate("MainWindow", "0.0"))
        self.pushButton_XMAX_IN_3.setText(_translate("MainWindow", "0.0"))
        self.pushButton_XMAX_OUT_3.setText(_translate("MainWindow", "0.0"))
        self.pushButton_YMIN_IN_3.setText(_translate("MainWindow", "0.0"))
        self.pushButton_XMIN_IN_3.setText(_translate("MainWindow", "0.0"))
        self.pushButton_YMAX_OUT_3.setText(_translate("MainWindow", "0.0"))
        self.pushButton_YMIN_OUT_3.setText(_translate("MainWindow", "0.0"))
        self.pushButton_XMIN_OUT_3.setText(_translate("MainWindow", "0.0"))
        self.pushButton_YMAX_IN_3.setText(_translate("MainWindow", "0.0"))
        self.pushButton_XMAX_IN_4.setText(_translate("MainWindow", "0.0"))
        self.pushButton_XMAX_OUT_4.setText(_translate("MainWindow", "0.0"))
        self.pushButton_YMIN_IN_4.setText(_translate("MainWindow", "0.0"))
        self.pushButton_XMIN_IN_4.setText(_translate("MainWindow", "0.0"))
        self.pushButton_YMAX_OUT_4.setText(_translate("MainWindow", "0.0"))
        self.pushButton_YMIN_OUT_4.setText(_translate("MainWindow", "0.0"))
        self.pushButton_XMIN_OUT_4.setText(_translate("MainWindow", "0.0"))
        self.pushButton_YMAX_IN_4.setText(_translate("MainWindow", "0.0"))
        self.label_XMAX.setText(_translate("MainWindow", "Xmax"))
        self.label_XMIN.setText(_translate("MainWindow", "Xmin"))
        self.label_YMAX.setText(_translate("MainWindow", "Ymax"))
        self.label_YMIN.setText(_translate("MainWindow", "Ymin"))
        self.label_IN_FLOW1.setText(_translate("MainWindow", "IN"))
        self.label_OUT_FLOW1.setText(_translate("MainWindow", "OUT"))
        self.label_IN_FLOW2.setText(_translate("MainWindow", "IN"))
        self.label_OUT_FLOW2.setText(_translate("MainWindow", "OUT"))
        self.label_IN_FLOW3.setText(_translate("MainWindow", "IN"))
        self.label_OUT_FLOW3.setText(_translate("MainWindow", "OUT"))
        self.label_IN_FLOW4.setText(_translate("MainWindow", "IN"))
        self.label_OUT_FLOW4.setText(_translate("MainWindow", "OUT"))
        self.label_XMIN_2.setText(_translate("MainWindow", "Xmin"))
        self.label_YMIN_2.setText(_translate("MainWindow", "Ymin"))
        self.pushButton_XMAX_IN_5.setText(_translate("MainWindow", "0.0"))
        self.pushButton_XMAX_OUT_5.setText(_translate("MainWindow", "0.0"))
        self.label_XMAX_2.setText(_translate("MainWindow", "Xmax"))
        self.pushButton_YMIN_IN_5.setText(_translate("MainWindow", "0.0"))
        self.pushButton_XMIN_IN_5.setText(_translate("MainWindow", "0.0"))
        self.pushButton_YMAX_OUT_5.setText(_translate("MainWindow", "0.0"))
        self.pushButton_YMIN_OUT_5.setText(_translate("MainWindow", "0.0"))
        self.label_YMAX_2.setText(_translate("MainWindow", "Ymax"))
        self.pushButton_XMIN_OUT_5.setText(_translate("MainWindow", "0.0"))
        self.pushButton_YMAX_IN_5.setText(_translate("MainWindow", "0.0"))
        self.pushButton_XMAX_IN_6.setText(_translate("MainWindow", "0.0"))
        self.pushButton_XMAX_OUT_6.setText(_translate("MainWindow", "0.0"))
        self.pushButton_XMIN_IN_6.setText(_translate("MainWindow", "0.0"))
        self.pushButton_YMIN_IN_6.setText(_translate("MainWindow", "0.0"))
        self.pushButton_YMAX_OUT_6.setText(_translate("MainWindow", "0.0"))
        self.pushButton_YMAX_IN_6.setText(_translate("MainWindow", "0.0"))
        self.pushButton_YMIN_OUT_6.setText(_translate("MainWindow", "0.0"))
        self.pushButton_XMIN_OUT_6.setText(_translate("MainWindow", "0.0"))
        self.label_TITLE_FLOW5.setText(_translate("MainWindow", "C. Flujo 5"))
        self.label_TITLE_FLOW6.setText(_translate("MainWindow", "C. Flujo 6"))

        self.actionButtons()
        #self.actualizaValoresPIDTimer()
        self.t = threading.Thread(target = self.actualizaValoresPIDTimer)
        self.t.IsBackground = True;
        self.t.start()

    def actionButtons(self):
        self.pushButton_HOME.setGeometry(QtCore.QRect(0, 7, 71, 71))
        self.pushButton_HOME.setStyleSheet("background-color: #222222; color:white; font-size: 22pt;")
        self.pushButton_HOME.setIcon(QtGui.QIcon('../images/home.png'))
        self.pushButton_HOME.setIconSize(QtCore.QSize(31,31))
        self.pushButton_HOME.clicked.connect(self.home)

        # IN
        self.pushButton_XMAX_IN_1.clicked.connect(lambda: self.displayCalculadora('MFC1','IN','XMAX'))
        self.pushButton_XMIN_IN_1.clicked.connect(lambda: self.displayCalculadora('MFC1','IN','XMIN'))
        self.pushButton_YMAX_IN_1.clicked.connect(lambda: self.displayCalculadora('MFC1','IN','YMAX'))
        self.pushButton_YMIN_IN_1.clicked.connect(lambda: self.displayCalculadora('MFC1','IN','YMIN'))

        self.pushButton_XMAX_IN_2.clicked.connect(lambda: self.displayCalculadora('MFC2','IN','XMAX'))
        self.pushButton_XMIN_IN_2.clicked.connect(lambda: self.displayCalculadora('MFC2','IN','XMIN'))
        self.pushButton_YMAX_IN_2.clicked.connect(lambda: self.displayCalculadora('MFC2','IN','YMAX'))
        self.pushButton_YMIN_IN_2.clicked.connect(lambda: self.displayCalculadora('MFC2','IN','YMIN'))

        self.pushButton_XMAX_IN_3.clicked.connect(lambda: self.displayCalculadora('MFC3','IN','XMAX'))
        self.pushButton_XMIN_IN_3.clicked.connect(lambda: self.displayCalculadora('MFC3','IN','XMIN'))
        self.pushButton_YMAX_IN_3.clicked.connect(lambda: self.displayCalculadora('MFC3','IN','YMAX'))
        self.pushButton_YMIN_IN_3.clicked.connect(lambda: self.displayCalculadora('MFC3','IN','YMIN'))

        self.pushButton_XMAX_IN_4.clicked.connect(lambda: self.displayCalculadora('MFC4','IN','XMAX'))
        self.pushButton_XMIN_IN_4.clicked.connect(lambda: self.displayCalculadora('MFC4','IN','XMIN'))
        self.pushButton_YMAX_IN_4.clicked.connect(lambda: self.displayCalculadora('MFC4','IN','YMAX'))
        self.pushButton_YMIN_IN_4.clicked.connect(lambda: self.displayCalculadora('MFC4','IN','YMIN'))

        self.pushButton_XMAX_IN_5.clicked.connect(lambda: self.displayCalculadora('MFC5','IN','XMAX'))
        self.pushButton_XMIN_IN_5.clicked.connect(lambda: self.displayCalculadora('MFC5','IN','XMIN'))
        self.pushButton_YMAX_IN_5.clicked.connect(lambda: self.displayCalculadora('MFC5','IN','YMAX'))
        self.pushButton_YMIN_IN_5.clicked.connect(lambda: self.displayCalculadora('MFC5','IN','YMIN'))

        self.pushButton_XMAX_IN_6.clicked.connect(lambda: self.displayCalculadora('MFC6','IN','XMAX'))
        self.pushButton_XMIN_IN_6.clicked.connect(lambda: self.displayCalculadora('MFC6','IN','XMIN'))
        self.pushButton_YMAX_IN_6.clicked.connect(lambda: self.displayCalculadora('MFC6','IN','YMAX'))
        self.pushButton_YMIN_IN_6.clicked.connect(lambda: self.displayCalculadora('MFC6','IN','YMIN'))

        # OUT
        self.pushButton_XMAX_OUT_1.clicked.connect(lambda: self.displayCalculadora('MFC1','OUT','XMAX'))
        self.pushButton_XMIN_OUT_1.clicked.connect(lambda: self.displayCalculadora('MFC1','OUT','XMIN'))
        self.pushButton_YMAX_OUT_1.clicked.connect(lambda: self.displayCalculadora('MFC1','OUT','YMAX'))
        self.pushButton_YMIN_OUT_1.clicked.connect(lambda: self.displayCalculadora('MFC1','OUT','YMIN'))

        self.pushButton_XMAX_OUT_2.clicked.connect(lambda: self.displayCalculadora('MFC2','OUT','XMAX'))
        self.pushButton_XMIN_OUT_2.clicked.connect(lambda: self.displayCalculadora('MFC2','OUT','XMIN'))
        self.pushButton_YMAX_OUT_2.clicked.connect(lambda: self.displayCalculadora('MFC2','OUT','YMAX'))
        self.pushButton_YMIN_OUT_2.clicked.connect(lambda: self.displayCalculadora('MFC2','OUT','YMIN'))

        self.pushButton_XMAX_OUT_3.clicked.connect(lambda: self.displayCalculadora('MFC3','OUT','XMAX'))
        self.pushButton_XMIN_OUT_3.clicked.connect(lambda: self.displayCalculadora('MFC3','OUT','XMIN'))
        self.pushButton_YMAX_OUT_3.clicked.connect(lambda: self.displayCalculadora('MFC3','OUT','YMAX'))
        self.pushButton_YMIN_OUT_3.clicked.connect(lambda: self.displayCalculadora('MFC3','OUT','YMIN'))

        self.pushButton_XMAX_OUT_4.clicked.connect(lambda: self.displayCalculadora('MFC4','OUT','XMAX'))
        self.pushButton_XMIN_OUT_4.clicked.connect(lambda: self.displayCalculadora('MFC4','OUT','XMIN'))
        self.pushButton_YMAX_OUT_4.clicked.connect(lambda: self.displayCalculadora('MFC4','OUT','YMAX'))
        self.pushButton_YMIN_OUT_4.clicked.connect(lambda: self.displayCalculadora('MFC4','OUT','YMIN'))

        self.pushButton_XMAX_OUT_5.clicked.connect(lambda: self.displayCalculadora('MFC5','OUT','XMAX'))
        self.pushButton_XMIN_OUT_5.clicked.connect(lambda: self.displayCalculadora('MFC5','OUT','XMIN'))
        self.pushButton_YMAX_OUT_5.clicked.connect(lambda: self.displayCalculadora('MFC5','OUT','YMAX'))
        self.pushButton_YMIN_OUT_5.clicked.connect(lambda: self.displayCalculadora('MFC5','OUT','YMIN'))

        self.pushButton_XMAX_OUT_6.clicked.connect(lambda: self.displayCalculadora('MFC6','OUT','XMAX'))
        self.pushButton_XMIN_OUT_6.clicked.connect(lambda: self.displayCalculadora('MFC6','OUT','XMIN'))
        self.pushButton_YMAX_OUT_6.clicked.connect(lambda: self.displayCalculadora('MFC6','OUT','YMAX'))
        self.pushButton_YMIN_OUT_6.clicked.connect(lambda: self.displayCalculadora('MFC6','OUT','YMIN'))

    def home(self):
        self.flag_DesactivaVista = True
        self.home = Home.Ui_MainWindow()
        self.home.setupUi(self.MainWindow, self.s, self.sBomba)
        #self.t.cancel()

    def displayCalculadora(self, MFC, IN_OUT, X_Y):
        self.MainWindow.setEnabled(False)
        MainWindow = QtWidgets.QMainWindow()
        self.calculadora = calculadora2.Ui_MainWindow()
        self.controladorFlujo = MFC
        self.IN_OUT = IN_OUT
        self.X_Y = X_Y
        self.calculadora.setupUI_escalado(MainWindow, self.sectionVector, MFC, IN_OUT, X_Y, self.MainWindow, self.s)
        MainWindow.show() 

    def actualizaValoresPIDTimer(self):
        global valorVariableAModificar, setValueFromCalculadora

        while True:
            self.instanciaModbus = serialClass.modbus(self.s)
            self.variablesPIDEscalado = self.instanciaModbus.readVarialesVistaEscalado()
            print(self.variablesPIDEscalado)
            print(valorVariableAModificar, setValueFromCalculadora)

            if(self.flag_DesactivaVista==True):
                break
            # IN:
            try:
                xmaxIn1String = self.decimalString(str(int(self.variablesPIDEscalado[0],16)))
                self.pushButton_XMAX_IN_1.setText(xmaxIn1String)
            except:
                pass

            time.sleep(0.005)

            try:
                xminIn1String = self.decimalString(str(int(self.variablesPIDEscalado[1],16)))
                self.pushButton_XMIN_IN_1.setText(xminIn1String)
            except:
                pass  

            time.sleep(0.005) 

            try:
                ymaxIn1String = self.decimalString(str(int(self.variablesPIDEscalado[2],16)))
                self.pushButton_YMAX_IN_1.setText(ymaxIn1String)
            except:
                pass

            time.sleep(0.005)

            try:   
                yminIn1String = self.decimalString(str(int(self.variablesPIDEscalado[3],16))) 
                self.pushButton_YMIN_IN_1.setText(yminIn1String)
            except:
                pass

            time.sleep(0.005)

            try:
                xmaxIn2String = self.decimalString(str(int(self.variablesPIDEscalado[4],16)))
                self.pushButton_XMAX_IN_2.setText(xmaxIn2String)
            except:
                pass

            time.sleep(0.005)

            try:
                xminIn2String = self.decimalString(str(int(self.variablesPIDEscalado[5],16)))
                self.pushButton_XMIN_IN_2.setText(xminIn2String)
            except:
                pass

            time.sleep(0.005)

            try:
                ymaxIn2String = self.decimalString(str(int(self.variablesPIDEscalado[6],16)))
                self.pushButton_YMAX_IN_2.setText(ymaxIn2String)
            except:
                pass

            time.sleep(0.005)

            try:
                yminIn2String = self.decimalString(str(int(self.variablesPIDEscalado[7],16))) 
                self.pushButton_YMIN_IN_2.setText(yminIn2String)
            except:
                pass

            time.sleep(0.005)

            try:
                xmaxIn3String = self.decimalString(str(int(self.variablesPIDEscalado[8],16)))
                self.pushButton_XMAX_IN_3.setText(xmaxIn3String)
            except:
                pass

            time.sleep(0.005)

            try:
                xminIn3String = self.decimalString(str(int(self.variablesPIDEscalado[9],16)))
                self.pushButton_XMIN_IN_3.setText(xminIn3String)
            except:
                pass
            time.sleep(0.005)

            try:
                ymaxIn3String = self.decimalString(str(int(self.variablesPIDEscalado[10],16)))
                self.pushButton_YMAX_IN_3.setText(ymaxIn3String)
            except:
                pass

            time.sleep(0.005)

            try:
                yminIn3String = self.decimalString(str(int(self.variablesPIDEscalado[11],16))) 
                self.pushButton_YMIN_IN_3.setText(yminIn3String)
            except:
                pass

            time.sleep(0.005)

            try:
                xmaxIn4String = self.decimalString(str(int(self.variablesPIDEscalado[12],16)))
                self.pushButton_XMAX_IN_4.setText(xmaxIn4String)
            except:
                pass

            time.sleep(0.005)

            try:
                xminIn4String = self.decimalString(str(int(self.variablesPIDEscalado[13],16)))
                self.pushButton_XMIN_IN_4.setText(xminIn4String)
            except:
                pass

            time.sleep(0.005)

            try:
                ymaxIn4String = self.decimalString(str(int(self.variablesPIDEscalado[14],16)))
                self.pushButton_YMAX_IN_4.setText(ymaxIn4String)
            except:
                pass

            time.sleep(0.005)

            try:
                yminIn4String = self.decimalString(str(int(self.variablesPIDEscalado[15],16))) 
                self.pushButton_YMIN_IN_4.setText(yminIn4String)
            except:
                pass

            time.sleep(0.005)

            try:
                xmaxIn5String = self.decimalString(str(int(self.variablesPIDEscalado[16],16)))
                self.pushButton_XMAX_IN_5.setText(xmaxIn5String)
            except:
                pass

            time.sleep(0.005)

            try:
                xminIn5String = self.decimalString(str(int(self.variablesPIDEscalado[17],16)))
                self.pushButton_XMIN_IN_5.setText(xminIn5String)
            except:
                pass

            time.sleep(0.005)

            try:
                ymaxIn5String = self.decimalString(str(int(self.variablesPIDEscalado[18],16)))
                self.pushButton_YMAX_IN_5.setText(ymaxIn5String)
            except:
                pass

            time.sleep(0.005)

            try:
                yminIn5String = self.decimalString(str(int(self.variablesPIDEscalado[19],16))) 
                self.pushButton_YMIN_IN_5.setText(yminIn5String)
            except:
                pass

            time.sleep(0.005)

            try:
                xmaxIn6String = self.decimalString(str(int(self.variablesPIDEscalado[20],16)))
                self.pushButton_XMAX_IN_6.setText(xmaxIn6String)
            except:
                pass

            time.sleep(0.005)

            try:
                xminIn6String = self.decimalString(str(int(self.variablesPIDEscalado[21],16)))
                self.pushButton_XMIN_IN_6.setText(xminIn6String)
            except:
                pass

            time.sleep(0.005)

            try:
                ymaxIn6String = self.decimalString(str(int(self.variablesPIDEscalado[22],16)))
                self.pushButton_YMAX_IN_6.setText(ymaxIn6String)
            except:
                pass

            time.sleep(0.005)

            try:
                yminIn6String = self.decimalString(str(int(self.variablesPIDEscalado[23],16))) 
                self.pushButton_YMIN_IN_6.setText(yminIn6String)
            except:
                pass
            
            time.sleep(0.005)
            # OUT:
            try:
                xmaxOut1String = self.decimalString(str(int(self.variablesPIDEscalado[25],16))) 
                self.pushButton_XMAX_OUT_1.setText(xmaxOut1String)
            except:
                pass

            time.sleep(0.005)

            try:
                xminOut1String = self.decimalString(str(int(self.variablesPIDEscalado[26],16)))
                self.pushButton_XMIN_OUT_1.setText(xminOut1String)
            except:
                pass

            time.sleep(0.005)

            try:
                ymaxOut1String = self.decimalString(str(int(self.variablesPIDEscalado[27],16)))
                self.pushButton_YMAX_OUT_1.setText(ymaxOut1String)
            except:
                pass

            time.sleep(0.005)

            try:
                yminOut1String = self.decimalString(str(int(self.variablesPIDEscalado[28],16))) 
                self.pushButton_YMIN_OUT_1.setText(yminOut1String)
            except:
                pass

            time.sleep(0.005)

            try:   
                xmaxOut2String = self.decimalString(str(int(self.variablesPIDEscalado[29],16)))         
                self.pushButton_XMAX_OUT_2.setText(xmaxOut2String)
            except:
                pass

            time.sleep(0.005)

            try:
                xminOut2String = self.decimalString(str(int(self.variablesPIDEscalado[30],16)))
                self.pushButton_XMIN_OUT_2.setText(xminOut2String)
            except:
                pass

            time.sleep(0.005)

            try:
                ymaxOut2String = self.decimalString(str(int(self.variablesPIDEscalado[31],16)))
                self.pushButton_YMAX_OUT_2.setText(ymaxOut2String)
            except:
                pass

            time.sleep(0.005)

            try:
                yminOut2String = self.decimalString(str(int(self.variablesPIDEscalado[32],16))) 
                self.pushButton_YMIN_OUT_2.setText(yminOut2String)
            except:
                pass

            time.sleep(0.005)

            try:
                xmaxOut3String = self.decimalString(str(int(self.variablesPIDEscalado[33],16)))              
                self.pushButton_XMAX_OUT_3.setText(xmaxOut3String)
            except:
                pass

            time.sleep(0.005)

            try:
                xminOut3String = self.decimalString(str(int(self.variablesPIDEscalado[34],16)))
                self.pushButton_XMIN_OUT_3.setText(xminOut3String)
            except:
                pass

            time.sleep(0.005)

            try:
                ymaxOut3String = self.decimalString(str(int(self.variablesPIDEscalado[35],16)))
                self.pushButton_YMAX_OUT_3.setText(ymaxOut3String)
            except:
                pass

            time.sleep(0.005)

            try:
                yminOut3String = self.decimalString(str(int(self.variablesPIDEscalado[36],16))) 
                self.pushButton_YMIN_OUT_3.setText(yminOut3String)
            except:
                pass

            time.sleep(0.005)

            try:
                xmaxOut4String = self.decimalString(str(int(self.variablesPIDEscalado[37],16))) 
                self.pushButton_XMAX_OUT_4.setText(xmaxOut4String)
            except:
                pass

            time.sleep(0.005)

            try:
                xminOut4String = self.decimalString(str(int(self.variablesPIDEscalado[38],16)))
                self.pushButton_XMIN_OUT_4.setText(xminOut4String)
            except:
                pass

            time.sleep(0.005)

            try:
                ymaxOut4String = self.decimalString(str(int(self.variablesPIDEscalado[39],16)))
                self.pushButton_YMAX_OUT_4.setText(ymaxOut4String)
            except:
                pass

            time.sleep(0.005)

            try:
                yminOut4String = self.decimalString(str(int(self.variablesPIDEscalado[40],16))) 
                self.pushButton_YMIN_OUT_4.setText(yminOut4String)
            except:
                pass

            time.sleep(0.005)

            try:
                xmaxOut5String = self.decimalString(str(int(self.variablesPIDEscalado[41],16))) 
                self.pushButton_XMAX_OUT_5.setText(xmaxOut5String)
            except:
                pass

            time.sleep(0.005)

            try:
                xminOut5String = self.decimalString(str(int(self.variablesPIDEscalado[42],16)))
                self.pushButton_XMIN_OUT_5.setText(xminOut5String)
            except:
                pass

            time.sleep(0.005)

            try:
                ymaxOut5String = self.decimalString(str(int(self.variablesPIDEscalado[43],16)))
                self.pushButton_YMAX_OUT_5.setText(ymaxOut5String)
            except:
                pass

            time.sleep(0.005)

            try:
                yminOut5String = self.decimalString(str(int(self.variablesPIDEscalado[44],16))) 
                self.pushButton_YMIN_OUT_5.setText(yminOut5String)
            except:
                pass

            time.sleep(0.005)


            try:
                xmaxOut6String = self.decimalString(str(int(self.variablesPIDEscalado[45],16)))
                self.pushButton_XMAX_OUT_6.setText(xmaxOut6String)
            except:
                pass

            time.sleep(0.005)

            try:
                xminOut6String = self.decimalString(str(int(self.variablesPIDEscalado[46],16)))
                self.pushButton_XMIN_OUT_6.setText(xminOut6String)
            except:
                pass

            time.sleep(0.005)

            try:
                ymaxOut6String = self.decimalString(str(int(self.variablesPIDEscalado[47],16)))
                self.pushButton_YMAX_OUT_6.setText(ymaxOut6String)
            except:
                pass

            time.sleep(0.005)

            try:
                yminOut6String = self.decimalString(str(int(self.variablesPIDEscalado[48],16))) 
                self.pushButton_YMIN_OUT_6.setText(yminOut6String)
            except:
                pass

            if (setValueFromCalculadora == True):
                setValueFromCalculadora = False

                self.instanciaModbus.writeValues_Escalado(float(valorVariableAModificar), self.controladorFlujo, self.IN_OUT, self.X_Y)

            time.sleep(0.2)

            hora = time.strftime("%H:%M:%S")

            try:
                self.buttonTime.setText(hora)
            except:
                pass

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
    app.setStyleSheet('QMainWindow{background-color: qlineargradient(spread:reflect, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(0, 64, 128, 255), stop:1 rgba(0, 0, 0, 255)); border:2px solid black;}')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
