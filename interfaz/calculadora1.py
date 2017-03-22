# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_copy_copy_copy_copy.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint
import setPID_parameters
import sqlite3
import sys
sys.path.append('../modbusComunication')
import serialClass
sys.path.append('../DB_SQL')
import dbSQLClass

import time

class Ui_MainWindow(object):
    def setupUi_PID_reactor(self, MainWindow, variablePIDSeleccionada, horno_manta_seleccionada, sectionVector, pidWindow):
        self.pidWindow = pidWindow
        self.variablePIDSeleccionada = variablePIDSeleccionada
        self.horno_manta_seleccionada = horno_manta_seleccionada
        self.instanciaModbus = serialClass.modbus()
        MainWindow.closeEvent = self.closeEvent_PID_reactor
        self.init_Interface(MainWindow, sectionVector)


    def setupUi_Alarmas(self, MainWindow, alarmaSeleccionada, buttonSelected, sectionVector, alarmWindow):
        self.alarmWindow = alarmWindow
        self.buttonSelected = buttonSelected
        self.alarmaSeleccionada = alarmaSeleccionada
        MainWindow.closeEvent = self.closeEvent_AlarmWindow
        self.init_Interface(MainWindow, sectionVector)
        self.instanciaBD_alarmas = dbSQLClass.DataBaseQueries()

    def setupUi_recetas(self, MainWindow, sectionVector, resetasMainWindow):
        self.resetasMainWindow = resetasMainWindow
        MainWindow.closeEvent = self.closeEvent_recetas
        self.init_Interface(MainWindow, sectionVector)

    def setupUI_escalado(self, MainWindow, sectionVector, controladorFlujo, IN_OUT, escaladoMainWindow):
        self.escaladoMainWindow = escaladoMainWindow
        MainWindow.closeEvent = self.closeEvent_escalado
        self.init_Interface(MainWindow, sectionVector)

    def init_Interface(self, MainWindow, sectionVector):

        self.setValueString = ""
        MainWindow.setStyleSheet('QMainWindow{background-color: white; border:2px solid black;}')
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(221, 351)

        qPoint = QPoint(300,60)
        MainWindow.move(qPoint)
        
        self.sectionVector = sectionVector

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 51, 51))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
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
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 51, 51))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 51, 51))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
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
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 51, 51))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
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
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 51, 51))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 51, 51))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
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
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 51, 51))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
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
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 51, 51))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 51, 51))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
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
        MainWindow.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 51, 51, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.ok_Button = QtWidgets.QPushButton(self.centralWidget)
        self.ok_Button.setGeometry(QtCore.QRect(10, 50, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.ok_Button.setFont(font)
        self.ok_Button.setStyleSheet("border-radius: 10px;background-color:white;")
        self.ok_Button.setObjectName("ok_Button")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_1.setGeometry(QtCore.QRect(20, 200, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("border-radius: 20px;background-color:white;")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 200, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-radius: 20px;background-color:white;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 200, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border-radius: 20px;background-color:white;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_6.setGeometry(QtCore.QRect(160, 150, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("border-radius: 20px;background-color:white;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 150, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("border-radius: 20px;background-color:white;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 150, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border-radius: 20px;background-color:white;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_9.setGeometry(QtCore.QRect(160, 100, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("border-radius: 20px;background-color:white;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_8.setGeometry(QtCore.QRect(90, 100, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("border-radius: 20px;background-color:white;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 100, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("border-radius: 20px;background-color:white;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_0.setGeometry(QtCore.QRect(20, 250, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setStyleSheet("border-radius: 20px;background-color:white;")
        self.pushButton_0.setObjectName("pushButton_0")
        self.clearAll_Button = QtWidgets.QPushButton(self.centralWidget)
        self.clearAll_Button.setGeometry(QtCore.QRect(160, 250, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.clearAll_Button.setFont(font)
        self.clearAll_Button.setStyleSheet("border-radius: 20px;background-color:white;")
        self.clearAll_Button.setObjectName("clearAll_Button")
        self.pushButton_point = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_point.setGeometry(QtCore.QRect(90, 250, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.pushButton_point.setFont(font)
        self.pushButton_point.setStyleSheet("border-radius: 20px;background-color:white;")
        self.pushButton_point.setObjectName("pushButton_point")
        self.clearButton = QtWidgets.QPushButton(self.centralWidget)
        self.clearButton.setGeometry(QtCore.QRect(160, 50, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.clearButton.setFont(font)
        self.clearButton.setStyleSheet("border-radius: 20px;background-color:white;")
        self.clearButton.setObjectName("clearButton")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 221, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quirema"))
        self.label.setText(_translate("MainWindow", "0.0"))
        self.ok_Button.setText(_translate("MainWindow", "OK"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.clearAll_Button.setText(_translate("MainWindow", "AC"))
        self.pushButton_point.setText(_translate("MainWindow", "."))
        self.clearButton.setText(_translate("MainWindow", "<"))

        self.ok_Button.clicked.connect(lambda: self.setValue('OK'))
        self.pushButton_1.clicked.connect(lambda: self.setValue('1'))
        self.pushButton_2.clicked.connect(lambda: self.setValue('2'))
        self.pushButton_3.clicked.connect(lambda: self.setValue('3'))
        self.pushButton_6.clicked.connect(lambda: self.setValue('6'))
        self.pushButton_5.clicked.connect(lambda: self.setValue('5'))
        self.pushButton_4.clicked.connect(lambda: self.setValue('4'))
        self.pushButton_9.clicked.connect(lambda: self.setValue('9'))
        self.pushButton_8.clicked.connect(lambda: self.setValue('8'))
        self.pushButton_7.clicked.connect(lambda: self.setValue('7'))
        self.pushButton_0.clicked.connect(lambda: self.setValue('0'))
        self.clearAll_Button.clicked.connect(lambda: self.setValue('AC'))
        self.pushButton_point.clicked.connect(lambda: self.setValue('.'))
        self.clearButton.clicked.connect(lambda: self.setValue('<'))

    def setValue(self, id_button):
        # Si el usuario selecciono los parametros PID
        if(self.sectionVector[0] == True):
            if id_button != "OK" and id_button != "AC" and id_button != "<":
                self.setValueString = self.setValueString + id_button
                self.label.setText(str(self.setValueString))
            
            if(id_button == "AC"):
                self.setValueString = ""
                self.label.setText(str(self.setValueString))

            if (id_button == "<"):
                self.setValueString = self.setValueString[0:len(self.setValueString)-1]
                self.label.setText(str(self.setValueString))

            if (id_button=="OK"):
                self.instanciaModbus.writeValuesPID(self.setValueString,self.variablePIDSeleccionada,self.horno_manta_seleccionada)

                self.MainWindow.close()
                self.setPID_parameters = setPID_parameters.Ui_MainWindow()
                self.pidWindow.setEnabled(True)
            
        # Si el usuario selecciona Reactor
        elif(self.sectionVector[5] == True):
            if id_button != "OK" and id_button != "AC" and id_button != "<":
                self.setValueString = self.setValueString + id_button
                self.label.setText(str(self.setValueString))

            if(id_button == "AC"):
                self.setValueString = ""
                self.label.setText(str(self.setValueString))
                
            if (id_button == "<"):
                self.setValueString = self.setValueString[0:len(self.setValueString)-1]
                self.label.setText(str(self.setValueString))

            if (id_button=="OK"):
                #try:
                self.instanciaModbus.writeValuesPID(float(self.setValueString),self.variablePIDSeleccionada,self.horno_manta_seleccionada)
                #except:
                    #print("error escritura modbus 2")
                hornoSeleccionado = self.horno_manta_seleccionada
                self.MainWindow.close()
                self.pidWindow.setEnabled(True)
                
        # Si el usuario selecciona configuracion de alarmas
        elif(self.sectionVector[2] == True):
            if id_button != "OK" and id_button != "AC" and id_button != "<":
                self.setValueString = self.setValueString + id_button
                self.label.setText(str(self.setValueString))

            if(id_button == "AC"):
                self.setValueString = ""
                self.label.setText(str(self.setValueString))
                
            if (id_button == "<"):
                self.setValueString = self.setValueString[0:len(self.setValueString)-1]
                self.label.setText(str(self.setValueString))

            if (id_button=="OK"):
                self.MainWindow.close()
                self.alarmWindow.setEnabled(True)
                self.instanciaBD_alarmas.update_alarma(self.setValueString, self.alarmaSeleccionada)
                self.buttonSelected.setText(self.setValueString)

        # Si el usuario selecciona configuracion de resetas
        elif(self.sectionVector[3] == True):
            if id_button != "OK" and id_button != "AC" and id_button != "<":
                self.setValueString = self.setValueString + id_button
                self.label.setText(str(self.setValueString))

            if(id_button == "AC"):
                self.setValueString = ""
                self.label.setText(str(self.setValueString))
                
            if (id_button == "<"):
                self.setValueString = self.setValueString[0:len(self.setValueString)-1]
                self.label.setText(str(self.setValueString))

            if (id_button=="OK"):
                self.MainWindow.close()
                self.alarmWindow.setEnabled(True)
                #self.instanciaBD_alarmas.update_alarma(self.setValueString, self.alarmaSeleccionada)
                self.buttonSelected.setText(self.setValueString)

        # Si el usuario selecciona configuracion de escalado
        elif(self.sectionVector[1] == True):
            if id_button != "OK" and id_button != "AC" and id_button != "<":
                self.setValueString = self.setValueString + id_button
                self.label.setText(str(self.setValueString))

            if(id_button == "AC"):
                self.setValueString = ""
                self.label.setText(str(self.setValueString))
                
            if (id_button == "<"):
                self.setValueString = self.setValueString[0:len(self.setValueString)-1]
                self.label.setText(str(self.setValueString))

            if (id_button=="OK"):
                self.MainWindow.close()
                self.escaladoMainWindow.setEnabled(True)
                #self.instanciaBD_alarmas.update_alarma(self.setValueString, self.alarmaSeleccionada)

    def closeEvent_PID_reactor(self, event):
        self.MainWindow.close()
        self.pidWindow.setEnabled(True)

    def closeEvent_AlarmWindow(self, event):
        self.MainWindow.close()
        self.alarmWindow.setEnabled(True)

    def closeEvent_recetas(self, event):
        self.MainWindow.close()
        self.resetasMainWindow.setEnabled(True) 

    def closeEvent_escalado(self, event):
        self.MainWindow.close()
        self.escaladoMainWindow.setEnabled(True)      

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet('QMainWindow{background-color: #333333; border:2px solid black;}')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
