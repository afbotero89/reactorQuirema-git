#Listar puertos mac, ls /dev/tty.*
#Check sum modbus protocolo (FF-suma-1), FF es 2^8 ---> complemento  a 2 
import serial
import time

class modbus:
	def __init__(self):
		try:
			self.s = serial.Serial('/dev/tty.SLAB_USBtoUART',9600)
			self.s.bytesize = 7
			self.s.parity = serial.PARITY_EVEN
			self.s.stopbits = 1

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
			#- 12. Set value
			#- 13. Present value
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

			self.vectorRegistrosHorno1 = [pidH1, pidH1 + 1, pidH1 + 2, pidH1 + 3, pidH1 + 4, pidH1 + 5, pidH1 + 6, pidH1 + 7, pidH1 + 8, pidH1 + 9, pidH1 + 10, pidH1 + 12, 4125, 4124, 4526]
			self.vectorRegistrosHorno2 = [pidH2, pidH2 + 1, pidH2 + 2, pidH2 + 3, pidH2 + 4, pidH2 + 5, pidH2 + 6, pidH2 + 7, pidH2 + 8, pidH2 + 9, pidH2 + 10, pidH2 + 12, 4135, 4134, 4529]
			self.vectorRegistrosHorno3 = [pidH3, pidH3 + 1, pidH3 + 2, pidH3 + 3, pidH3 + 4, pidH3 + 5, pidH3 + 6, pidH3 + 7, pidH3 + 8, pidH3 + 9, pidH3 + 10, pidH3 + 12, 4145, 4144, 4532]
			self.vectorRegistrosHorno4 = [pidH4, pidH4 + 1, pidH4 + 2, pidH4 + 3, pidH4 + 4, pidH4 + 5, pidH4 + 6, pidH4 + 7, pidH4 + 8, pidH4 + 9, pidH4 + 10, pidH4 + 12, 4155, 4154, 4596]
			
			self.registrosRampasHornos_Hex = ['1021','102B','1035','103F']

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

			self.registrosPIDHornosLectura = []
			self.registrosHorno = []
			self.registros_SetPresent_Value_Hornos = []

		except:
			print("error en la conexion con el plc")

	################################################
	### Hornos lecturas de datos, vista variables PID
	################################################
	def readRegisterHorno1(self, horno_manta_seleccionada):
		#print("horno=",horno_manta_seleccionada)
		try:
			if (horno_manta_seleccionada=='horno1'):
				vectorRegistros = self.vectorRegistrosHorno1_Hex
			elif(horno_manta_seleccionada=='horno2'):
				vectorRegistros = self.vectorRegistrosHorno2_Hex
			elif(horno_manta_seleccionada=='horno3'):
				vectorRegistros = self.vectorRegistrosHorno3_Hex
			elif(horno_manta_seleccionada=='horno4'):
				vectorRegistros = self.vectorRegistrosHorno4_Hex

			startBit = ':'  #Bit de inicio
			stopbits = '\r\n' #Bis de stop
			prefijo = '0103' #01: direccion, 03:operacion lectura (06 es para escritura)
			sufijo = '000D' #Numero de registros a leer, 11 en este caso

			###### leyendo 11 registros 000B registros #######
			#vectorRegistros[0] -> vamos a leer 11 registros a partir del primero, split('x')-> porque el retorno es con formato 0x0A, pos[1]-> el split retorna (0,0a), upper() para volverlo mayuscula
			registro = (vectorRegistros[0].split('x')[1]).upper()     
			
			modbusCommand = prefijo + registro + sufijo

			#print(modbusCommand)

			vectorModbus = list(modbusCommand)

			#Calculo del chec sum: FF - (suma de todos los bits por pares) + 1
			checkSum = self.checkSumCalculation(vectorModbus)

			# if el checksum es solo un dato ej: A, debe completarse 0A, debe ir en dos bits
			if len(checkSum) == 1:
				comandoModbus = startBit + modbusCommand + '0' + checkSum.upper() + '\r\n'
				
			elif len(checkSum) == 2:
				comandoModbus = startBit + modbusCommand + checkSum.upper() + '\r\n'

			self.s.write(bytes(comandoModbus,'UTF-8'))	
			time.sleep(0.1)

			variablesPID_4506_4518 = self.s.readline()   # lee serial

			if len(variablesPID_4506_4518) < 60:
				self.s.write(bytes(comandoModbus,'UTF-8'))	
				variablesPID_4506_4518 = self.s.readline()   # lee serial

			print('leido', variablesPID_4506_4518, len(variablesPID_4506_4518))
			print('escrito', comandoModbus, len(comandoModbus))
			
			#Lee set_value_present_value
			registro_SV_PV = (vectorRegistros[13].split('x')[1]).upper() 
			sufijo_SV_PV = '0002'
			modbusCommand_SV_PV = prefijo + registro_SV_PV + sufijo_SV_PV
			vectorModbus_SV_PV = list(modbusCommand_SV_PV)
			checksum_SV_PV = self.checkSumCalculation(vectorModbus_SV_PV)

			#Lee GPWM
			registro_GPWM = (vectorRegistros[14].split('x')[1]).upper() 
			sufijo_GPWM = '0001'
			modbusCommand_GPWM = prefijo + registro_GPWM + sufijo_GPWM
			vectorModbus_GPWM = list(modbusCommand_GPWM)
			checksum_GPWM = self.checkSumCalculation(vectorModbus_GPWM)

			if len(checksum_SV_PV) == 1:

				self.s.write(bytes(startBit + modbusCommand_SV_PV + '0' + checksum_SV_PV.upper() + '\r\n','UTF-8'))

			elif len(checksum_SV_PV) == 2:

				self.s.write(bytes(startBit + modbusCommand_SV_PV + checksum_SV_PV.upper() + '\r\n','UTF-8'))


			variablePID_SV_PV =  self.s.readline()   # lee serial

			if len(checksum_GPWM) == 1:

				self.s.write(bytes(startBit + modbusCommand_GPWM + '0' + checksum_GPWM.upper() + '\r\n','UTF-8'))

			elif len(checksum_GPWM) == 2:

				self.s.write(bytes(startBit + modbusCommand_GPWM + checksum_GPWM.upper() + '\r\n','UTF-8'))

			
			variablePID_GPWM = self.s.readline()   # lee serial

			try:
				# ej retorno plc(plc -> pc) =  ':01 03 0C = numero de bytes 00 0A 00 14 00 1E 00 28 00 32 00 3C 1E'

				variablesPID_4506_4518 = str(variablesPID_4506_4518).split(':')[1]

				registros = list(variablesPID_4506_4518)

				registros = registros[6::] #Se discriminan los primeros 6 bits (01 direccion, 03 lectura escritura, 0C contador bits)

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
				
				# Agrupo lista en grupos de cuatro

				#print(registros, "longitud vector = ", len(registros))
				for i in range(26):
					self.registrosPIDHornosLectura.append(registros[i*2] + registros[i*2 + 1])


				for i in range(13):
					self.registrosHorno.append(self.registrosPIDHornosLectura[i*2] + self.registrosPIDHornosLectura[i*2 + 1])

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
						int(self.registrosHorno[12],16),
						int(presentValueHorno,16),
						int(setValueHorno,16),
						int(registros_GPWM,16))
			except:
				#self.readRegisterHorno1(horno_manta_seleccionada)
				return ('--','--','--','--','--','--','--','--','--','--','--','--','--','--','--')
			
		except:
			#self.readRegisterHorno1(horno_manta_seleccionada)
			return ('--','--','--','--','--','--','--','--','--','--','--','--','--','--','--')

	###################################################
	### Hornos Escritura de datos, vista variables PID
	###################################################		
	def writeValuesPID(self, valorPID, variablePID, horno_mantaSeleccionada):

		try:
			#print('horno seleccionadoX=',horno_mantaSeleccionada)
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
			        registro = vectorRegistros[12]
			elif variablePID == 'presentValue':
			        registro = vectorRegistros[13]
			elif variablePID == 'gpwm':
			        registro = vectorRegistros[14]
			elif variablePID == 'rampa':
					registro = registroRampa

			startBit = ':'
			stopbits = '\r\n'
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
			
			vectorModbus = list(modbusCommand)
			#Calculo del chec sum: FF - (suma de todos los bits por pares) + 1
			checkSum = self.checkSumCalculation(vectorModbus)

			if len(checkSum)==1:
				checkSum = '0' + checkSum  # El check sum debe ir en dos bytes (ej: si es F, debe convertirse en 0F)

			modbusCommand = bytes(startBit + modbusCommand + checkSum + stopbits, 'UTF-8')
			
			self.s.write(modbusCommand)
			time.sleep(0.1)
			respuestaPLC = self.s.readline()
			
			if (modbusCommand == respuestaPLC):
				pass  # Si la respuesta del plc es el mismo comando modbus que se escribio, fue existosa la modificacion del registro
			else:
				time.sleep(0.2)
				self.s.write(modbusCommand)
				
			print('respuestaPLC', respuestaPLC)
			print('escrito',modbusCommand)
			#self.instrument.write_register(registro,valorPID,1)
		except:
			time.sleep(0.2)
			self.s.write(modbusCommand)
			print("error de escritura")
	
	######################################################
	### Hornos Escritura de datos, vista variables PID ###
	######################################################	
	def read_variablesVistaReactor(self):
		try:
			#Lee set_value_present_value

			for i in range(4):
				registrosRampa = self.registrosRampasHornos_Hex[i]
				if i == 0:
					registro = self.vectorRegistrosHorno1_Hex[13]
				elif i == 1:
					registro = self.vectorRegistrosHorno2_Hex[13]
				elif i == 2:
					registro = self.vectorRegistrosHorno3_Hex[13]
				elif i == 3:
					registro = self.vectorRegistrosHorno4_Hex[13]

				registro_SV_PV = (registro.split('x')[1]).upper()
				startBit = ':'
				prefijo = '0103'  
				sufijo_SV_PV = '0002'  #Numero de registros para leer
				sufijoRampa = '0001'

				modbusCommand_SV_PV = prefijo + registro_SV_PV + sufijo_SV_PV
				vectorModbus_SV_PV = list(modbusCommand_SV_PV)
				checksum_SV_PV = self.checkSumCalculation(vectorModbus_SV_PV)

				comandoModbus_Rampa = prefijo + registrosRampa + sufijoRampa
				vectorModbus_Rampa = list(comandoModbus_Rampa)
				checksum_Rampa = self.checkSumCalculation(vectorModbus_Rampa)

				if len(checksum_SV_PV) == 1:
					self.s.write(bytes(startBit + modbusCommand_SV_PV + '0' + checksum_SV_PV.upper() + '\r\n','UTF-8'))
				elif len(checksum_SV_PV) == 2:
					self.s.write(bytes(startBit + modbusCommand_SV_PV + checksum_SV_PV.upper() + '\r\n','UTF-8'))

				variablePID_SV_PV =  self.s.readline()   # lee serial sv-presentValue

				if len(checksum_Rampa) == 1:
					self.s.write(bytes(startBit + comandoModbus_Rampa + '0' + checksum_Rampa.upper() + '\r\n','UTF-8'))
				elif len(checksum_SV_PV) == 2:
					self.s.write(bytes(startBit + comandoModbus_Rampa + checksum_Rampa.upper() + '\r\n','UTF-8'))

				variablePID_rampa =  self.s.readline()   # lee serial rampa

				registroRampa =  str(variablePID_rampa).split(':')[1]
				registroRampa = list(registroRampa)
				registroRampa = registroRampa[6::] #Se discriminan los primeros 6 bits (01 direccion, 03 lectura escritura, 0C contador bits)

				rampa = registroRampa[0] + registroRampa[1] + registroRampa[2] + registroRampa[3]

				#### Set value-present value
				registros_SV_PV = str(variablePID_SV_PV).split(':')[1]
				registros_SV_PV = list(registros_SV_PV)
				registros_SV_PV = registros_SV_PV[6::] #Se discriminan los primeros 6 bits (01 direccion, 03 lectura escritura, 0C contador bits)

				setValueHorno = registros_SV_PV[0] + registros_SV_PV[1] + registros_SV_PV[2] + registros_SV_PV[3]
				presentValueHorno = registros_SV_PV[4] + registros_SV_PV[5] + registros_SV_PV[6] + registros_SV_PV[7]

				self.registros_SetPresent_Value_Hornos.append(setValueHorno)
				self.registros_SetPresent_Value_Hornos.append(presentValueHorno)
				self.registros_SetPresent_Value_Hornos.append(rampa)
			
				
			return (self.registros_SetPresent_Value_Hornos)
		except:
			#self.read_variablesVistaReactor()
			return ['0','0','0','0','0','0','0','0','0','0','0','0']


	################################################
	### Lectura parametros de hornos(interfaz reactor): present value: PV, set value: SV, rampa: R, por definir: X: 
	################################################	
	def write_variablesHornos(self, variablesHornos):
		
		try:
			# Horno 1

			self.instrument.write_register(1556,variablesHornos[0][1],1)
			self.instrument.write_register(1556,variablesHornos[0][2],1)
			self.instrument.write_register(1556,variablesHornos[0][3],1)
			self.instrument.write_register(1556,variablesHornos[0][4],1)

			# Horno 2
			self.instrument.write_register(1556,variablesHornos[1][1],1)
			self.instrument.write_register(1556,variablesHornos[1][2],1)
			self.instrument.write_register(1556,variablesHornos[1][3],1)
			self.instrument.write_register(1556,variablesHornos[1][4],1)

			# Horno 3
			self.instrument.write_register(1556,variablesHornos[2][1],1)
			self.instrument.write_register(1556,variablesHornos[2][2],1)
			self.instrument.write_register(1556,variablesHornos[2][3],1)
			self.instrument.write_register(1556,variablesHornos[2][4],1)

			# Horno 4
			self.instrument.write_register(1556,variablesHornos[3][1],1)
			self.instrument.write_register(1556,variablesHornos[3][2],1)
			self.instrument.write_register(1556,variablesHornos[3][3],1)
			self.instrument.write_register(1556,variablesHornos[3][4],1)
		except:
			print('error en la escritura de datos en plc')

	def checkSumCalculation(self,vectorModbus):
		#Calculo del chec sum: FF - (suma de todos los bits por pares) + 1
		checkSum = int('FF',16) - (int(vectorModbus[0] + vectorModbus[1],16) + int(vectorModbus[2] + vectorModbus[3],16) + int(vectorModbus[4] + vectorModbus[5],16) + int(vectorModbus[6] + vectorModbus[7],16) + int(vectorModbus[8] + vectorModbus[9],16) + int(vectorModbus[10] + vectorModbus[11],16)) + 1
		if checkSum < 0:
			checkSum = checkSum + 255 + 1

		checkSum = hex(checkSum).split('x')[1]  #split('x') porque el retorno de convertir un int a un hex es 0x0A, queda (0,0A)
		#print(checkSum.upper())
		#Cuando el numero hexadecimal contiene letras ej: 0x0A, python retorna 0a, se debe volver mayuscula
		
		return checkSum.upper() 