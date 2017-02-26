# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!
import sys
sys.path.append('../DB_SQL')
import dbSQLClass
from PyQt5 import QtCore, QtGui, QtWidgets
import PID_parameters 
import alarmsMainWindow
import calculadora
import reactorMainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        dbSQLClass.DataBaseQueries()
        # Indica en que seccion se encuentra el usuario: PID, Escalado, Alarmas, Recetas, Graficos, Reactor
        self.sectionVector = [False,False,False,False,False,False]

        MainWindow.setObjectName("Reactor Quirema")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 480)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        MainWindow.setMaximumSize(QtCore.QSize(800, 480))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        buttonStyle = "background-color: #FFFFFF; border-style: outset; border-width: 10px; border-radius: 20px; border-color: #AFAFAF; padding: 6px; font-size: 25pt;"

        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 100, 271, 80))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(buttonStyle)

        self.pushButtonIcon = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonIcon.setGeometry(QtCore.QRect(130, 105, 100, 70))
        self.pushButtonIcon.setObjectName("pushButton")

        rMyIcon = QtGui.QPixmap("../images/quirema.png")
        self.pushButtonIcon.setIconSize(QtCore.QSize(70,70))
        self.pushButtonIcon.setIcon(QtGui.QIcon(rMyIcon))

        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 100, 271, 80))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet(buttonStyle)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 210, 271, 80))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet(buttonStyle)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(410, 210, 271, 80))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet(buttonStyle)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 320, 271, 80))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet(buttonStyle)

        self.pushButton_6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_6.setGeometry(QtCore.QRect(410, 320, 271, 80))
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

        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 61, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Desktop/pid.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(230, 30, 61, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Desktop/escalado.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 51, 51))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../Desktop/alarm.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(230, 140, 61, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../../Desktop/list.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(20, 240, 61, 51))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../../Desktop/graph.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(230, 240, 61, 51))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../../Desktop/reactor.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
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
        self.pushButton.setText(_translate("MainWindow", "              PID"))
        self.pushButton_2.setText(_translate("MainWindow", "Escalado"))
        self.pushButton_3.setText(_translate("MainWindow", "Alarmas"))
        self.pushButton_4.setText(_translate("MainWindow", "Recetas"))
        self.pushButton_5.setText(_translate("MainWindow", "Gráficos"))
        self.pushButton_6.setText(_translate("MainWindow", "Reactor"))

        self.pushButton.clicked.connect(self.PIDInterface)
        self.pushButton_3.clicked.connect(self.alarms)
        self.pushButton_4.clicked.connect(self.recetas)
        self.pushButton_6.clicked.connect(self.rectorMainWindow)
        
    def PIDInterface(self):
        # Indica en que seccion se encuentra el usuario: PID, Escalado, Alarmas, Recetas, Graficos, Reactor
        self.sectionVector = [True,False,False,False,False,False]
        self.pidInterface = PID_parameters.Ui_MainWindow_PIDParameters()
        self.pidInterface.setupUi(self.MainWindow, self.sectionVector)

    def alarms(self):
        self.alarms = alarmsMainWindow.Ui_MainWindow()
        self.alarms.setupUi(self.MainWindow)

    def recetas(self):
        print('recetas')
        #self.calculadora = calculadora.Ui_MainWindow()
        #self.calculadora.setupUi(self.MainWindow)

    def rectorMainWindow(self):
        # Indica en que seccion se encuentra el usuario: PID, Escalado, Alarmas, Recetas, Graficos, Reactor
        self.sectionVector = [False,False,False,False,False,True]
        self.reactor = reactorMainWindow.Ui_MainWindow()
        self.reactor.setupUi(self.MainWindow, self.sectionVector)
       
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet('QMainWindow{background-color: #333333; border:2px solid black;}')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
