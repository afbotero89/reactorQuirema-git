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
    def setupUi(self, MainWindow1, sectionVector, socket, socketBomba):
        self.s = socket
        self.sBomba = socketBomba

        self.MainWindow = MainWindow1
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(800, 480)
        self.sectionVector = sectionVector

        self.centralWidget = QtWidgets.QWidget(MainWindow1)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(5, 160, 190, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButtonHorno2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonHorno2.setGeometry(QtCore.QRect(205, 160, 190, 81))
        self.pushButtonHorno2.setObjectName("pushButtonHorno2")
        self.pushButtonHorno3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonHorno3.setGeometry(QtCore.QRect(405, 160, 190, 81))
        self.pushButtonHorno3.setObjectName("pushButtonHorno3")
        self.pushButtonHorno4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonHorno4.setGeometry(QtCore.QRect(605, 160, 190, 81))
        self.pushButtonHorno4.setObjectName("pushButtonHorno4")
        self.pushButtonManta1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonManta1.setGeometry(QtCore.QRect(150, 270, 121, 51))
        self.pushButtonManta1.setObjectName("pushButtonManta1")
        self.pushButtonManta2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonManta2.setGeometry(QtCore.QRect(350, 270, 121, 51))
        self.pushButtonManta2.setObjectName("pushButtonManta2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(280, 100, 261, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButtonManta3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonManta3.setGeometry(QtCore.QRect(560, 270, 121, 51))
        self.pushButtonManta3.setObjectName("pushButtonManta3")
        self.pushButtonManta4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonManta4.setGeometry(QtCore.QRect(240, 340,  121, 51))
        self.pushButtonManta4.setObjectName("pushButtonManta4")
        self.pushButtonManta5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonManta5.setGeometry(QtCore.QRect(440, 340, 121, 51))
        self.pushButtonManta5.setObjectName("pushButtonManta5")

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
        self.pushButtonHorno2.setText(_translate("MainWindow1", "Horno 2"))
        self.pushButtonHorno3.setText(_translate("MainWindow1", "Horno 3"))
        self.pushButtonHorno4.setText(_translate("MainWindow1", "Horno 4"))
        self.pushButtonManta1.setText(_translate("MainWindow1", "Manta 1"))
        self.pushButtonManta2.setText(_translate("MainWindow1", "Manta 2"))
        self.label.setText(_translate("MainWindow1", "Modificar parametros PID"))
        self.pushButtonManta3.setText(_translate("MainWindow1", "Manta 3"))
        self.pushButtonManta4.setText(_translate("MainWindow1", "Manta 4"))
        self.pushButtonManta5.setText(_translate("MainWindow1", "Manta 5"))
        self.addAdditionalAttributes()


        self.label.setStyleSheet("color: white; font-size: 18pt;")
        self.pushButton.clicked.connect(lambda: self.setPID_parameters('horno1'))
        self.pushButtonHorno2.clicked.connect(lambda: self.setPID_parameters('horno2'))
        self.pushButtonHorno3.clicked.connect(lambda: self.setPID_parameters('horno3'))
        self.pushButtonHorno4.clicked.connect(lambda: self.setPID_parameters('horno4'))
        self.pushButtonManta1.clicked.connect(lambda: self.setPID_parameters('manta1'))
        self.pushButtonManta2.clicked.connect(lambda: self.setPID_parameters('manta2'))
        self.pushButtonManta3.clicked.connect(lambda: self.setPID_parameters('manta3'))
        self.pushButtonManta4.clicked.connect(lambda: self.setPID_parameters('manta4'))
        self.pushButtonManta5.clicked.connect(lambda: self.setPID_parameters('manta5'))
        self.pushButton0.clicked.connect(self.home)

    def addAdditionalAttributes(self):
        buttonStyle = "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255)); border-style: outset; border-width: 1px; border-radius: 10px; border-color: white; padding: 6px; font-size: 25pt;"
        self.pushButton.setStyleSheet(buttonStyle)
        self.pushButtonHorno2.setStyleSheet(buttonStyle)
        self.pushButtonHorno3.setStyleSheet(buttonStyle)
        self.pushButtonHorno4.setStyleSheet(buttonStyle)
        self.pushButtonManta1.setStyleSheet(buttonStyle)
        self.pushButtonManta2.setStyleSheet(buttonStyle)
        self.pushButtonManta3.setStyleSheet(buttonStyle)
        self.pushButtonManta4.setStyleSheet(buttonStyle)
        self.pushButtonManta5.setStyleSheet(buttonStyle)

    def setPID_parameters(self, horno_manta_seleccionada):
        self.pidInterface = setPID_parameters.Ui_MainWindow()
        self.pidInterface.setupUi(self.MainWindow, horno_manta_seleccionada, self.sectionVector, self.s, self.sBomba)

    def home(self):
        self.home = Home.Ui_MainWindow()
        self.home.setupUi(self.MainWindow, self.s, self.sBomba)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet('QMainWindow{background-color: #BDBDBD; border:2px solid black;}')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_PIDParameters()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
