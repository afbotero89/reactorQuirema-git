# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow2.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

import sys
sys.path.append('../modbusComunication')
import serialClass
from PyQt5 import QtCore, QtGui, QtWidgets
import PID_parameters
import Home
import calculadora2
import sqlite3
import threading
import time
import serialClass


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow, horno_manta_seleccionada, sectionVector, socket):

        global valorVariableAModificar, setValueFromCalculadora
        self.s = socket
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.MainWindow = MainWindow
        self.horno_manta_seleccionada = horno_manta_seleccionada
        self.sectionVector = sectionVector
        self.contador = 0
        self.instanciaModbus = serialClass.modbus(self.s)

        self.flag_DesactivaVista = False
        self.playHornos_flag = False
        valorVariableAModificar = "0"
        setValueFromCalculadora = False
        threadCreated = False
        
        self.variablePIDSeleccionada = ""
        #self.lecturaDatosPID_PLC = serialClass.modbus()
        #self.datosPID_PLC = self.lecturaDatosPID_PLC.readRegisterHorno1(self.horno_manta_seleccionada)

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(280, 100, 350, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.labelTiempoMuestreo = QtWidgets.QLabel(self.centralWidget)
        self.labelTiempoMuestreo.setGeometry(QtCore.QRect(110, 150, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTiempoMuestreo.setFont(font)
        self.labelTiempoMuestreo.setObjectName("label_2")
        self.labelGanProporcional = QtWidgets.QLabel(self.centralWidget)
        self.labelGanProporcional.setGeometry(QtCore.QRect(110, 190, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelGanProporcional.setFont(font)
        self.labelGanProporcional.setObjectName("label_3")
        self.labelGanIntegral = QtWidgets.QLabel(self.centralWidget)
        self.labelGanIntegral.setGeometry(QtCore.QRect(110, 230, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelGanIntegral.setFont(font)
        self.labelGanIntegral.setObjectName("label_5")
        self.labelGanDerivativa = QtWidgets.QLabel(self.centralWidget)
        self.labelGanDerivativa.setGeometry(QtCore.QRect(110, 270, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelGanDerivativa.setFont(font)
        self.labelGanDerivativa.setObjectName("label_7")
        self.labelDirControl = QtWidgets.QLabel(self.centralWidget)
        self.labelDirControl.setGeometry(QtCore.QRect(110, 310, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelDirControl.setFont(font)
        self.labelDirControl.setObjectName("label_8")
        self.labelRanToleranciaError = QtWidgets.QLabel(self.centralWidget)
        self.labelRanToleranciaError.setGeometry(QtCore.QRect(110, 350, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelRanToleranciaError.setFont(font)
        self.labelRanToleranciaError.setObjectName("label_10")

        self.labelLimSuperiorSalida = QtWidgets.QLabel(self.centralWidget)
        self.labelLimSuperiorSalida.setGeometry(QtCore.QRect(110, 390, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelLimSuperiorSalida.setFont(font)
        self.labelLimSuperiorSalida.setObjectName("label_14")


        self.labelLimInferiorIntegral = QtWidgets.QLabel(self.centralWidget)
        self.labelLimInferiorIntegral.setGeometry(QtCore.QRect(390, 230, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelLimInferiorIntegral.setFont(font)
        self.labelLimInferiorIntegral.setObjectName("label_11")
        self.labelPVAnterior = QtWidgets.QLabel(self.centralWidget)
        self.labelPVAnterior.setGeometry(QtCore.QRect(390, 310, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelPVAnterior.setFont(font)
        self.labelPVAnterior.setObjectName("label_12")
        self.labelValIntegralAcumulado = QtWidgets.QLabel(self.centralWidget)
        self.labelValIntegralAcumulado.setGeometry(QtCore.QRect(390, 270, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelValIntegralAcumulado.setFont(font)
        self.labelValIntegralAcumulado.setObjectName("label_13")

        self.labelLimInferiorSalida = QtWidgets.QLabel(self.centralWidget)
        self.labelLimInferiorSalida.setGeometry(QtCore.QRect(390, 150, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelLimInferiorSalida.setFont(font)
        self.labelLimInferiorSalida.setObjectName("label_15")
        self.labelLimSuperiorIntegral = QtWidgets.QLabel(self.centralWidget)
        self.labelLimSuperiorIntegral.setGeometry(QtCore.QRect(390, 190, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelLimSuperiorIntegral.setFont(font)
        self.labelLimSuperiorIntegral.setObjectName("label_16")

        self.labelGPWM = QtWidgets.QLabel(self.centralWidget)
        self.labelGPWM.setGeometry(QtCore.QRect(390, 350, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelGPWM.setFont(font)
        self.labelGPWM.setObjectName("label_17")

        # Buttons variables PID
        self.buttonTime= QtWidgets.QPushButton(self.centralWidget)
        self.buttonTime.setGeometry(QtCore.QRect(700, 80, 90, 40))
        self.buttonTime.setObjectName("pushButtonTime")
        self.buttonTime.setStyleSheet("background-color:#2F4F4F; color: white")

        self.buttonTiempoMuestreo = QtWidgets.QPushButton(self.centralWidget)
        self.buttonTiempoMuestreo.setGeometry(QtCore.QRect(30, 150, 78, 31))
        self.buttonTiempoMuestreo.setObjectName("pushButton")
        self.buttonGanProporcional = QtWidgets.QPushButton(self.centralWidget)
        self.buttonGanProporcional.setGeometry(QtCore.QRect(30, 190, 78, 31))
        self.buttonGanProporcional.setObjectName("pushButton_2")
        self.buttonGanIntegral = QtWidgets.QPushButton(self.centralWidget)
        self.buttonGanIntegral.setGeometry(QtCore.QRect(30, 230, 78, 31))
        self.buttonGanIntegral.setObjectName("pushButton_3")
        self.buttonGanDerivativa = QtWidgets.QPushButton(self.centralWidget)
        self.buttonGanDerivativa.setGeometry(QtCore.QRect(30, 270, 78, 31))
        self.buttonGanDerivativa.setObjectName("pushButton_4")
        self.buttonDireccionControl = QtWidgets.QPushButton(self.centralWidget)
        self.buttonDireccionControl.setGeometry(QtCore.QRect(30, 310, 78, 31))
        self.buttonDireccionControl.setObjectName("pushButton_5")
        self.buttonRangoToleranciaError = QtWidgets.QPushButton(self.centralWidget)
        self.buttonRangoToleranciaError.setGeometry(QtCore.QRect(30, 350, 78, 31))
        self.buttonRangoToleranciaError.setObjectName("pushButton_6")
        self.buttonLimiteSuperiorSalida = QtWidgets.QPushButton(self.centralWidget)
        self.buttonLimiteSuperiorSalida.setGeometry(QtCore.QRect(30, 390, 78, 31))
        self.buttonLimiteSuperiorSalida.setObjectName("pushButton_7")
        self.buttonLimiteInferiorSalida = QtWidgets.QPushButton(self.centralWidget)
        self.buttonLimiteInferiorSalida.setGeometry(QtCore.QRect(310, 150, 78, 31))
        self.buttonLimiteInferiorSalida.setObjectName("pushButton_8")
        self.buttonLimiteSuperiorIntegral = QtWidgets.QPushButton(self.centralWidget)
        self.buttonLimiteSuperiorIntegral.setGeometry(QtCore.QRect(310, 190, 78, 31))
        self.buttonLimiteSuperiorIntegral.setObjectName("pushButton_9")
        self.buttonLimiteInferiorIntegral = QtWidgets.QPushButton(self.centralWidget)
        self.buttonLimiteInferiorIntegral.setGeometry(QtCore.QRect(310, 230, 78, 31))
        self.buttonLimiteInferiorIntegral.setObjectName("pushButton_10")
        self.buttonValIntegralAcumulado = QtWidgets.QPushButton(self.centralWidget)
        self.buttonValIntegralAcumulado.setGeometry(QtCore.QRect(310, 270, 78, 31))
        self.buttonValIntegralAcumulado.setObjectName("pushButton_11")
        self.buttonPVAnterior = QtWidgets.QPushButton(self.centralWidget)
        self.buttonPVAnterior.setGeometry(QtCore.QRect(310, 310, 78, 31))
        self.buttonPVAnterior.setObjectName("pushButton_12")
        
        self.buttonGPWM = QtWidgets.QPushButton(self.centralWidget)
        self.buttonGPWM.setGeometry(QtCore.QRect(310, 350, 78, 31))
        self.buttonGPWM.setObjectName("pushButton_13")

        self.playButton = QtWidgets.QPushButton(self.centralWidget)
        self.playButton.setGeometry(QtCore.QRect(640, 300, 80, 80))
        self.playButton.setObjectName("playButton")
        self.playButton.setStyleSheet("background-color: black; color:white; font-size: 22pt; border-radius: 40px;")
        self.playButton.setIcon(QtGui.QIcon('../images/play-button.png'))
        self.playButton.setIconSize(QtCore.QSize(72,72))

        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(630, 170, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(630, 210, 61, 41))
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setGeometry(QtCore.QRect(630, 250, 61, 41))
        self.label_9.setObjectName("label_9")
        self.buttonSetValue = QtWidgets.QPushButton(self.centralWidget)
        self.buttonSetValue.setGeometry(QtCore.QRect(680, 210, 78, 31))
        self.buttonSetValue.setObjectName("pushButton_13")
        self.buttonPresentValue = QtWidgets.QPushButton(self.centralWidget)
        self.buttonPresentValue.setGeometry(QtCore.QRect(680, 250, 78, 31))
        self.buttonPresentValue.setObjectName("pushButton_14")
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

        self.label0 = QtWidgets.QLabel(self.centralWidget)
        self.label0.setGeometry(QtCore.QRect(0, 0, 800, 71))
        self.label0.setText("                           Parametros PLC")
        self.label0.setStyleSheet("background-color: black; color:#0080FF; font-size: 22pt;")
        self.label0.setScaledContents(True)

        self.pushButton0 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton0.setGeometry(QtCore.QRect(0, 0, 71, 71))
        self.pushButton0.setStyleSheet("background-color: #222222; color:white; font-size: 22pt;")
        self.pushButton0.setIcon(QtGui.QIcon('../images/home.png'))
        self.pushButton0.setIconSize(QtCore.QSize(31,31))

        self.pushButton1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton1.setGeometry(QtCore.QRect(73, 0, 71, 71))
        self.pushButton1.setStyleSheet("background-color: #222222; color: #222222; font-size: 22pt;")
        self.pushButton1.setIcon(QtGui.QIcon('../images/back.png'))
        self.pushButton1.setIconSize(QtCore.QSize(31,31))

        self.label1 = QtWidgets.QLabel(self.centralWidget)
        self.label1.setGeometry(QtCore.QRect(644, 0, 120, 71))
        self.label1.setText("")
        self.label1.setPixmap(QtGui.QPixmap("../images/quirema.png"))
        self.label1.setScaledContents(True)
        self.label1.setObjectName("label")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #self.actualizaValoresTimer()

        self.t = threading.Thread(target=self.actualizaValoresTimer)
        self.t.IsBackground = True;
        print(self.t)
        self.t.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Parametros PID", "Parametros PID"))
        #Labels
        self.label.setText(_translate("MainWindow", "Parametros PID:" + " " + self.horno_manta_seleccionada))
        self.labelTiempoMuestreo.setText(_translate("MainWindow", "Tiempo de muestreo "))
        self.labelGanProporcional.setText(_translate("MainWindow", "Ganancia proporcional"))
        self.labelGanIntegral.setText(_translate("MainWindow", "Ganancia integral"))
        self.labelGanDerivativa.setText(_translate("MainWindow", "Ganancia derivativa"))
        self.labelDirControl.setText(_translate("MainWindow", "Direccion de control"))
        self.labelRanToleranciaError.setText(_translate("MainWindow", "Rango de tolerancia de error"))
        self.labelLimInferiorIntegral.setText(_translate("MainWindow", "Limite inferior integral"))
        self.labelPVAnterior.setText(_translate("MainWindow", "PV anterior"))
        self.labelValIntegralAcumulado.setText(_translate("MainWindow", "Valor integral acumulado"))
        self.labelLimSuperiorSalida.setText(_translate("MainWindow", "Limite superior de salida"))
        self.labelLimInferiorSalida.setText(_translate("MainWindow", "Limite inferior de salida"))
        self.labelLimSuperiorIntegral.setText(_translate("MainWindow", "Limite superior integral"))
        self.labelGPWM.setText(_translate("MainWindow", "GPWM"))

        #Buttons

        #self.buttonTiempoMuestreo.setText(_translate("MainWindow", str(self.datosPID_PLC[0])))
        #self.buttonGanProporcional.setText(_translate("MainWindow", str(self.datosPID_PLC[1])))
        #self.buttonGanIntegral.setText(_translate("MainWindow", str(self.datosPID_PLC[2])))
        #self.buttonGanDerivativa.setText(_translate("MainWindow", str(self.datosPID_PLC[3])))
        #self.buttonDireccionControl.setText(_translate("MainWindow", str(self.datosPID_PLC[4])))
        #self.buttonRangoToleranciaError.setText(_translate("MainWindow", str(self.datosPID_PLC[5])))
        #self.buttonLimiteSuperiorSalida.setText(_translate("MainWindow", str(self.datosPID_PLC[6])))
        #self.buttonLimiteInferiorSalida.setText(_translate("MainWindow", str(self.datosPID_PLC[7])))
        #self.buttonLimiteSuperiorIntegral.setText(_translate("MainWindow", str(self.datosPID_PLC[8])))
        #self.buttonLimiteInferiorIntegral.setText(_translate("MainWindow", str(self.datosPID_PLC[9])))
        #self.buttonValIntegralAcumulado.setText(_translate("MainWindow", str(self.datosPID_PLC[10])))
        #self.buttonPVAnterior.setText(_translate("MainWindow", str(self.datosPID_PLC[11])))
        #self.buttonSetValue.setText(_translate("MainWindow", str(self.datosPID_PLC[12])))
        #self.buttonPresentValue.setText(_translate("MainWindow", str(self.datosPID_PLC[13])))
        #self.buttonGPWM.setText(_translate("MainWindow", str(self.datosPID_PLC[14])))

        self.label_4.setText(_translate("MainWindow", "Auto ajuste PID"))
        self.label_6.setText(_translate("MainWindow", "SV:"))
        self.label_9.setText(_translate("MainWindow", "PV:"))

        #Styles
        styleLabels = "color:white; font-size: 12pt;"
        styleLabelsTitles = "color: white; font-size: 12pt;"

        self.label.setStyleSheet("color:white; font-size: 18pt;")
        self.labelTiempoMuestreo.setStyleSheet(styleLabels)
        self.labelGanProporcional.setStyleSheet(styleLabels)
        
        self.labelGanIntegral.setStyleSheet(styleLabels)
        self.labelGanDerivativa.setStyleSheet(styleLabels)
        self.labelDirControl.setStyleSheet(styleLabels)
        self.labelRanToleranciaError.setStyleSheet(styleLabels)
        self.labelLimInferiorIntegral.setStyleSheet(styleLabels)
        self.labelPVAnterior.setStyleSheet(styleLabels)
        self.labelValIntegralAcumulado.setStyleSheet(styleLabels)
        self.labelLimSuperiorSalida.setStyleSheet(styleLabels)
        self.labelLimInferiorSalida.setStyleSheet(styleLabels)
        self.labelLimSuperiorIntegral.setStyleSheet(styleLabels)
        self.labelGPWM.setStyleSheet(styleLabels)

        self.label_4.setStyleSheet(styleLabelsTitles)
        self.label_6.setStyleSheet(styleLabelsTitles)
        self.label_9.setStyleSheet(styleLabelsTitles)

        #Eventos de los botones
        self.pushButton0.clicked.connect(self.home)
        self.pushButton1.clicked.connect(self.back)
        self.buttonTiempoMuestreo.clicked.connect(lambda: self.displayCalculadora('tiempoMuestreo'))
        self.buttonGanProporcional.clicked.connect(lambda: self.displayCalculadora('gananciaProporcional'))
        self.buttonGanIntegral.clicked.connect(lambda: self.displayCalculadora('gananciaIntegral'))
        self.buttonGanDerivativa.clicked.connect(lambda: self.displayCalculadora('gananciaDerivativa'))
        self.buttonDireccionControl.clicked.connect(lambda: self.displayCalculadora('direccionControl'))
        self.buttonRangoToleranciaError.clicked.connect(lambda: self.displayCalculadora('RangoToleranciaError'))
        self.buttonLimiteSuperiorSalida.clicked.connect(lambda: self.displayCalculadora('limiteSuperiorSalida'))
        self.buttonLimiteInferiorSalida.clicked.connect(lambda: self.displayCalculadora('limiteInferiorSalida'))
        self.buttonLimiteSuperiorIntegral.clicked.connect(lambda: self.displayCalculadora('LimiteSuperiorIntegral'))
        self.buttonLimiteInferiorIntegral.clicked.connect(lambda: self.displayCalculadora('limiteInferiorIntegral'))
        self.buttonValIntegralAcumulado.clicked.connect(lambda: self.displayCalculadora('valorIntegralAcumulado'))
        self.buttonPVAnterior.clicked.connect(lambda: self.displayCalculadora('PVAnterior'))
        self.buttonSetValue.clicked.connect(lambda: self.displayCalculadora('setValue'))
        #self.buttonPresentValue.clicked.connect(lambda: self.displayCalculadora('presentValue'))
        self.buttonGPWM.clicked.connect(lambda: self.displayCalculadora('gpwm'))
        self.playButton.clicked.connect(lambda: self.playHornos(self.playButton))

    def back(self):
        #self.t.cancel()
        self.flag_DesactivaVista = True
        #self.instanciaModbus.closePort()
        self.pidInterface = PID_parameters.Ui_MainWindow_PIDParameters()
        self.pidInterface.setupUi(self.MainWindow, self.sectionVector, self.s)

    def home(self):
        #self.t.cancel()
        self.flag_DesactivaVista = True
        #self.instanciaModbus.closePort()        
        self.home = Home.Ui_MainWindow()
        self.home.setupUi(self.MainWindow)

    def playHornos(self, playButtonSelected):
        self.playHornos_flag = True 
        self.hornoSeleccionado_start = self.horno_manta_seleccionada
        self.playButtonSelected_start = playButtonSelected

    def displayCalculadora(self, parametroPIDSeleccionado):
        
        if parametroPIDSeleccionado == 'play':
            pass
        else:
            self.variablePIDSeleccionada = parametroPIDSeleccionado
            self.MainWindow.setEnabled(False)
            MainWindow = QtWidgets.QMainWindow()
            calculadora = calculadora2.Ui_MainWindow()
            calculadora.setupUi_PID_reactor(MainWindow, parametroPIDSeleccionado, self.horno_manta_seleccionada, self.sectionVector, self.MainWindow, self.s)
            MainWindow.show()
        
        #self.t = threading.Timer(1, self.actualizaValoresTimer)
        #self.t.name = 'threadPIDWindow'
        #self.t.start()

    def actualizaValoresTimer(self):
        global valorVariableAModificar, setValueFromCalculadora
        
        while True:

            self.contador = self.contador + 1
            self.datosPID_PLC = self.instanciaModbus.readRegister_PIDWindow(self.horno_manta_seleccionada)

            self.datosPID_PLC_SV_PV_GPWM = self.instanciaModbus.readRegister_PIDWindow_SV_PV_GPWM(self.horno_manta_seleccionada)

            if(self.flag_DesactivaVista==True):
                break
            try:
                self.buttonTiempoMuestreo.setText(str(self.datosPID_PLC[0]))
            except:
                pass

            try:
                self.buttonGanProporcional.setText(str(self.datosPID_PLC[1]))
            except:
                pass

            try:
                self.buttonGanIntegral.setText(str(self.datosPID_PLC[2]))
            except:
                pass

            try:
                self.buttonGanDerivativa.setText(str(self.datosPID_PLC[3]))
            except:
                pass
            try:
                self.buttonDireccionControl.setText(str(self.datosPID_PLC[4]))
            except:
                pass
            try:
                self.buttonRangoToleranciaError.setText(str(self.datosPID_PLC[5]))
            except:
                pass
            try:
                self.buttonLimiteSuperiorSalida.setText(str(self.datosPID_PLC[6]))
            except:
                pass
            try:
                self.buttonLimiteInferiorSalida.setText(str(self.datosPID_PLC[7]))
            except:
                pass
            try:
                self.buttonLimiteSuperiorIntegral.setText(str(self.datosPID_PLC[8]))
            except:
                pass
            try:
                self.buttonLimiteInferiorIntegral.setText(str(self.datosPID_PLC[9]))
            except:
                pass
            try:
                self.buttonValIntegralAcumulado.setText(str(self.datosPID_PLC[10]))
            except:
                pass
            try:
                self.buttonPVAnterior.setText(str(self.datosPID_PLC[11]))
            except:
                pass
            try:
                self.buttonSetValue.setText(str(self.datosPID_PLC_SV_PV_GPWM[0]))
            except:
                pass
            try:    
                self.buttonPresentValue.setText(str(self.datosPID_PLC_SV_PV_GPWM[1]))
            except:
                pass
            try:
                self.buttonGPWM.setText(str(self.datosPID_PLC_SV_PV_GPWM[2]))
            except:
                pass    
            hora = time.strftime("%H:%M:%S")
            #print(hora)
            try:
                self.buttonTime.setText(hora)
            except:
                pass
            if (self.playHornos_flag==True):
                self.playHornos_flag = False
                self.instanciaModbus.startHorno_vistaPID(self.horno_manta_seleccionada, self.playButtonSelected_start)

            if (setValueFromCalculadora == True):
                setValueFromCalculadora = False
                self.instanciaModbus.writeValuesPID(valorVariableAModificar,self.variablePIDSeleccionada,self.horno_manta_seleccionada)
            time.sleep(0.01)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet('QMainWindow{background-color: #BDBDBD; border:2px solid black;}')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
