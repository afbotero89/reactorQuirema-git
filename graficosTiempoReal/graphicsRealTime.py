import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import numpy as np
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
import threading
import socket
import time
from matplotlib.figure import Figure
import sys
sys.path.append('../modbusComunication/')
import modbusClass

plt.ion()

class Ui_MainWindow(object):
    def __init__(self):
        self.listaX = [0]
        self.listaY = [0]
        
        self.contadorX = 0
        self.contadorY = 0
        
        self.fig, self.ax = plt.subplots()
        self.ax.set_xticklabels([])
        self.labels = [0]
        self.modbusInstance = modbusClass.modbus()
        print('xxxxx')
        while True:
            self.insertPoint()
            time.sleep(1)

    def insertPoint(self):
        temperaturaTermocupla = self.modbusInstance.readRegisterTermocuple1()
        print('temperatura termocupla')
        print(temperaturaTermocupla)
        self.contadorX = self.contadorX + 20
        self.contadorY = self.contadorY + 1

        self.listaX.append(self.contadorX)
        self.listaY.append(temperaturaTermocupla)

        y = np.random.random()
        hourData = time.strftime("%H:%M:%S")
        plt.cla()
        plt.grid(True)
        plt.plot(self.listaX, self.listaY,marker='o', linestyle='-', color='b', label = "Temperatura 1", markersize=3)
        
        # major ticks every 20, minor ticks every 5                                      
        major_ticks_x = np.arange(0, 501, 20)                                              
        minor_ticks_x = np.arange(0, 501, 5)

        # major ticks every 20, minor ticks every 5                                      
        major_ticks_y = np.arange(0, 100, 5)                                              
        minor_ticks_y = np.arange(0, 100, 5) 

        self.ax.set_xticks(major_ticks_x)                                                       
        self.ax.set_xticks(minor_ticks_x, minor=True)                                           
        self.ax.set_yticks(major_ticks_y)                                                       
        self.ax.set_yticks(minor_ticks_y, minor=True)


        for tick in self.ax.xaxis.get_major_ticks():
            tick.label.set_fontsize(8)  

        self.ax.tick_params(axis='x', colors='white')
        self.ax.tick_params(axis='y', colors='white')
        # and a corresponding grid                                                       

        self.ax.grid(which='both')                                                            

        # or if you want differnet settings for the grids:                               
        self.ax.grid(which='minor', alpha=0.2)                                                
        self.ax.grid(which='major', alpha=0.5)  

        plt.ylabel('Presion')
        plt.xlabel('Temperatura')
        plt.title('Graficos de presion')
        self.ax.yaxis.label.set_color('white')
        self.ax.xaxis.label.set_color('white')
        self.ax.title.set_color('white')
        plt.ylim([0,100])

        self.labels.append(hourData)
        self.labels[self.contadorY - 1] = hourData
        self.ax.set_xticklabels(self.labels, rotation=70)
        plt.savefig('../images/GraficoPresion.png',facecolor='#222222', edgecolor='none')
        plt.pause(0.5)
interfaz = Ui_MainWindow()


