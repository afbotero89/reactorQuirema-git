# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow1.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import setPID_parameters
import Home


class Ui_MainWindow_PIDParameters(object):
    def setupUi(self, MainWindow1, sectionVector):
        self.MainWindow = MainWindow1
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(800, 480)
        self.sectionVector = sectionVector

        self.centralWidget = QtWidgets.QWidget(MainWindow1)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(5, 160, 190, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(205, 160, 190, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(405, 160, 190, 81))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(605, 160, 190, 81))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 270, 121, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_6.setGeometry(QtCore.QRect(350, 270, 121, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(280, 100, 261, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_7.setGeometry(QtCore.QRect(560, 270, 121, 51))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_8.setGeometry(QtCore.QRect(240, 340,  121, 51))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_9.setGeometry(QtCore.QRect(440, 340, 121, 51))
        self.pushButton_9.setObjectName("pushButton_9")

        self.label0 = QtWidgets.QLabel(self.centralWidget)
        self.label0.setGeometry(QtCore.QRect(0, 0, 800, 71))
        self.label0.setText("               Control PLC")
        self.label0.setStyleSheet("background-color: black; color: #0080FF; font-size: 22pt;")
        self.label0.setScaledContents(True)


        self.pushButton0 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton0.setGeometry(QtCore.QRect(0, 0, 71, 71))
        self.pushButton0.setStyleSheet("background-color: #222222; color:white; font-size: 22pt;")
        self.pushButton0.setIcon(QtGui.QIcon('../images/home.png'))
        self.pushButton0.setIconSize(QtCore.QSize(31,31))

        self.label1 = QtWidgets.QLabel(self.centralWidget)
        self.label1.setGeometry(QtCore.QRect(644, 0, 120, 71))
        self.label1.setText("")
        self.label1.setPixmap(QtGui.QPixmap("../images/quirema.png"))
        self.label1.setScaledContents(True)
        self.label1.setObjectName("label")

        MainWindow1.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow1)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 464, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow1.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow1)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow1.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow1)
        self.statusBar.setObjectName("statusBar")
        MainWindow1.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("Parametros PID", "Parametros PID"))
        self.pushButton.setText(_translate("MainWindow1", "Horno 1"))
        self.pushButton_2.setText(_translate("MainWindow1", "Horno 2"))
        self.pushButton_3.setText(_translate("MainWindow1", "Horno 3"))
        self.pushButton_4.setText(_translate("MainWindow1", "Horno 4"))
        self.pushButton_5.setText(_translate("MainWindow1", "Manta 1"))
        self.pushButton_6.setText(_translate("MainWindow1", "Manta 2"))
        self.label.setText(_translate("MainWindow1", "Modificar parametros PID"))
        self.pushButton_7.setText(_translate("MainWindow1", "Manta 3"))
        self.pushButton_8.setText(_translate("MainWindow1", "Manta 4"))
        self.pushButton_9.setText(_translate("MainWindow1", "Manta 5"))
        self.addAdditionalAttributes()


        self.label.setStyleSheet("color: #0080FF; font-size: 18pt;")
        self.pushButton.clicked.connect(lambda: self.setPID_parameters('horno1'))
        self.pushButton_2.clicked.connect(lambda: self.setPID_parameters('horno2'))
        self.pushButton_3.clicked.connect(lambda: self.setPID_parameters('horno3'))
        self.pushButton_4.clicked.connect(lambda: self.setPID_parameters('horno4'))
        self.pushButton_5.clicked.connect(lambda: self.setPID_parameters('manta1'))
        self.pushButton_6.clicked.connect(lambda: self.setPID_parameters('manta2'))
        self.pushButton_7.clicked.connect(lambda: self.setPID_parameters('manta3'))
        self.pushButton_8.clicked.connect(lambda: self.setPID_parameters('manta4'))
        self.pushButton_9.clicked.connect(lambda: self.setPID_parameters('manta5'))
        self.pushButton0.clicked.connect(self.home)

    def addAdditionalAttributes(self):
        buttonStyle = "background-color: #EFEFF4; border-style: outset; border-width: 2px; border-radius: 10px; border-color: #0080FF; padding: 6px; font-size: 25pt;"
        self.pushButton.setStyleSheet(buttonStyle)
        self.pushButton_2.setStyleSheet(buttonStyle)
        self.pushButton_3.setStyleSheet(buttonStyle)
        self.pushButton_4.setStyleSheet(buttonStyle)
        self.pushButton_5.setStyleSheet(buttonStyle)
        self.pushButton_6.setStyleSheet(buttonStyle)
        self.pushButton_7.setStyleSheet(buttonStyle)
        self.pushButton_8.setStyleSheet(buttonStyle)
        self.pushButton_9.setStyleSheet(buttonStyle)

    def setPID_parameters(self, horno_manta_seleccionada):
        self.pidInterface = setPID_parameters.Ui_MainWindow()
        self.pidInterface.setupUi(self.MainWindow, horno_manta_seleccionada, self.sectionVector)

    def home(self):
        self.home = Home.Ui_MainWindow()
        self.home.setupUi(self.MainWindow)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet('QMainWindow{background-color: #BDBDBD; border:2px solid black;}')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_PIDParameters()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
