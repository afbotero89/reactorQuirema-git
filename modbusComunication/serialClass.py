#Listar puertos mac, ls /dev/tty.*
#Check sum modbus protocolo (FF-suma-1), FF es 2^8 ---> complemento  a 2 
from PyQt5 import QtGui
import serial
import time
import threading
import psutil, os
import Home 

class modbus:
	def __init__(self, socket):
		instanceHome = Home.Ui_MainWindow()
		self.s = socket
		self.init_Varialbes_Serial()


	def init_Varialbes_Serial(self):
			global s

			#self.s = serial.Serial()
			#self.s.port = '/dev/tty.SLAB_USBtoUART'
			#self.s.baudrate = 9600
			#self.s.bytesize = 7
			#self.s.parity = serial.PARITY_EVEN
			#self.s.stopbits = 1
			#self.s.timeout = 0.1

			p = psutil.Process(os.getpid())
			files = p.open_files()
			files.clear()

			#if self.s.is_open == False:
			 #   self.s.open()

			s = self.s


			#print("puerto abierto",s.is_open)


			#print("datos !!!!!!")
			#print(files)
			#Registros hornos PLC orden: 
			#- 0. tiempo de muestreo
			#- 1. ganancia proporcional
			#- 2. Ganancia integral
			#- 3. Ganancia derivativa
			#- 4. Direccion de control
			#- 5. Rango de tolerancia de error
			#- 6. Limite superior de salida
			#- 7. limite inferior de salida
			#- 8. Limite superior integral
			#- 9. limite inferior integral
			#- 10. Valor integral acumulado
			#- 11. PV anterior
			#- 12. Present value
			#- 13. Set value
			#- 14. GPWM

			# Formato para lectura modbus ':0103119A000150\r\n'
			# 01 ---> Direccion
			# 03 ---> Leer registro 06---> Escribir registro 119A ---> registro hexadecimal para este caso (119A = 4506)
			# 0001 ---> Numero de registros que se quiere leer, en este caso solo es un registro.
			# 50 ---> Check sum (FF - suma de todos los numeros pares 01+03+11) + 1

			pidH1=4506
			pidH2=4536
			pidH3=4556
			pidH4=4576

			self.vectorRegistrosHorno1 = [pidH1, pidH1 + 1, pidH1 + 2, pidH1 + 3, pidH1 + 4, pidH1 + 5, pidH1 + 6, pidH1 + 7, pidH1 + 8, pidH1 + 9, pidH1 + 10, pidH1 + 12, 4124, 4125, 4526]
			self.vectorRegistrosHorno2 = [pidH2, pidH2 + 1, pidH2 + 2, pidH2 + 3, pidH2 + 4, pidH2 + 5, pidH2 + 6, pidH2 + 7, pidH2 + 8, pidH2 + 9, pidH2 + 10, pidH2 + 12, 4134, 4135, 4529]
			self.vectorRegistrosHorno3 = [pidH3, pidH3 + 1, pidH3 + 2, pidH3 + 3, pidH3 + 4, pidH3 + 5, pidH3 + 6, pidH3 + 7, pidH3 + 8, pidH3 + 9, pidH3 + 10, pidH3 + 12, 4144, 4145, 4532]
			self.vectorRegistrosHorno4 = [pidH4, pidH4 + 1, pidH4 + 2, pidH4 + 3, pidH4 + 4, pidH4 + 5, pidH4 + 6, pidH4 + 7, pidH4 + 8, pidH4 + 9, pidH4 + 10, pidH4 + 12, 4154, 4155, 4596]
			
			# Registros mantas para escribir
			self.presentValue_setValue_onOff_Mantas = ['1044', '1045','0813']

			# Registros solenoide para escribir
			self.injection_load_onOff_solenoide = ['1019','101A','081A']


			# Rampas valores en decimal: 4129, 4139, 4149, 4159
			self.registrosRampasHornos_Hex = ['1021','102B','1035','103F']

			# Registros controladores de flujo masico (MFC: Mass flow controllers)
			
			# Set values inicia a partir del registro 4098 (Dec) = 1002 (Hex), termina en 4101
			# Present values inician a partir del registro 4197 (Dec) = 1065 (Hex), termina en 4200

			self.registrosMFC1_SV_PV = ['1002','1065']
			self.registrosMFC2_SV_PV = ['1003','1066']
			self.registrosMFC3_SV_PV = ['1004','1067']
			self.registrosMFC4_SV_PV = ['1005','1068']
			self.registrosMFC5_SV_PV = ['1006','1069']
			self.registrosMFC6_SV_PV = ['1007','106A']

			# Escalado inicia a partir del registro 4606 (Dec) = 11FE (Hex), termina en 4621(Dec) = 120D(Hex)
			# In: Xmax, Xmin, Ymax, Ymin
			self.registrosMFC1_IN = ['11FE','11FF','1200','1201']
			self.registrosMFC2_IN = ['1202','1203','1204','1205']
			self.registrosMFC3_IN = ['1206','1207','1208','1209']
			self.registrosMFC4_IN = ['120A','120B','120C','120D']
			self.registrosMFC5_IN = ['120E','120F','1210','1211']
			self.registrosMFC6_IN = ['1212','1213','1214','1215']

			# Escalado inicia a partir del registro 4631 (Dec) = 1217 (Hex), termina en 4646 (Dec) = 1226(Hex)
			# Out: Xmax, Xmin, Ymax, Ymin
			self.registrosMFC1_OUT = ['1217','1218','1219','121A']
			self.registrosMFC2_OUT = ['121B','121C','121D','121E']
			self.registrosMFC3_OUT = ['121F','1220','1221','1222']
			self.registrosMFC4_OUT = ['1223','1224','1225','1226']
			self.registrosMFC5_OUT = ['1227','1228','1229','122A']
			self.registrosMFC6_OUT = ['122B','122C','122D','122E']

			self.vectorRegistrosHorno1_Hex = [hex(self.vectorRegistrosHorno1[0]),
											  hex(self.vectorRegistrosHorno1[1]),
											  hex(self.vectorRegistrosHorno1[2]),
											  hex(self.vectorRegistrosHorno1[3]),
											  hex(self.vectorRegistrosHorno1[4]),
											  hex(self.vectorRegistrosHorno1[5]),
											  hex(self.vectorRegistrosHorno1[6]),
											  hex(self.vectorRegistrosHorno1[7]),
											  hex(self.vectorRegistrosHorno1[8]),
											  hex(self.vectorRegistrosHorno1[9]),
											  hex(self.vectorRegistrosHorno1[10]),
											  hex(self.vectorRegistrosHorno1[11]),
											  hex(self.vectorRegistrosHorno1[12]),
											  hex(self.vectorRegistrosHorno1[13]),
											  hex(self.vectorRegistrosHorno1[14])]

			self.vectorRegistrosHorno2_Hex = [hex(self.vectorRegistrosHorno2[0]),
											  hex(self.vectorRegistrosHorno2[1]),
											  hex(self.vectorRegistrosHorno2[2]),
											  hex(self.vectorRegistrosHorno2[3]),
											  hex(self.vectorRegistrosHorno2[4]),
											  hex(self.vectorRegistrosHorno2[5]),
											  hex(self.vectorRegistrosHorno2[6]),
											  hex(self.vectorRegistrosHorno2[7]),
											  hex(self.vectorRegistrosHorno2[8]),
											  hex(self.vectorRegistrosHorno2[9]),
											  hex(self.vectorRegistrosHorno2[10]),
											  hex(self.vectorRegistrosHorno2[11]),
											  hex(self.vectorRegistrosHorno2[12]),
											  hex(self.vectorRegistrosHorno2[13]),
											  hex(self.vectorRegistrosHorno2[14])]

			self.vectorRegistrosHorno3_Hex = [hex(self.vectorRegistrosHorno3[0]),
											  hex(self.vectorRegistrosHorno3[1]),
											  hex(self.vectorRegistrosHorno3[2]),
											  hex(self.vectorRegistrosHorno3[3]),
											  hex(self.vectorRegistrosHorno3[4]),
											  hex(self.vectorRegistrosHorno3[5]),
											  hex(self.vectorRegistrosHorno3[6]),
											  hex(self.vectorRegistrosHorno3[7]),
											  hex(self.vectorRegistrosHorno3[8]),
											  hex(self.vectorRegistrosHorno3[9]),
											  hex(self.vectorRegistrosHorno3[10]),
											  hex(self.vectorRegistrosHorno3[11]),
											  hex(self.vectorRegistrosHorno3[12]),
											  hex(self.vectorRegistrosHorno3[13]),
											  hex(self.vectorRegistrosHorno3[14])]

			self.vectorRegistrosHorno4_Hex = [hex(self.vectorRegistrosHorno4[0]),
											  hex(self.vectorRegistrosHorno4[1]),
											  hex(self.vectorRegistrosHorno4[2]),
											  hex(self.vectorRegistrosHorno4[3]),
											  hex(self.vectorRegistrosHorno4[4]),
											  hex(self.vectorRegistrosHorno4[5]),
											  hex(self.vectorRegistrosHorno4[6]),
											  hex(self.vectorRegistrosHorno4[7]),
											  hex(self.vectorRegistrosHorno4[8]),
											  hex(self.vectorRegistrosHorno4[9]),
											  hex(self.vectorRegistrosHorno4[10]),
											  hex(self.vectorRegistrosHorno4[11]),
											  hex(self.vectorRegistrosHorno4[12]),
											  hex(self.vectorRegistrosHorno4[13]),
											  hex(self.vectorRegistrosHorno4[14])]

			self.vectorReceta1 = ['1898','1899','189A','189B','189C','189D','189E','189F','18A0','18A1','18A2','18A3','18A4','18A5']
			self.vectorReceta2 = ['18A6','18A7','18A8','18A9','18AA','18AB','18AC','18AD','18AE','18AF','18B0','18B1','18B2','18B3']
			self.vectorReceta3 = ['18B4','18B5','18B6','18B7','18B8','18B9','18BA','18BB','18BC','18BD','18BE','18BF','18C0','18C1']
			self.vectorReceta4 = ['18C2','18C3','18C4','18C5','18C6','18C7','18C8','18C9','18CA','18CB','18CC','18CD','18CE','18CF']

			self.vectorReceta5 = ['18D0','18D1','18D2','18D3','18D4','18D5','18D6','18D7','18D8','18D9','18DA','18DB','18DC','18DD']
			self.vectorReceta6 = ['18DE','18DF','18E0','18E1','18E2','18E3','18E4','18E5','18E6','18E7','18E8','18E9','18EA','18EB']
			self.vectorReceta7 = ['18EC','18ED','18EE','18EF','18F0','18F1','18F2','18F3','18F4','18F5','18F6','18F7','18F8','18F9']
			self.vectorReceta8 = ['18FA','18FB','18FC','18FD','18FE','18FF','1900','1901','1902','1903','1904','1905','1906','1907']

			self.registrosPIDHornosLectura = []
			self.registrosHorno = []
			self.registros_SetPresent_Value_Hornos = []
			self.registros_SetPresent_Value_Hornos_rampa = []
			self.registrosEscalado_IN = []
			self.registrosEscalado_OUT = []
			self.registrosRecetas = []
			self.startBit = ':'
			self.prefijo_lectura = '0103' #01: direccion, 03:operacion lectura (06 es para escritura)
			self.stopbits = '\r\n' #Bis de stop

			self.start_Horno1_PIDWindow = False
			self.start_Horno2_PIDWindow = False
			self.start_Horno3_PIDWindow = False
			self.start_Horno4_PIDWindow = False

			self.start_Horno1_Reactor = False
			self.start_Horno2_Reactor = False
			self.start_Horno3_Reactor = False
			self.start_Horno4_Reactor = False

			self.startSolenoideReactor_flag = False
			self.startMantasReactor_flag = False


	def readRegister_Reactor(self):
		global s
		#print("horno=",horno_manta_seleccionada)
		try:
			self.registrosHorno = []

			sufijo = '0044' #Numero de registros a leer, 68 en este caso
			###### leyendo 11 registros 000B registros #######
			#vectorRegistros[0] -> vamos a leer 11 registros a partir del primero, split('x')-> porque el retorno es con formato 0x0A, pos[1]-> el split retorna (0,0a), upper() para volverlo mayuscula
			registro = '1002'    
			
			modbusCommand = self.prefijo_lectura + registro + sufijo

			#Calculo del chec sum: FF - (suma de todos los bits por pares) + 1
			checkSum = self.checkSumCalculation(modbusCommand)

			comandoModbus = self.startBit + modbusCommand + checkSum + '\r\n'

			s.write(bytes(comandoModbus,'UTF-8'))	
			
			time.sleep(0.1)
			
			#print(self.startBit + modbusCommand + checkSum)

			variablesPID_4506_4518 = s.readline()   # lee serial

			#print(variablesPID_4506_4518)
			# ej retorno plc(plc -> pc) =  ':01 03 0C = numero de bytes 00 0A 00 14 00 1E 00 28 00 32 00 3C 1E'

			variablesPID_4506_4518 = str(variablesPID_4506_4518).split(':')[1]

			registros = list(variablesPID_4506_4518)

			registros = registros[6::] #Se discriminan los primeros 6 bits (01 direccion, 03 lectura escritura, 0C contador bits)
			
			for i in range(68):
				self.registrosHorno.append(registros[i*4] + registros[(i*4) + 1] + registros[(i*4) + 2] + registros[(i*4) + 3])

			# Agrupo lista en grupos de cuatro
			return self.registrosHorno
		except:
			pass

	################################################
	### Hornos lecturas de datos, vista variables PID
	################################################
	def readRegister_PIDWindow(self, horno_manta_seleccionada):
		global s
		#print("horno=",horno_manta_seleccionada)
		self.registrosHorno = []
		#self.readRegister_Reactor()
		try:

			if (horno_manta_seleccionada=='horno1'):
				vectorRegistros = self.vectorRegistrosHorno1_Hex
			elif(horno_manta_seleccionada=='horno2'):
				vectorRegistros = self.vectorRegistrosHorno2_Hex
			elif(horno_manta_seleccionada=='horno3'):
				vectorRegistros = self.vectorRegistrosHorno3_Hex
			elif(horno_manta_seleccionada=='horno4'):
				vectorRegistros = self.vectorRegistrosHorno4_Hex

			sufijo = '000D' #Numero de registros a leer, 13 en este caso

			###### leyendo 11 registros 000B registros #######
			#vectorRegistros[0] -> vamos a leer 11 registros a partir del primero, split('x')-> porque el retorno es con formato 0x0A, pos[1]-> el split retorna (0,0a), upper() para volverlo mayuscula
			registro = (vectorRegistros[0].split('x')[1]).upper()     
			
			modbusCommand = self.prefijo_lectura + registro + sufijo

			#Calculo del chec sum: FF - (suma de todos los bits por pares) + 1
			checkSum = self.checkSumCalculation(modbusCommand)

			comandoModbus = self.startBit + modbusCommand + checkSum + '\r\n'

			s.write(bytes(comandoModbus,'UTF-8'))	
			
			time.sleep(0.1)
			
			#print(self.startBit + modbusCommand + checkSum)

			variablesPID_4506_4518 = s.readline()   # lee serial

			#print(variablesPID_4506_4518)
			# ej retorno plc(plc -> pc) =  ':01 03 0C = numero de bytes 00 0A 00 14 00 1E 00 28 00 32 00 3C 1E'

			variablesPID_4506_4518 = str(variablesPID_4506_4518).split(':')[1]

			registros = list(variablesPID_4506_4518)
			print("valores evaluar",comandoModbus, variablesPID_4506_4518)
			registros = registros[6::] #Se discriminan los primeros 6 bits (01 direccion, 03 lectura escritura, 0C contador bits)
			
			# Agrupo lista en grupos de cuatro
			#print("registros horno = ", registros)
			for i in range(13):
				self.registrosHorno.append(registros[i*4] + registros[(i*4) + 1] + registros[(i*4) + 2] + registros[(i*4) + 3])

			hora = time.strftime("%H:%M:%S")

			#print(hora)
			
			return (int(self.registrosHorno[0],16),
					int(self.registrosHorno[1],16),
					int(self.registrosHorno[2],16),
					int(self.registrosHorno[3],16),
					int(self.registrosHorno[4],16),
					int(self.registrosHorno[5],16),
					int(self.registrosHorno[6],16),
					int(self.registrosHorno[7],16),
					int(self.registrosHorno[8],16),
					int(self.registrosHorno[9],16),
					int(self.registrosHorno[10],16),
					int(self.registrosHorno[12],16))
	
		except:
			pass	
			#self.init_Varialbes_Serial()

	def readRegister_PIDWindow_SV_PV_GPWM(self, horno_manta_seleccionada):
		global s
		try:
			if (horno_manta_seleccionada=='horno1'):
				vectorRegistros = self.vectorRegistrosHorno1_Hex
			elif(horno_manta_seleccionada=='horno2'):
				vectorRegistros = self.vectorRegistrosHorno2_Hex
			elif(horno_manta_seleccionada=='horno3'):
				vectorRegistros = self.vectorRegistrosHorno3_Hex
			elif(horno_manta_seleccionada=='horno4'):
				vectorRegistros = self.vectorRegistrosHorno4_Hex

			sufijo = '000D' #Numero de registros a leer, 11 en este caso
			#Lee set_value_present_value
			registro_SV_PV = (vectorRegistros[12].split('x')[1]).upper() 
			sufijo_SV_PV = '0002'
			modbusCommand_SV_PV = self.prefijo_lectura + registro_SV_PV + sufijo_SV_PV
			checksum_SV_PV = self.checkSumCalculation(modbusCommand_SV_PV)

			#Lee GPWM
			registro_GPWM = (vectorRegistros[14].split('x')[1]).upper() 
			sufijo_GPWM = '0001'
			modbusCommand_GPWM = self.prefijo_lectura + registro_GPWM + sufijo_GPWM
			checksum_GPWM = self.checkSumCalculation(modbusCommand_GPWM)

			s.write(bytes(self.startBit + modbusCommand_SV_PV + checksum_SV_PV + '\r\n','UTF-8'))
			time.sleep(0.1)
			variablePID_SV_PV =  s.readline()   # lee serial
			#print(variablePID_SV_PV)

			s.write(bytes(self.startBit + modbusCommand_GPWM + checksum_GPWM + '\r\n','UTF-8'))
			time.sleep(0.1)
			variablePID_GPWM = s.readline()   # lee serial

			#### Set value-present value
			registros_SV_PV = str(variablePID_SV_PV).split(':')[1]
			registros_SV_PV = list(registros_SV_PV)
			registros_SV_PV = registros_SV_PV[6::] #Se discriminan los primeros 6 bits (01 direccion, 03 lectura escritura, 0C contador bits)
			setValueHorno = registros_SV_PV[0] + registros_SV_PV[1] + registros_SV_PV[2] + registros_SV_PV[3]
			presentValueHorno = registros_SV_PV[4] + registros_SV_PV[5] + registros_SV_PV[6] + registros_SV_PV[7]
			
			registros_GPWM = str(variablePID_GPWM).split(':')[1]
			registros_GPWM = list(registros_GPWM)
			registros_GPWM = registros_GPWM[6::] #Se discriminan los primeros 6 bits (01 direccion, 03 lectura escritura, 0C contador bits)
			registros_GPWM = registros_GPWM[0] + registros_GPWM[1] + registros_GPWM[2] + registros_GPWM[3]	

			return (int(presentValueHorno,16),int(setValueHorno,16),int(registros_GPWM,16))
		except:
			pass

	def readRegister_Recetas(self, recetas):
		global s
		#print("horno=",horno_manta_seleccionada)

		self.registrosRecetas = []

		try:

			sufijo = '0038' #Numero de registros a leer, 56 en este caso
			###### leyendo 56 registros 0038 registros #######
			#vectorRegistros[0] -> vamos a leer 56 registros a partir del primero, split('x')-> porque el retorno es con formato 0x0A, pos[1]-> el split retorna (0,0a), upper() para volverlo mayuscula
			registro = '1898'
			if(recetas == "hoja1"):
				registro = '1898'  
			elif(recetas == "hoja2"):  
				registro = '18D0'
			
			modbusCommand = self.prefijo_lectura + registro + sufijo

			#Calculo del chec sum: FF - (suma de todos los bits por pares) + 1
			checkSum = self.checkSumCalculation(modbusCommand)

			comandoModbus = self.startBit + modbusCommand + checkSum + '\r\n'

			s.write(bytes(comandoModbus,'UTF-8'))	
			
			time.sleep(0.1)
			
			#print(self.startBit + modbusCommand + checkSum)

			variablesPID_4506_4518 = s.readline()   # lee serial
			#print(variablesPID_4506_4518)
			# ej retorno plc(plc -> pc) =  ':01 03 0C = numero de bytes 00 0A 00 14 00 1E 00 28 00 32 00 3C 1E'

			variablesPID_4506_4518 = str(variablesPID_4506_4518).split(':')[1]

			registros = list(variablesPID_4506_4518)

			registros = registros[6::] #Se discriminan los primeros 6 bits (01 direccion, 03 lectura escritura, 0C contador bits)

			for i in range(56):
				self.registrosRecetas.append(registros[i*4] + registros[(i*4) + 1] + registros[(i*4) + 2] + registros[(i*4) + 3])

			# Agrupo lista en grupos de cuatro
			return self.registrosRecetas
		
		except:
			pass

	###################################################
	### Hornos Escritura de datos, vista variables PID
	###################################################		
	def writeValuesPID(self, valorPID, variablePID, horno_mantaSeleccionada):
		global s
		print("escritura!!!!!",variablePID, horno_mantaSeleccionada)
		try:
			
			if (horno_mantaSeleccionada=='horno1'):
			        vectorRegistros = self.vectorRegistrosHorno1_Hex
			        registroRampa = '0x' + self.registrosRampasHornos_Hex[0]
			elif(horno_mantaSeleccionada=='horno2'):
			        vectorRegistros = self.vectorRegistrosHorno2_Hex
			        registroRampa = '0x' + self.registrosRampasHornos_Hex[1]
			elif(horno_mantaSeleccionada=='horno3'):
			        vectorRegistros = self.vectorRegistrosHorno3_Hex
			        registroRampa = '0x' + self.registrosRampasHornos_Hex[2]
			elif(horno_mantaSeleccionada=='horno4'):
			        vectorRegistros = self.vectorRegistrosHorno4_Hex
			        registroRampa = '0x' + self.registrosRampasHornos_Hex[3]
			elif(horno_mantaSeleccionada=='MFC1'):
					vectorRegistros=self.registrosMFC1_SV_PV
			elif(horno_mantaSeleccionada=='MFC2'):
					vectorRegistros=self.registrosMFC2_SV_PV
			elif(horno_mantaSeleccionada=='MFC3'):
					vectorRegistros=self.registrosMFC3_SV_PV
			elif(horno_mantaSeleccionada=='MFC4'):
					vectorRegistros=self.registrosMFC4_SV_PV
			elif(horno_mantaSeleccionada=='MFC5'):
					vectorRegistros=self.registrosMFC5_SV_PV
			elif(horno_mantaSeleccionada=='MFC6'):
					vectorRegistros=self.registrosMFC6_SV_PV
			elif(horno_mantaSeleccionada=='Mantas'):
					vectorRegistros = self.presentValue_setValue_onOff_Mantas
			elif(horno_mantaSeleccionada=='Solenoide'):
					vectorRegistros = self.injection_load_onOff_solenoide

			if variablePID == 'tiempoMuestreo':
			        registro = vectorRegistros[0]
			elif variablePID == 'gananciaProporcional':
			        registro = vectorRegistros[1]
			elif variablePID == 'gananciaIntegral':
			        registro = vectorRegistros[2]
			elif variablePID == 'gananciaDerivativa':
			        registro = vectorRegistros[3]
			elif variablePID == 'direccionControl':
			        registro = vectorRegistros[4]
			elif variablePID == 'RangoToleranciaError':
			        registro = vectorRegistros[5]
			elif variablePID == 'limiteSuperiorSalida':
			        registro = vectorRegistros[6]
			elif variablePID == 'limiteInferiorSalida':
			        registro = vectorRegistros[7]
			elif variablePID == 'LimiteSuperiorIntegral':
			        registro = vectorRegistros[8]
			elif variablePID == 'limiteInferiorIntegral':
			        registro = vectorRegistros[9]
			elif variablePID == 'valorIntegralAcumulado':
			        registro = vectorRegistros[10]	
			elif variablePID == 'PVAnterior':
			        registro = vectorRegistros[11]
			elif variablePID == 'setValue':
			        registro = vectorRegistros[13]
			elif variablePID == 'presentValue':
			        registro = vectorRegistros[12]
			elif variablePID == 'gpwm':
			        registro = vectorRegistros[14]
			elif variablePID == 'rampa':
					registro = registroRampa
			elif variablePID == 'setValue_MFC':
					registro = '0x'+ vectorRegistros[0]
			elif variablePID == 'presentValue_MFC':
					registro = '0x'+ vectorRegistros[1]
			elif variablePID == 'setValue_mantas':
					registro = '0x' + vectorRegistros[1]
			elif variablePID == 'Injection':
					registro = '0x' + vectorRegistros[0]
			elif variablePID == 'Load':
					registro = '0x' + vectorRegistros[1]

			prefijo = '0106'   
			registro = (registro.split('x')[1]).upper()
			setValue = hex(int(valorPID)).split('x')[1].upper()
			if len(setValue) == 1:
				setValue = '000' + setValue
			elif len(setValue) == 2:
				setValue = '00' + setValue
			elif len(setValue) == 3:
				setValue = '0' + setValue

			modbusCommand = prefijo + registro + setValue 
			#Calculo del chec sum: FF - (suma de todos los bits por pares) + 1
			checkSum = self.checkSumCalculation(modbusCommand)

			modbusCommand = bytes(self.startBit + modbusCommand + checkSum + self.stopbits, 'UTF-8')
			
			s.write(modbusCommand)
			time.sleep(0.1)
			respuestaPLC = s.readline()
			
			if (modbusCommand == respuestaPLC):
				pass  # Si la respuesta del plc es el mismo comando modbus que se escribio, fue existosa la modificacion del registro
			else:
				s.write(modbusCommand)
				time.sleep(0.1)
				
			print('escrito',modbusCommand)
			print('respuestaPLC', respuestaPLC)
			
			#self.instrument.write_register(registro,valorPID,1)
		except:
			#time.sleep(0.2)
			#s.write(modbusCommand)
			#print("error de escritura")
			pass
	
	#######################################################
	### Recetas Escritura de datos, vista variables recetas
	#######################################################		
	def writeValuesRecetas(self, receta, equipoSeleccionado, valor):
		global s
		print("escritura receta",receta, equipoSeleccionado)
		try:
			
			if (receta=='1'):
				vectorRegistros = self.vectorReceta1
			elif(receta=='2'):
				vectorRegistros = self.vectorReceta2
			elif(receta=='3'):
				vectorRegistros = self.vectorReceta3
			elif(receta=='4'):
				vectorRegistros = self.vectorReceta4
			elif(receta=='5'):
				vectorRegistros = self.vectorReceta5
			elif(receta=='6'):
				vectorRegistros = self.vectorReceta6
			elif(receta=='7'):
				vectorRegistros = self.vectorReceta7
			elif(receta=='8'):
				vectorRegistros = self.vectorReceta8

			if equipoSeleccionado == 'horno1':
			        registro = vectorRegistros[0]
			elif equipoSeleccionado == 'horno2':
			        registro = vectorRegistros[1]
			elif equipoSeleccionado == 'horno3':
			        registro = vectorRegistros[2]
			elif equipoSeleccionado == 'horno4':
			        registro = vectorRegistros[3]
			elif equipoSeleccionado == 'MFC1':
			        registro = vectorRegistros[4]
			elif equipoSeleccionado == 'MFC2':
			        registro = vectorRegistros[5]
			elif equipoSeleccionado == 'MFC3':
			        registro = vectorRegistros[6]
			elif equipoSeleccionado == 'MFC4':
			        registro = vectorRegistros[7]
			elif equipoSeleccionado == 'MFC5':
			        registro = vectorRegistros[8]
			elif equipoSeleccionado == 'MFC6':
			        registro = vectorRegistros[9]
			elif equipoSeleccionado == 'Solenoide':
			        registro = vectorRegistros[10]	
			elif equipoSeleccionado == 'Bomba':
			        registro = vectorRegistros[11]
			elif equipoSeleccionado == 'TempMantas':
			        registro = vectorRegistros[12]
			elif equipoSeleccionado == 'Tiempo':
			        registro = vectorRegistros[13]


			prefijo = '0106'   
			setValue = hex(int(valor)).split('x')[1].upper()
			if len(setValue) == 1:
				setValue = '000' + setValue
			elif len(setValue) == 2:
				setValue = '00' + setValue
			elif len(setValue) == 3:
				setValue = '0' + setValue

			modbusCommand = prefijo + registro + setValue 
			#Calculo del chec sum: FF - (suma de todos los bits por pares) + 1
			checkSum = self.checkSumCalculation(modbusCommand)

			modbusCommand = bytes(self.startBit + modbusCommand + checkSum + self.stopbits, 'UTF-8')
			
			s.write(modbusCommand)
			time.sleep(0.1)
			respuestaPLC = s.readline()
			
			if (modbusCommand == respuestaPLC):
				pass  # Si la respuesta del plc es el mismo comando modbus que se escribio, fue existosa la modificacion del registro
			else:
				s.write(modbusCommand)
				time.sleep(0.1)
				
			print('escrito',modbusCommand)
			print('respuestaPLC', respuestaPLC)
			
			#self.instrument.write_register(registro,valorPID,1)
		except:
			#time.sleep(0.2)
			#s.write(modbusCommand)
			#print("error de escritura")
			pass
	######################################################
	### Hornos Escritura de datos, vista variables PID ###
	######################################################	

	def read_variablesVistaReactor_MFC_SV(self):
		global s
		try:
			comandoModbus_MFC_SV = self.prefijo_lectura + self.registrosMFC1_SV_PV[0] + '0006'
			checksum_MFC_SV = self.checkSumCalculation(comandoModbus_MFC_SV)
			s.write(bytes(self.startBit + comandoModbus_MFC_SV + checksum_MFC_SV + '\r\n','UTF-8'))
			time.sleep(0.1)
			variablePID_MFC_SV =  s.readline()   # lee serial sv-presentValue

			# 27 es el numero de datos retornado al consultar los 4 registros de los controladores de flujo para los SV
			#if(len(variablePID_MFC_SV) < 27):
				#s.write(bytes(self.startBit + comandoModbus_MFC_SV + checksum_MFC_SV + '\r\n','UTF-8'))
				#time.sleep(0.1)
				#variablePID_MFC_SV =  s.readline()   # lee serial sv-presentValue

			#print("len mfc sv",len(variablePID_MFC_SV))

			registros_MFC_SV =  str(variablePID_MFC_SV).split(':')[1]
			registros_MFC_SV = list(registros_MFC_SV)
			registros_MFC_SV = registros_MFC_SV[6::] #Se discriminan los primeros 6 bits (01 direccion, 03 lectura escritura, 0C contador bits)
			registros_MFC_SV = [registros_MFC_SV[0]+registros_MFC_SV[1]+registros_MFC_SV[2]+registros_MFC_SV[3],
								registros_MFC_SV[4]+registros_MFC_SV[5]+registros_MFC_SV[6]+registros_MFC_SV[7],
								registros_MFC_SV[8]+registros_MFC_SV[9]+registros_MFC_SV[10]+registros_MFC_SV[11],
								registros_MFC_SV[12]+registros_MFC_SV[13]+registros_MFC_SV[14]+registros_MFC_SV[15],
								registros_MFC_SV[16]+registros_MFC_SV[17]+registros_MFC_SV[18]+registros_MFC_SV[19],
								registros_MFC_SV[20]+registros_MFC_SV[21]+registros_MFC_SV[22]+registros_MFC_SV[23]]
			return registros_MFC_SV
		except:
			pass

	def read_variablesVistaReactor_MFC_PV(self):
		global s
		try:
			# Read present values MFC (mass flow controller)
			comandoModbus_MFC_PV = self.prefijo_lectura + self.registrosMFC1_SV_PV[1] + '0006'
			checksum_MFC_PV = self.checkSumCalculation(comandoModbus_MFC_PV)
			s.write(bytes(self.startBit + comandoModbus_MFC_PV + checksum_MFC_PV + '\r\n','UTF-8'))
			time.sleep(0.1)
			variablePID_MFC_PV =  s.readline()   # lee serial sv-presentValue

			# 27 es el numero de datos retornado al consultar los 4 registros de los controladores de flujo para los PV
			#if(len(variablePID_MFC_PV)<27):
				#s.write(bytes(self.startBit + comandoModbus_MFC_PV + checksum_MFC_PV + '\r\n','UTF-8'))
				#time.sleep(0.1)
				#variablePID_MFC_PV =  s.readline()   # lee serial sv-presentValue

			#print("len mfc pv", len(variablePID_MFC_PV))

			registros_MFC_PV =  str(variablePID_MFC_PV).split(':')[1]
			registros_MFC_PV = list(registros_MFC_PV)
			registros_MFC_PV = registros_MFC_PV[6::] #Se discriminan los primeros 6 bits (01 direccion, 03 lectura escritura, 0C contador bits)
			registros_MFC_PV = [registros_MFC_PV[0]+registros_MFC_PV[1]+registros_MFC_PV[2]+registros_MFC_PV[3],
								registros_MFC_PV[4]+registros_MFC_PV[5]+registros_MFC_PV[6]+registros_MFC_PV[7],
								registros_MFC_PV[8]+registros_MFC_PV[9]+registros_MFC_PV[10]+registros_MFC_PV[11],
								registros_MFC_PV[12]+registros_MFC_PV[13]+registros_MFC_PV[14]+registros_MFC_PV[15],
								registros_MFC_PV[16]+registros_MFC_PV[17]+registros_MFC_PV[18]+registros_MFC_PV[19],
								registros_MFC_PV[20]+registros_MFC_PV[21]+registros_MFC_PV[22]+registros_MFC_PV[23]]
			return registros_MFC_PV

		except:
			pass

	def readVarialesVistaEscalado(self):
		global s
		# Read values MFC (mass flow controller), escalado IN
		try:
			comandoModbus_MFC_IN = self.prefijo_lectura + self.registrosMFC1_IN[0] + '0031'
			checksum_MFC_IN = self.checkSumCalculation(comandoModbus_MFC_IN)
			s.write(bytes(self.startBit + comandoModbus_MFC_IN + checksum_MFC_IN + '\r\n','UTF-8'))
			time.sleep(0.1)
			variablePID_MFC_IN =  s.readline()   # lee serial sv-presentValue

			registros_MFC_IN =  str(variablePID_MFC_IN).split(':')[1]
			registros_MFC_IN = list(registros_MFC_IN)
			registros_MFC_IN = registros_MFC_IN[6::] #Se discriminan los primeros 6 bits (01 direccion, 03 lectura escritura, 0C contador bits)
			for i in range(49):
				registros_MFC = registros_MFC_IN[i*4]+registros_MFC_IN[(i*4) + 1]+registros_MFC_IN[(i*4) + 2]+registros_MFC_IN[(i*4) + 3]
				self.registrosEscalado_IN.append(registros_MFC)
		except:
			pass

		return self.registrosEscalado_IN

	###################################################
	### Hornos Escritura de datos, vista ESCALADO
	###################################################		
	def writeValues_Escalado(self, valorPID, MFC, IN_OUT, X_Y):
		global s
		try:
			
			# SI LA VARIABLE DE ENTRADA SELECCIONADA FUE IN
			if (MFC=='MFC1' and IN_OUT =='IN'):
			        vectorRegistros = self.registrosMFC1_IN
			if (MFC=='MFC2' and IN_OUT =='IN'):
			        vectorRegistros = self.registrosMFC2_IN			     
			if (MFC=='MFC3' and IN_OUT =='IN'):
			        vectorRegistros = self.registrosMFC3_IN	
			if (MFC=='MFC4' and IN_OUT =='IN'):
			        vectorRegistros = self.registrosMFC4_IN	
			if (MFC=='MFC5' and IN_OUT =='IN'):
			        vectorRegistros = self.registrosMFC5_IN	
			if (MFC=='MFC6' and IN_OUT =='IN'):
			        vectorRegistros = self.registrosMFC6_IN	

			# SI LA VARIABLE DE ENTRADA SELECCIONADA FUE OUT
			if (MFC=='MFC1' and IN_OUT =='OUT'):
			        vectorRegistros = self.registrosMFC1_OUT
			if (MFC=='MFC2' and IN_OUT =='OUT'):
			        vectorRegistros = self.registrosMFC2_OUT			     
			if (MFC=='MFC3' and IN_OUT =='OUT'):
			        vectorRegistros = self.registrosMFC3_OUT
			if (MFC=='MFC4' and IN_OUT =='OUT'):
			        vectorRegistros = self.registrosMFC4_OUT
			if (MFC=='MFC5' and IN_OUT =='OUT'):
			        vectorRegistros = self.registrosMFC5_OUT
			if (MFC=='MFC6' and IN_OUT =='OUT'):
			        vectorRegistros = self.registrosMFC6_OUT

			if X_Y == 'XMAX':
			    registro = '0x' + vectorRegistros[0]
			elif X_Y == 'XMIN':
				registro = '0x' + vectorRegistros[1]
			elif X_Y == 'YMAX':
				registro = '0x' + vectorRegistros[2]
			elif X_Y == 'YMIN':
				registro = '0x' + vectorRegistros[3]

			prefijo = '0106'   
			registro = (registro.split('x')[1]).upper()
			setValue = hex(int(valorPID)).split('x')[1].upper()
			if len(setValue) == 1:
				setValue = '000' + setValue
			elif len(setValue) == 2:
				setValue = '00' + setValue
			elif len(setValue) == 3:
				setValue = '0' + setValue

			modbusCommand = prefijo + registro + setValue 
			#Calculo del chec sum: FF - (suma de todos los bits por pares) + 1
			checkSum = self.checkSumCalculation(modbusCommand)

			modbusCommand = bytes(self.startBit + modbusCommand + checkSum + self.stopbits, 'UTF-8')
			
			s.write(modbusCommand)
			time.sleep(0.1)
			respuestaPLC = s.readline()
			print("escrito", modbusCommand, "respuesta", respuestaPLC)
			if (modbusCommand == respuestaPLC):
				pass  # Si la respuesta del plc es el mismo comando modbus que se escribio, fue existosa la modificacion del registro
			else:
				time.sleep(0.1)
				pass
				#s.write(modbusCommand)
		except:
			pass


	def startHorno_reactor(self, hornoSeleccionado, playButtonSelected):
		print("escalado", hornoSeleccionado)
		global s		
		try:
			flag_start = False
			if(hornoSeleccionado=='horno1' and self.start_Horno1_Reactor == False):
				
				checkSum = self.checkSumCalculation('0105080BFF00')
				comando = bytes(':0105080BFF00'+ checkSum + '\r\n','UTF-8')
				s.write(comando)
				time.sleep(0.1)
				lectura = s.readline()
				if (lectura==comando):
					print('start 1')
					flag_start = True
					self.start_Horno1_Reactor = True
					playButtonSelected.setStyleSheet('background:red;color:white')
					playButtonSelected.setText("Stop 1")
			elif(hornoSeleccionado=='horno2' and self.start_Horno2_Reactor == False):
				checkSum = self.checkSumCalculation('0105080DFF00')
				comando = bytes(':0105080DFF00'+ checkSum + '\r\n','UTF-8')
				s.write(comando)
				time.sleep(0.1)
				lectura = s.readline()
				if (lectura==comando):
					print('start 2')
					flag_start = True
					self.start_Horno2_Reactor = True
					playButtonSelected.setStyleSheet('background:red;color:white')
					playButtonSelected.setText("Stop 2")
			elif(hornoSeleccionado=='horno3' and self.start_Horno3_Reactor == False):
				checkSum = self.checkSumCalculation('0105080FFF00')
				comando = bytes(':0105080FFF00'+ checkSum + '\r\n','UTF-8')
				s.write(comando)
				time.sleep(0.1)
				lectura = s.readline()
				if (lectura==comando):
					print('start 3')
					flag_start = True
					self.start_Horno3_Reactor = True
					playButtonSelected.setStyleSheet('background:red;color:white')
					playButtonSelected.setText("Stop 3")
			elif(hornoSeleccionado=='horno4' and self.start_Horno4_Reactor == False):
				checkSum = self.checkSumCalculation('01050811FF00')
				comando = bytes(':01050811FF00'+ checkSum + '\r\n','UTF-8')
				s.write(comando)
				time.sleep(0.1)
				lectura = s.readline()
				if (lectura==comando):
					print('start 4')
					flag_start = True
					self.start_Horno4_Reactor = True
					playButtonSelected.setStyleSheet('background:red;color:white')
					playButtonSelected.setText("Stop 4")
			playButtonSelected.enabled = False


			if(hornoSeleccionado=='horno1' and self.start_Horno1_Reactor == True and flag_start == False):
				
				checkSum = self.checkSumCalculation('0105080B0000')
				comando = bytes(':0105080B0000'+ checkSum + '\r\n','UTF-8')
				s.write(comando)
				time.sleep(0.1)
				lectura = s.readline()
				if (lectura==comando):
					print('stop 1')
					self.start_Horno1_Reactor = False
					playButtonSelected.setStyleSheet('background:green;color:white')
					playButtonSelected.setText("Play 1")
			elif(hornoSeleccionado=='horno2' and self.start_Horno2_Reactor == True and flag_start == False):
				checkSum = self.checkSumCalculation('0105080D0000')
				comando = bytes(':0105080D0000'+ checkSum + '\r\n','UTF-8')
				s.write(comando)
				time.sleep(0.1)
				lectura = s.readline()
				if (lectura==comando):
					print('stop 2')
					self.start_Horno2_Reactor = False
					playButtonSelected.setStyleSheet('background:green;color:white')
					playButtonSelected.setText("Play 2")
			elif(hornoSeleccionado=='horno3' and self.start_Horno3_Reactor == True and flag_start == False):
				checkSum = self.checkSumCalculation('0105080F0000')
				comando = bytes(':0105080F0000'+ checkSum + '\r\n','UTF-8')
				s.write(comando)
				time.sleep(0.1)
				lectura = s.readline()
				if (lectura==comando):
					print('stop 3')
					self.start_Horno3_Reactor = False
					playButtonSelected.setStyleSheet('background:green;color:white')
					playButtonSelected.setText("Play 3")
			elif(hornoSeleccionado=='horno4' and self.start_Horno4_Reactor == True and flag_start == False):
				checkSum = self.checkSumCalculation('010508110000')
				comando = bytes(':010508110000'+ checkSum + '\r\n','UTF-8')
				s.write(comando)
				time.sleep(0.1)
				lectura = s.readline()
				if (lectura==comando):
					print('stop 4')
					self.start_Horno4_Reactor = False
					playButtonSelected.setStyleSheet('background:green;color:white')
					playButtonSelected.setText("Play 4")
		except:
			pass		
	
	def start_Valve_reactor(self,solenoideOrManta, playButtonSelected):

		# Por defecto el registro correponde al solenoide
		registro = '081A'
		print("start solenoide o manta", solenoideOrManta)
		if(solenoideOrManta == 'Solenoide'):
			registro = '081A'

			flag_start = False
			if (self.startSolenoideReactor_flag == False):
				checkSum = self.checkSumCalculation('0105' + registro + 'FF00')
				comando = bytes(':0105'+ registro +'FF00'+ checkSum + '\r\n','UTF-8')
				s.write(comando)
				time.sleep(0.1)
				lectura = s.readline()
				if (lectura==comando):
					self.startSolenoideReactor_flag = True
					flag_start = True
					playButtonSelected.setStyleSheet('background:red;color:white')
					playButtonSelected.setText("OFF")
			elif(self.startSolenoideReactor_flag == True and flag_start == False):
				checkSum = self.checkSumCalculation('0105'+ registro +'0000')
				comando = bytes(':0105' + registro + '0000'+ checkSum + '\r\n','UTF-8')
				s.write(comando)
				time.sleep(0.1)
				lectura = s.readline()
				if (lectura==comando):
					self.startSolenoideReactor_flag = False
					playButtonSelected.setStyleSheet('background:green;color:white')
					playButtonSelected.setText("ON")

		elif(solenoideOrManta == 'Mantas'):
			registro = '0813'

			flag_start = False
			if (self.startMantasReactor_flag == False):
				checkSum = self.checkSumCalculation('0105' + registro + 'FF00')
				comando = bytes(':0105'+ registro +'FF00'+ checkSum + '\r\n','UTF-8')
				s.write(comando)
				time.sleep(0.1)
				lectura = s.readline()
				if (lectura==comando):
					self.startMantasReactor_flag = True
					flag_start = True
					playButtonSelected.setStyleSheet('background:red;color:white')
					playButtonSelected.setText("OFF")
			elif(self.startMantasReactor_flag == True and flag_start == False):
				checkSum = self.checkSumCalculation('0105'+ registro +'0000')
				comando = bytes(':0105' + registro + '0000'+ checkSum + '\r\n','UTF-8')
				s.write(comando)
				time.sleep(0.1)
				lectura = s.readline()
				if (lectura==comando):
					self.startMantasReactor_flag = False
					playButtonSelected.setStyleSheet('background:green;color:white')
					playButtonSelected.setText("ON")			


	
				
	def startHorno_vistaPID(self, hornoSeleccionado, playButtonSelected):
		global s		
		try:
			flag_start = False
			if(hornoSeleccionado=='horno1' and self.start_Horno1_PIDWindow == False):		
				checkSum = self.checkSumCalculation('0105080AFF00')
				comando = bytes(':0105080AFF00'+ checkSum + '\r\n','UTF-8')
				s.write(comando)
				time.sleep(0.1)
				lectura = s.readline()
				if (lectura==comando):
					flag_start = True
					self.start_Horno1_PIDWindow = True
					playButtonSelected.setIcon(QtGui.QIcon('../images/pause-button.png'))
					print('start 1')
					
			elif(hornoSeleccionado=='horno2' and self.start_Horno2_PIDWindow == False):
				checkSum = self.checkSumCalculation('0105080CFF00')
				comando = bytes(':0105080CFF00'+ checkSum + '\r\n','UTF-8')
				s.write(comando)
				time.sleep(0.1)
				lectura = s.readline()
				if (lectura==comando):
					flag_start = True
					self.start_Horno2_PIDWindow = True
					playButtonSelected.setIcon(QtGui.QIcon('../images/pause-button.png'))
					print('start 2')
			elif(hornoSeleccionado=='horno3' and self.start_Horno3_PIDWindow == False):
				checkSum = self.checkSumCalculation('0105080EFF00')
				comando = bytes(':0105080EFF00'+ checkSum + '\r\n','UTF-8')
				s.write(comando)
				time.sleep(0.1)
				lectura = s.readline()
				if (lectura==comando):
					flag_start = True
					self.start_Horno3_PIDWindow = True
					playButtonSelected.setIcon(QtGui.QIcon('../images/pause-button.png'))
					print('start 3')
			elif(hornoSeleccionado=='horno4' and self.start_Horno4_PIDWindow == False):
				checkSum = self.checkSumCalculation('01050810FF00')
				comando = bytes(':01050810FF00'+ checkSum + '\r\n','UTF-8')
				s.write(comando)
				time.sleep(0.1)
				lectura = s.readline()
				if (lectura==comando):
					flag_start = True
					self.start_Horno4_PIDWindow = True
					playButtonSelected.setIcon(QtGui.QIcon('../images/pause-button.png'))
					print('start 4')


			if(hornoSeleccionado=='horno1' and self.start_Horno1_PIDWindow == True  and flag_start == False):		
				checkSum = self.checkSumCalculation('0105080A0000')
				comando = bytes(':0105080A0000'+ checkSum + '\r\n','UTF-8')
				s.write(comando)
				time.sleep(0.1)
				lectura = s.readline()
				if (lectura==comando):
					self.start_Horno1_PIDWindow = False
					playButtonSelected.setIcon(QtGui.QIcon('../images/play-button.png'))
					print('stop 1')
			elif(hornoSeleccionado=='horno2' and self.start_Horno2_PIDWindow == True  and flag_start == False):
				checkSum = self.checkSumCalculation('0105080C0000')
				comando = bytes(':0105080C0000'+ checkSum + '\r\n','UTF-8')
				s.write(comando)
				time.sleep(0.1)
				lectura = s.readline()
				if (lectura==comando):
					self.start_Horno2_PIDWindow = False
					playButtonSelected.setIcon(QtGui.QIcon('../images/play-button.png'))
					print('stop 2')
			elif(hornoSeleccionado=='horno3' and self.start_Horno3_PIDWindow == True and flag_start == False):
				checkSum = self.checkSumCalculation('0105080E0000')
				comando = bytes(':0105080E0000'+ checkSum + '\r\n','UTF-8')
				s.write(comando)
				time.sleep(0.1)
				lectura = s.readline()
				if (lectura==comando):
					self.start_Horno3_PIDWindow = False
					playButtonSelected.setIcon(QtGui.QIcon('../images/play-button.png'))
					print('stop 3')
			elif(hornoSeleccionado=='horno4' and self.start_Horno4_PIDWindow == True and flag_start == False):
				checkSum = self.checkSumCalculation('010508100000')
				comando = bytes(':010508100000'+ checkSum + '\r\n','UTF-8')
				s.write(comando)
				time.sleep(0.1)
				lectura = s.readline()
				if (lectura==comando):
					self.start_Horno4_PIDWindow = False
					playButtonSelected.setIcon(QtGui.QIcon('../images/play-button.png'))
					print('stop 4')
		except:
			pass

	def closePort(self):
		global s
		print('close port')
		s.close()
			
	def checkSumCalculation(self,vectorModbus):
		global s
		#Calculo del chec sum: FF - (suma de todos los bits por pares) + 1
		vectorModbus = list(vectorModbus)

		checkSum = int('FF',16) - (int(vectorModbus[0] + vectorModbus[1],16) + int(vectorModbus[2] + vectorModbus[3],16) + int(vectorModbus[4] + vectorModbus[5],16) + int(vectorModbus[6] + vectorModbus[7],16) + int(vectorModbus[8] + vectorModbus[9],16) + int(vectorModbus[10] + vectorModbus[11],16)) + 1
		if checkSum < 0:
			checkSum = checkSum + 255 + 1

		checkSum = hex(checkSum).split('x')[1]  #split('x') porque el retorno de convertir un int a un hex es 0x0A, queda (0,0A)
		if len(checkSum) == 1:
			checkSum = '0' + checkSum 
		elif len(checkSum) == 2:
			pass
		#Cuando el numero hexadecimal contiene letras ej: 0x0A, python retorna 0a, se debe volver mayuscula
		
		return checkSum.upper() 
