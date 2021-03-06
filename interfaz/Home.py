# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint
import PID_parameters 
import alarmsMainWindow
import reactorWindow2
import recetas1
import escalado
import serial
import psutil, os

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow, socket):
        self.s = socket
        self.MainWindow = MainWindow
        p = psutil.Process(os.getpid())
        files = p.open_files()
        #files.clear()
        print(p)
        #MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));")
        # Indica en que seccion se encuentra el usuario: PID, Escalado, Alarmas, Recetas, Graficos, Reactor
        self.sectionVector = [False,False,False,False,False,False]

        MainWindow.setObjectName("Reactor Quirema")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 480)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        MainWindow.setMaximumSize(QtCore.QSize(800, 480))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        buttonStyle = "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255)); border-style: outset; border-width: 1px; border-radius: 20px; border-color: #AFAFAF; padding: 6px; font-size: 25pt;"

        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 100, 271, 80))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(buttonStyle)

        #self.pushButtonIcon = QtWidgets.QPushButton(self.centralWidget)
        #self.pushButtonIcon.setGeometry(QtCore.QRect(130, 105, 100, 70))
        #self.pushButtonIcon.setObjectName("pushButton")

        #rMyIcon = QtGui.QPixmap("../images/quirema.png")
        #self.pushButtonIcon.setIconSize(QtCore.QSize(70,70))
        #self.pushButtonIcon.setIcon(QtGui.QIcon(rMyIcon))

        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 100, 271, 80))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet(buttonStyle)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 320, 271, 80))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet(buttonStyle)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(410, 320, 271, 80))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet(buttonStyle)

        self.pushButton_6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_6.setGeometry(QtCore.QRect(260, 210, 271, 80))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet(buttonStyle)

        self.label0 = QtWidgets.QLabel(self.centralWidget)
        self.label0.setGeometry(QtCore.QRect(0, 0, 800, 71))
        self.label0.setText(" Control PLC")
        self.label0.setStyleSheet("background-color: black; color:#0080FF; font-size: 22pt;")
        self.label0.setScaledContents(True)

        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(644, 0, 120, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../images/quirema.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 464, 21))
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
        MainWindow.setWindowTitle(_translate("Control PLC", "Control PLC"))
        self.pushButton.setText(_translate("MainWindow", "PID"))
        self.pushButton_2.setText(_translate("MainWindow", "Escalado"))
        self.pushButton_3.setText(_translate("MainWindow", "Alarmas"))
        self.pushButton_4.setText(_translate("MainWindow", "Recetas"))
        self.pushButton_6.setText(_translate("MainWindow", "Reactor"))

        self.pushButton.clicked.connect(self.PIDInterface)
        self.pushButton_2.clicked.connect(self.escaladoMainWindow)
        self.pushButton_3.clicked.connect(self.alarms)
        self.pushButton_4.clicked.connect(self.recetas)
        self.pushButton_6.clicked.connect(self.rectorMainWindow)
        
    def PIDInterface(self):
        # Indica en que seccion se encuentra el usuario: PID, Escalado, Alarmas, Recetas, Graficos, Reactor
        self.sectionVector = [True,False,False,False,False,False]
        self.pidInterface = PID_parameters.Ui_MainWindow_PIDParameters()
        self.pidInterface.setupUi(self.MainWindow, self.sectionVector, self.s)

    def alarms(self):
        self.sectionVector = [False,False,True,False,False,False]
        self.alarms = alarmsMainWindow.Ui_MainWindow()
        self.alarms.setupUi(self.MainWindow, self.sectionVector, self.s)

    def recetas(self):
        self.sectionVector = [False,False,False,True,False,False]
        self.recetas = recetas1.Ui_MainWindow()
        self.recetas.setupUi(self.MainWindow, self.sectionVector, self.s)

    def rectorMainWindow(self):
        # Indica en que seccion se encuentra el usuario: PID, Escalado, Alarmas, Recetas, Graficos, Reactor
        self.sectionVector = [False,False,False,False,False,True]
        self.reactor = reactorWindow2.Ui_MainWindow()
        self.reactor.setupUi(self.MainWindow, self.sectionVector, self.s)

    def escaladoMainWindow(self):
        # Indica en que seccion se encuentra el usuario: PID, Escalado, Alarmas, Recetas, Graficos, Reactor
        self.sectionVector = [False,True,False,False,False,False]
        self.escalado = escalado.Ui_MainWindow()
        self.escalado.setupUi(self.MainWindow, self.sectionVector, self.s)       
       
        
if __name__ == "__main__":
    import sys

    socket = serial.Serial()
    #socket.port = '/dev/tty.SLAB_USBtoUART'
    socket.port = '/dev/ttyUSB0'
    socket.baudrate = 9600
    socket.bytesize = 7
    socket.parity = serial.PARITY_EVEN
    socket.stopbits = 1
    socket.timeout = 0.1

    #p = psutil.Process(os.getpid())
    #files = p.open_files()
    #files.clear()
    
    #if socket.is_open == False:
    try:
        socket.open()
    except:
        pass    
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet('QMainWindow{background-color: qlineargradient(spread:reflect, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(0, 64, 128, 255), stop:1 rgba(0, 0, 0, 255)); border:2px solid black;}')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, socket)
    qPoint = QPoint(0,-5)
    MainWindow.move(qPoint)
    MainWindow.show()
    sys.exit(app.exec_())
