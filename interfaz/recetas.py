# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_copy_copy2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Home

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
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
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 71))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(670, 0, 131, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../images/quirema.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton_Receta1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Receta1.setGeometry(QtCore.QRect(60, 70, 78, 31))
        self.pushButton_Receta1.setObjectName("pushButton_Receta1")
        self.pushButton_Receta2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Receta2.setGeometry(QtCore.QRect(130, 70, 78, 31))
        self.pushButton_Receta2.setObjectName("pushButton_Receta2")
        self.pushButton_Receta3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Receta3.setGeometry(QtCore.QRect(200, 70, 78, 31))
        self.pushButton_Receta3.setObjectName("pushButton_Receta3")
        self.pushButton_Receta4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Receta4.setGeometry(QtCore.QRect(270, 70, 78, 31))
        self.pushButton_Receta4.setObjectName("pushButton_Receta4")
        self.pushButton_Receta5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Receta5.setGeometry(QtCore.QRect(340, 70, 78, 31))
        self.pushButton_Receta5.setObjectName("pushButton_Receta5")
        self.pushButton_Receta6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Receta6.setGeometry(QtCore.QRect(410, 70, 78, 31))
        self.pushButton_Receta6.setObjectName("pushButton_Receta6")
        self.pushButton_Receta7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Receta7.setGeometry(QtCore.QRect(480, 70, 78, 31))
        self.pushButton_Receta7.setObjectName("pushButton_Receta7")
        self.pushButton_Receta8 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Receta8.setGeometry(QtCore.QRect(550, 70, 78, 31))
        self.pushButton_Receta8.setObjectName("pushButton_Receta8")
        self.pushButton_Receta9 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Receta9.setGeometry(QtCore.QRect(620, 70, 78, 31))
        self.pushButton_Receta9.setObjectName("pushButton_Receta9")
        self.pushButton_Receta10 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Receta10.setGeometry(QtCore.QRect(690, 70, 91, 32))
        self.pushButton_Receta10.setObjectName("pushButton_Receta10")
        self.label_Horno1 = QtWidgets.QLabel(self.centralWidget)
        self.label_Horno1.setGeometry(QtCore.QRect(10, 110, 51, 16))
        self.label_Horno1.setStyleSheet("color: white")
        self.label_Horno1.setObjectName("label_Horno1")
        self.label_Horno2 = QtWidgets.QLabel(self.centralWidget)
        self.label_Horno2.setGeometry(QtCore.QRect(10, 140, 51, 16))
        self.label_Horno2.setStyleSheet("color: white")
        self.label_Horno2.setObjectName("label_Horno2")
        self.label_Horno3 = QtWidgets.QLabel(self.centralWidget)
        self.label_Horno3.setGeometry(QtCore.QRect(10, 170, 51, 16))
        self.label_Horno3.setStyleSheet("color: white")
        self.label_Horno3.setObjectName("label_Horno3")
        self.label_Horno4 = QtWidgets.QLabel(self.centralWidget)
        self.label_Horno4.setGeometry(QtCore.QRect(10, 200, 51, 16))
        self.label_Horno4.setStyleSheet("color: white")
        self.label_Horno4.setObjectName("label_Horno4")
        self.pushButton_H1R1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H1R1.setGeometry(QtCore.QRect(60, 100, 78, 31))
        self.pushButton_H1R1.setObjectName("pushButton_H1R1")
        self.pushButton_H2R2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H2R2.setGeometry(QtCore.QRect(60, 130, 78, 31))
        self.pushButton_H2R2.setObjectName("pushButton_H2R2")
        self.pushButton_H3R3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H3R3.setGeometry(QtCore.QRect(60, 160, 78, 31))
        self.pushButton_H3R3.setObjectName("pushButton_H3R3")
        self.pushButton_H4R1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H4R1.setGeometry(QtCore.QRect(60, 190, 78, 31))
        self.pushButton_H4R1.setObjectName("pushButton_H4R1")
        self.pushButton_H4R2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H4R2.setGeometry(QtCore.QRect(130, 190, 78, 31))
        self.pushButton_H4R2.setObjectName("pushButton_H4R2")
        self.pushButton_H1R2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H1R2.setGeometry(QtCore.QRect(130, 100, 78, 31))
        self.pushButton_H1R2.setObjectName("pushButton_H1R2")
        self.pushButton_H3R2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H3R2.setGeometry(QtCore.QRect(130, 160, 78, 31))
        self.pushButton_H3R2.setObjectName("pushButton_H3R2")
        self.pushButton_H2R2_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H2R2_2.setGeometry(QtCore.QRect(130, 130, 78, 31))
        self.pushButton_H2R2_2.setObjectName("pushButton_H2R2_2")
        self.pushButton_H4R3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H4R3.setGeometry(QtCore.QRect(200, 190, 78, 31))
        self.pushButton_H4R3.setObjectName("pushButton_H4R3")
        self.pushButton_H1R3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H1R3.setGeometry(QtCore.QRect(200, 100, 78, 31))
        self.pushButton_H1R3.setObjectName("pushButton_H1R3")
        self.pushButton_H3R3_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H3R3_2.setGeometry(QtCore.QRect(200, 160, 78, 31))
        self.pushButton_H3R3_2.setObjectName("pushButton_H3R3_2")
        self.pushButton_H2R3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H2R3.setGeometry(QtCore.QRect(200, 130, 78, 31))
        self.pushButton_H2R3.setObjectName("pushButton_H2R3")
        self.pushButton_H4R4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H4R4.setGeometry(QtCore.QRect(270, 190, 78, 31))
        self.pushButton_H4R4.setObjectName("pushButton_H4R4")
        self.pushButton_H1R4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H1R4.setGeometry(QtCore.QRect(270, 100, 78, 31))
        self.pushButton_H1R4.setObjectName("pushButton_H1R4")
        self.pushButton_H3R4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H3R4.setGeometry(QtCore.QRect(270, 160, 78, 31))
        self.pushButton_H3R4.setObjectName("pushButton_H3R4")
        self.pushButton_H2R4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H2R4.setGeometry(QtCore.QRect(270, 130, 78, 31))
        self.pushButton_H2R4.setObjectName("pushButton_H2R4")
        self.pushButton_H4R5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H4R5.setGeometry(QtCore.QRect(340, 190, 78, 31))
        self.pushButton_H4R5.setObjectName("pushButton_H4R5")
        self.pushButton_H1R5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H1R5.setGeometry(QtCore.QRect(340, 100, 78, 31))
        self.pushButton_H1R5.setObjectName("pushButton_H1R5")
        self.pushButton_H3R5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H3R5.setGeometry(QtCore.QRect(340, 160, 78, 31))
        self.pushButton_H3R5.setObjectName("pushButton_H3R5")
        self.pushButton_H2R5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H2R5.setGeometry(QtCore.QRect(340, 130, 78, 31))
        self.pushButton_H2R5.setObjectName("pushButton_H2R5")
        self.pushButton_H4R6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H4R6.setGeometry(QtCore.QRect(410, 190, 78, 31))
        self.pushButton_H4R6.setObjectName("pushButton_H4R6")
        self.pushButton_H1R6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H1R6.setGeometry(QtCore.QRect(410, 100, 78, 31))
        self.pushButton_H1R6.setObjectName("pushButton_H1R6")
        self.pushButton_H3R6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H3R6.setGeometry(QtCore.QRect(410, 160, 78, 31))
        self.pushButton_H3R6.setObjectName("pushButton_H3R6")
        self.pushButton_H2R6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H2R6.setGeometry(QtCore.QRect(410, 130, 78, 31))
        self.pushButton_H2R6.setObjectName("pushButton_H2R6")
        self.pushButton_H4R7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H4R7.setGeometry(QtCore.QRect(480, 190, 78, 31))
        self.pushButton_H4R7.setObjectName("pushButton_H4R7")
        self.pushButton_H1R7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H1R7.setGeometry(QtCore.QRect(480, 100, 78, 31))
        self.pushButton_H1R7.setObjectName("pushButton_H1R7")
        self.pushButton_H3R7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H3R7.setGeometry(QtCore.QRect(480, 160, 78, 31))
        self.pushButton_H3R7.setObjectName("pushButton_H3R7")
        self.pushButton_H2R7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H2R7.setGeometry(QtCore.QRect(480, 130, 78, 31))
        self.pushButton_H2R7.setObjectName("pushButton_H2R7")
        self.pushButton_H4R8 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H4R8.setGeometry(QtCore.QRect(550, 190, 78, 31))
        self.pushButton_H4R8.setObjectName("pushButton_H4R8")
        self.pushButton_H1R8 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H1R8.setGeometry(QtCore.QRect(550, 100, 78, 31))
        self.pushButton_H1R8.setObjectName("pushButton_H1R8")
        self.pushButton_H3R8 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H3R8.setGeometry(QtCore.QRect(550, 160, 78, 31))
        self.pushButton_H3R8.setObjectName("pushButton_H3R8")
        self.pushButton_H2R8 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H2R8.setGeometry(QtCore.QRect(550, 130, 78, 31))
        self.pushButton_H2R8.setObjectName("pushButton_H2R8")
        self.pushButton_H4R9 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H4R9.setGeometry(QtCore.QRect(620, 190, 78, 31))
        self.pushButton_H4R9.setObjectName("pushButton_H4R9")
        self.pushButton_H1R9 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H1R9.setGeometry(QtCore.QRect(620, 100, 78, 31))
        self.pushButton_H1R9.setObjectName("pushButton_H1R9")
        self.pushButton_H3R9 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H3R9.setGeometry(QtCore.QRect(620, 160, 78, 31))
        self.pushButton_H3R9.setObjectName("pushButton_H3R9")
        self.pushButton_H2R9 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H2R9.setGeometry(QtCore.QRect(620, 130, 78, 31))
        self.pushButton_H2R9.setObjectName("pushButton_H2R9")
        self.pushButton_H4R10 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H4R10.setGeometry(QtCore.QRect(690, 190, 78, 31))
        self.pushButton_H4R10.setObjectName("pushButton_H4R10")
        self.pushButton_H1R10 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H1R10.setGeometry(QtCore.QRect(690, 100, 78, 31))
        self.pushButton_H1R10.setObjectName("pushButton_H1R10")
        self.pushButton_H3R10 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H3R10.setGeometry(QtCore.QRect(690, 160, 78, 31))
        self.pushButton_H3R10.setObjectName("pushButton_H3R10")
        self.pushButton_H2R10 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_H2R10.setGeometry(QtCore.QRect(690, 130, 78, 31))
        self.pushButton_H2R10.setObjectName("pushButton_H2R10")
        self.pushButton_TMantasR1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_TMantasR1.setGeometry(QtCore.QRect(60, 220, 78, 31))
        self.pushButton_TMantasR1.setObjectName("pushButton_TMantasR1")
        self.pushButton_TempMantasR8 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_TempMantasR8.setGeometry(QtCore.QRect(550, 220, 78, 31))
        self.pushButton_TempMantasR8.setObjectName("pushButton_TempMantasR8")
        self.pushButton_TempMantasR2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_TempMantasR2.setGeometry(QtCore.QRect(130, 220, 78, 31))
        self.pushButton_TempMantasR2.setObjectName("pushButton_TempMantasR2")
        self.pushButton_TempMantasR3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_TempMantasR3.setGeometry(QtCore.QRect(200, 220, 78, 31))
        self.pushButton_TempMantasR3.setObjectName("pushButton_TempMantasR3")
        self.pushButton_TempMantasR5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_TempMantasR5.setGeometry(QtCore.QRect(340, 220, 78, 31))
        self.pushButton_TempMantasR5.setObjectName("pushButton_TempMantasR5")
        self.pushButton_TempMantasR7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_TempMantasR7.setGeometry(QtCore.QRect(480, 220, 78, 31))
        self.pushButton_TempMantasR7.setObjectName("pushButton_TempMantasR7")
        self.pushButton_TempMantasR9 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_TempMantasR9.setGeometry(QtCore.QRect(620, 220, 78, 31))
        self.pushButton_TempMantasR9.setObjectName("pushButton_TempMantasR9")
        self.label_TempMantas = QtWidgets.QLabel(self.centralWidget)
        self.label_TempMantas.setGeometry(QtCore.QRect(0, 230, 61, 20))
        self.label_TempMantas.setStyleSheet("color: white")
        self.label_TempMantas.setObjectName("label_TempMantas")
        self.pushButton_TempMantasR4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_TempMantasR4.setGeometry(QtCore.QRect(270, 220, 78, 31))
        self.pushButton_TempMantasR4.setObjectName("pushButton_TempMantasR4")
        self.pushButton_TempMantasR10 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_TempMantasR10.setGeometry(QtCore.QRect(690, 220, 78, 31))
        self.pushButton_TempMantasR10.setObjectName("pushButton_TempMantasR10")
        self.pushButton_TempMantasR6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_TempMantasR6.setGeometry(QtCore.QRect(410, 220, 78, 31))
        self.pushButton_TempMantasR6.setObjectName("pushButton_TempMantasR6")
        self.pushButton_TiempoR10 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_TiempoR10.setGeometry(QtCore.QRect(690, 250, 78, 31))
        self.pushButton_TiempoR10.setObjectName("pushButton_TiempoR10")
        self.pushButton_TiempoR8 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_TiempoR8.setGeometry(QtCore.QRect(550, 250, 78, 31))
        self.pushButton_TiempoR8.setObjectName("pushButton_TiempoR8")
        self.pushButton_TiempoR3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_TiempoR3.setGeometry(QtCore.QRect(200, 250, 78, 31))
        self.pushButton_TiempoR3.setObjectName("pushButton_TiempoR3")
        self.pushButton_TiempoR1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_TiempoR1.setGeometry(QtCore.QRect(60, 250, 78, 31))
        self.pushButton_TiempoR1.setObjectName("pushButton_TiempoR1")
        self.pushButton_TiempoR5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_TiempoR5.setGeometry(QtCore.QRect(340, 250, 78, 31))
        self.pushButton_TiempoR5.setObjectName("pushButton_TiempoR5")
        self.pushButton_TiempoR9 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_TiempoR9.setGeometry(QtCore.QRect(620, 250, 78, 31))
        self.pushButton_TiempoR9.setObjectName("pushButton_TiempoR9")
        self.label_Tiempo = QtWidgets.QLabel(self.centralWidget)
        self.label_Tiempo.setGeometry(QtCore.QRect(10, 260, 51, 20))
        self.label_Tiempo.setStyleSheet("color: white")
        self.label_Tiempo.setObjectName("label_Tiempo")
        self.pushButton_TiempoR4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_TiempoR4.setGeometry(QtCore.QRect(270, 250, 78, 31))
        self.pushButton_TiempoR4.setObjectName("pushButton_TiempoR4")
        self.pushButton_TiempoR7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_TiempoR7.setGeometry(QtCore.QRect(480, 250, 78, 31))
        self.pushButton_TiempoR7.setObjectName("pushButton_TiempoR7")
        self.pushButton_TiempoR6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_TiempoR6.setGeometry(QtCore.QRect(410, 250, 78, 31))
        self.pushButton_TiempoR6.setObjectName("pushButton_TiempoR6")
        self.pushButton_TiempoR2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_TiempoR2.setGeometry(QtCore.QRect(130, 250, 78, 31))
        self.pushButton_TiempoR2.setObjectName("pushButton_TiempoR2")
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

        self.pushButton0 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton0.setGeometry(QtCore.QRect(0, 0, 71, 71))
        self.pushButton0.setStyleSheet("background-color: #222222; color:white; font-size: 22pt;")
        self.pushButton0.setIcon(QtGui.QIcon('../images/home.png'))
        self.pushButton0.setIconSize(QtCore.QSize(31,31))

        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quirema"))
        self.label.setText(_translate("MainWindow", "               Quirema                                      Recetas"))
        self.pushButton_Receta1.setText(_translate("MainWindow", "Receta 1"))
        self.pushButton_Receta2.setText(_translate("MainWindow", "Receta 2"))
        self.pushButton_Receta3.setText(_translate("MainWindow", "Receta 3"))
        self.pushButton_Receta4.setText(_translate("MainWindow", "Receta 4"))
        self.pushButton_Receta5.setText(_translate("MainWindow", "Receta 5"))
        self.pushButton_Receta6.setText(_translate("MainWindow", "Receta 6"))
        self.pushButton_Receta7.setText(_translate("MainWindow", "Receta 7"))
        self.pushButton_Receta8.setText(_translate("MainWindow", "Receta 8"))
        self.pushButton_Receta9.setText(_translate("MainWindow", "Receta 9"))
        self.pushButton_Receta10.setText(_translate("MainWindow", "Receta 10"))
        self.label_Horno1.setText(_translate("MainWindow", "Horno 1"))
        self.label_Horno2.setText(_translate("MainWindow", "Horno 2"))
        self.label_Horno3.setText(_translate("MainWindow", "Horno 3"))
        self.label_Horno4.setText(_translate("MainWindow", "Horno 4"))
        self.pushButton_H1R1.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H2R2.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H3R3.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H4R1.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H4R2.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H1R2.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H3R2.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H2R2_2.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H4R3.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H1R3.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H3R3_2.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H2R3.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H4R4.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H1R4.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H3R4.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H2R4.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H4R5.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H1R5.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H3R5.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H2R5.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H4R6.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H1R6.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H3R6.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H2R6.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H4R7.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H1R7.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H3R7.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H2R7.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H4R8.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H1R8.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H3R8.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H2R8.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H4R9.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H1R9.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H3R9.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H2R9.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H4R10.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H1R10.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H3R10.setText(_translate("MainWindow", "0.0"))
        self.pushButton_H2R10.setText(_translate("MainWindow", "0.0"))
        self.pushButton_TMantasR1.setText(_translate("MainWindow", "0.0"))
        self.pushButton_TempMantasR8.setText(_translate("MainWindow", "0.0"))
        self.pushButton_TempMantasR2.setText(_translate("MainWindow", "0.0"))
        self.pushButton_TempMantasR3.setText(_translate("MainWindow", "0.0"))
        self.pushButton_TempMantasR5.setText(_translate("MainWindow", "0.0"))
        self.pushButton_TempMantasR7.setText(_translate("MainWindow", "0.0"))
        self.pushButton_TempMantasR9.setText(_translate("MainWindow", "0.0"))
        self.label_TempMantas.setText(_translate("MainWindow", "T. Mantas"))
        self.pushButton_TempMantasR4.setText(_translate("MainWindow", "0.0"))
        self.pushButton_TempMantasR10.setText(_translate("MainWindow", "0.0"))
        self.pushButton_TempMantasR6.setText(_translate("MainWindow", "0.0"))
        self.pushButton_TiempoR10.setText(_translate("MainWindow", "0.0"))
        self.pushButton_TiempoR8.setText(_translate("MainWindow", "0.0"))
        self.pushButton_TiempoR3.setText(_translate("MainWindow", "0.0"))
        self.pushButton_TiempoR1.setText(_translate("MainWindow", "0.0"))
        self.pushButton_TiempoR5.setText(_translate("MainWindow", "0.0"))
        self.pushButton_TiempoR9.setText(_translate("MainWindow", "0.0"))
        self.label_Tiempo.setText(_translate("MainWindow", "Tiempo"))
        self.pushButton_TiempoR4.setText(_translate("MainWindow", "0.0"))
        self.pushButton_TiempoR7.setText(_translate("MainWindow", "0.0"))
        self.pushButton_TiempoR6.setText(_translate("MainWindow", "0.0"))
        self.pushButton_TiempoR2.setText(_translate("MainWindow", "0.0"))
        self.pushButton0.clicked.connect(self.home)

    def home(self):
        self.home = Home.Ui_MainWindow()
        self.home.setupUi(self.MainWindow)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet('QMainWindow{background-color:qlineargradient(spread:reflect, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(0, 64, 128, 255), stop:1 rgba(0, 0, 0, 255)); border:2px solid black;}')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
