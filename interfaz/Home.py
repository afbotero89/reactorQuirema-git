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
import sqlite3

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow, socketPLC, socketBomba):
        
        self.s = socketPLC
        self.sBomba = socketBomba

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

        self.pushButtonPID = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonPID.setGeometry(QtCore.QRect(100, 100, 271, 80))
        self.pushButtonPID.setObjectName("pushButtonPID")
        self.pushButtonPID.setStyleSheet(buttonStyle)

        self.pushButtonEscalado = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonEscalado.setGeometry(QtCore.QRect(410, 185, 271, 80))
        self.pushButtonEscalado.setObjectName("pushButtonEscalado")
        self.pushButtonEscalado.setStyleSheet(buttonStyle)

        self.pushButtonAlarmas = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonAlarmas.setGeometry(QtCore.QRect(100, 320, 271, 80))
        self.pushButtonAlarmas.setObjectName("pushButtonAlarmas")
        self.pushButtonAlarmas.setStyleSheet(buttonStyle)
        self.pushButtonAlarmas.setEnabled(False)
        self.pushButtonAlarmas.setVisible(False)

        self.pushButtonRecetas = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonRecetas.setGeometry(QtCore.QRect(410, 320, 271, 80))
        self.pushButtonRecetas.setObjectName("pushButtonRecetas")
        self.pushButtonRecetas.setStyleSheet(buttonStyle)

        self.pushButtonReactor = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonReactor.setGeometry(QtCore.QRect(100, 240, 271, 80))
        self.pushButtonReactor.setObjectName("pushButtonReactor")
        self.pushButtonReactor.setStyleSheet(buttonStyle)

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
        self.pushButtonPID.setText(_translate("MainWindow", "PID"))
        self.pushButtonEscalado.setText(_translate("MainWindow", "Escalado"))
        self.pushButtonAlarmas.setText(_translate("MainWindow", "Alarmas"))
        self.pushButtonRecetas.setText(_translate("MainWindow", "Recetas"))
        self.pushButtonReactor.setText(_translate("MainWindow", "Reactor"))

        self.pushButtonPID.clicked.connect(self.PIDInterface)
        self.pushButtonEscalado.clicked.connect(self.escaladoMainWindow)
        self.pushButtonAlarmas.clicked.connect(self.alarms)
        self.pushButtonRecetas.clicked.connect(self.recetas)
        self.pushButtonReactor.clicked.connect(self.rectorMainWindow)
        
    def PIDInterface(self):
        # Indica en que seccion se encuentra el usuario: PID, Escalado, Alarmas, Recetas, Graficos, Reactor
        self.sectionVector = [True,False,False,False,False,False]
        self.pidInterface = PID_parameters.Ui_MainWindow_PIDParameters()
        self.pidInterface.setupUi(self.MainWindow, self.sectionVector, self.s, self.sBomba)

    def alarms(self):
        self.sectionVector = [False,False,True,False,False,False]
        self.alarms = alarmsMainWindow.Ui_MainWindow()
        self.alarms.setupUi(self.MainWindow, self.sectionVector, self.s, self.sBomba)

    def recetas(self):
        self.sectionVector = [False,False,False,True,False,False]
        self.recetas = recetas1.Ui_MainWindow()
        self.recetas.setupUi(self.MainWindow, self.sectionVector, self.s, self.sBomba)

    def rectorMainWindow(self):
        # Indica en que seccion se encuentra el usuario: PID, Escalado, Alarmas, Recetas, Graficos, Reactor
        self.sectionVector = [False,False,False,False,False,True]
        self.reactor = reactorWindow2.Ui_MainWindow()
        self.reactor.setupUi(self.MainWindow, self.sectionVector, self.s, self.sBomba)

    def escaladoMainWindow(self):
        # Indica en que seccion se encuentra el usuario: PID, Escalado, Alarmas, Recetas, Graficos, Reactor
        self.sectionVector = [False,True,False,False,False,False]
        self.escalado = escalado.Ui_MainWindow()
        self.escalado.setupUi(self.MainWindow, self.sectionVector, self.s, self.sBomba)       
       
        
if __name__ == "__main__":
    import sys

    # Socket PLC
    socketPLC = serial.Serial()
    #socket.port = '/dev/tty.SLAB_USBtoUART'
    socketPLC.port = '/dev/tty.SLAB_USBtoUART'
    socketPLC.baudrate = 9600
    socketPLC.bytesize = 7
    socketPLC.parity = serial.PARITY_EVEN
    socketPLC.stopbits = 1
    socketPLC.timeout = 0.1

    # Socket bomba
    socketBomba = serial.Serial()

    socketBomba.port = '/dev/ttyUSB1'
    socketBomba.baudrate = 38400


    #p = psutil.Process(os.getpid())
    #files = p.open_files()
    #files.clear()
    
    # Try socket PLC
    try:
        socketPLC.open()
    except:
        pass

    # Try socket Bomba
    try:
        socketBomba.open()
    except:
        pass

    campoSensor1Creado = False
    conn = sqlite3.connect('statusButtonsStart.db')
    c = conn.cursor()
    #self.c.execute("DELETE FROM `sensorSuperior` WHERE 1")
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS dispositivos (id text, Horno1PID text, Horno2PID text, Horno3PID text, Horno4PID text, Solenoide text, Mantas text, Horno1Reactor text, Horno2Reactor text, Horno3Reactor text, Horno4Reactor text)''')

    for row in c.execute("SELECT * FROM dispositivos WHERE '%s'" % 1):
        if row[0] == "1":
            campoSensor1Creado = True

    if campoSensor1Creado == False:
        campoSensor1Creado = True
        c.execute("INSERT INTO dispositivos VALUES ('1','False','False','False','False', 'False','False','False','False','False','False')")
    conn.commit()

    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet('QMainWindow{background-color: qlineargradient(spread:reflect, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(0, 64, 128, 255), stop:1 rgba(0, 0, 0, 255)); border:2px solid black;}')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, socketPLC, socketBomba)
    qPoint = QPoint(0,-5)
    MainWindow.move(qPoint)
    MainWindow.show()
    sys.exit(app.exec_())
