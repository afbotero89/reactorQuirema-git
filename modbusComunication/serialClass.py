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

			# Registros controladores de flujo masico (MFC: Mass flow controllers)
			
			# Set values inicia a partir del registro 4098 (Dec) = 1002 (Hex)
			# Present values inician a partir del registro 4197 (Dec) = 1065 (Hex)

			self.registrosMFC1_SV_PV = ['1002','1065']
			self.registrosMFC2_SV_PV = ['1003','1066']
			self.registrosMFC3_SV_PV = ['1004','1067']
			self.registrosMFC4_SV_PV = ['1005','1068']

			# Escalado inicia a partir del registro 4606 (Dec) = 11FE (Hex)
			# In: Xmax, Xmin, Ymax, Ymin
			self.registrosMFC1_IN = ['11FE','11FF','1200','1201']
			self.registrosMFC2_IN = ['1202','1203','1204','1205']
			self.registrosMFC3_IN = ['1206','1207','1208','1209']
			self.registrosMFC4_IN = ['120A','120B','120C','120D']

			# Escalado inicia a partir del registro 4631 (Dec) = 1217 (Hex)
			# Out: Xmax, Xmin, Ymax, Ymin
			self.registrosMFC1_OUT = ['1217','1218','1219','121A']
			self.registrosMFC2_OUT = ['121B','121C','121D','121E']
			self.registrosMFC3_OUT = ['121F','1220','1221','1222']
			self.registrosMFC4_OUT = ['1223','1224','1225','1226']

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
			self.registrosEscalado_IN = []
			self.registrosEscalado_OUT = []
			self.startBit = ':'
			self.prefijo_lectura = '0103' #01: direccion, 03:operacion lectura (06 es para escritura)
			self.stopbits = '\r\n' #Bis de stop

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

			sufijo = '000D' #Numero de registros a leer, 11 en este caso

			###### leyendo 11 registros 000B registros #######
			#vectorRegistros[0] -> vamos a leer 11 registros a partir del primero, split('x')-> porque el retorno es con formato 0x0A, pos[1]-> el split retorna (0,0a), upper() para volverlo mayuscula
			registro = (vectorRegistros[0].split('x')[1]).upper()     
			
			modbusCommand = self.prefijo_lectura + registro + sufijo

			#Calculo del chec sum: FF - (suma de todos los bits por pares) + 1
			checkSum = self.checkSumCalculation(modbusCommand)

			comandoModbus = self.startBit + modbusCommand + checkSum + '\r\n'

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
			modbusCommand_SV_PV = self.prefijo_lectura + registro_SV_PV + sufijo_SV_PV
			checksum_SV_PV = self.checkSumCalculation(modbusCommand_SV_PV)

			#Lee GPWM
			registro_GPWM = (vectorRegistros[14].split('x')[1]).upper() 
			sufijo_GPWM = '0001'
			modbusCommand_GPWM = self.prefijo_lectura + registro_GPWM + sufijo_GPWM
			checksum_GPWM = self.checkSumCalculation(modbusCommand_GPWM)

			self.s.write(bytes(self.startBit + modbusCommand_SV_PV + checksum_SV_PV + '\r\n','UTF-8'))

			variablePID_SV_PV =  self.s.readline()   # lee serial

			self.s.write(bytes(self.startBit + modbusCommand_GPWM + checksum_GPWM + '\r\n','UTF-8'))

			
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
			elif variablePID == 'setValue_MFC':
					registro = '0x'+ vectorRegistros[0]
			elif variablePID == 'presentValue_MFC':
					registro = '0x'+ vectorRegistros[1]

			print('registro!!!!!',registro)
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
			#self.s.write(modbusCommand)
			print("error de escritura")
	
	######################################################
	### Hornos Escritura de datos, vista variables PID ###
	######################################################	
	def read_variablesVistaReactor(self):
		# Read set values MFC (mass flow controller)
		try:
			comandoModbus_MFC_SV = self.prefijo_lectura + self.registrosMFC1_SV_PV[0] + '0004'
			checksum_MFC_SV = self.checkSumCalculation(comandoModbus_MFC_SV)
			self.s.write(bytes(self.startBit + comandoModbus_MFC_SV + checksum_MFC_SV + '\r\n','UTF-8'))
			variablePID_MFC_SV =  self.s.readline()   # lee serial sv-presentValue

			registros_MFC_SV =  str(variablePID_MFC_SV).split(':')[1]
			registros_MFC_SV = list(registros_MFC_SV)
			registros_MFC_SV = registros_MFC_SV[6::] #Se discriminan los primeros 6 bits (01 direccion, 03 lectura escritura, 0C contador bits)
			registros_MFC_SV = [registros_MFC_SV[0]+registros_MFC_SV[1]+registros_MFC_SV[2]+registros_MFC_SV[3],
								registros_MFC_SV[4]+registros_MFC_SV[5]+registros_MFC_SV[6]+registros_MFC_SV[7],
								registros_MFC_SV[8]+registros_MFC_SV[9]+registros_MFC_SV[10]+registros_MFC_SV[11],
								registros_MFC_SV[12]+registros_MFC_SV[13]+registros_MFC_SV[14]+registros_MFC_SV[15]]
		except:
			registros_MFC_SV = ['1','1','1','1']

		# Read present values MFC (mass flow controller)
		try:
			comandoModbus_MFC_PV = self.prefijo_lectura + self.registrosMFC1_SV_PV[1] + '0004'
			checksum_MFC_PV = self.checkSumCalculation(comandoModbus_MFC_PV)
			self.s.write(bytes(self.startBit + comandoModbus_MFC_PV + checksum_MFC_PV + '\r\n','UTF-8'))
			variablePID_MFC_PV =  self.s.readline()   # lee serial sv-presentValue

			registros_MFC_PV =  str(variablePID_MFC_PV).split(':')[1]
			registros_MFC_PV = list(registros_MFC_PV)
			registros_MFC_PV = registros_MFC_PV[6::] #Se discriminan los primeros 6 bits (01 direccion, 03 lectura escritura, 0C contador bits)
			registros_MFC_PV = [registros_MFC_PV[0]+registros_MFC_PV[1]+registros_MFC_PV[2]+registros_MFC_PV[3],
								registros_MFC_PV[4]+registros_MFC_PV[5]+registros_MFC_PV[6]+registros_MFC_PV[7],
								registros_MFC_PV[8]+registros_MFC_PV[9]+registros_MFC_PV[10]+registros_MFC_PV[11],
								registros_MFC_PV[12]+registros_MFC_PV[13]+registros_MFC_PV[14]+registros_MFC_PV[15]]
		except:
			registros_MFC_PV = ['2','2','2','2']	

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
				sufijo_SV_PV = '0002'  #Numero de registros para leer
				sufijoRampa = '0001'

				modbusCommand_SV_PV = self.prefijo_lectura + registro_SV_PV + sufijo_SV_PV
				checksum_SV_PV = self.checkSumCalculation(modbusCommand_SV_PV)

				comandoModbus_Rampa = self.prefijo_lectura + registrosRampa + sufijoRampa
				checksum_Rampa = self.checkSumCalculation(comandoModbus_Rampa)

				self.s.write(bytes(self.startBit + modbusCommand_SV_PV + checksum_SV_PV + '\r\n','UTF-8'))

				variablePID_SV_PV =  self.s.readline()   # lee serial sv-presentValue

				self.s.write(bytes(self.startBit + comandoModbus_Rampa + checksum_Rampa + '\r\n','UTF-8'))

				variablePID_rampa =  self.s.readline()   # lee serial rampa
				#print(variablePID_rampa)

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
			
			return (self.registros_SetPresent_Value_Hornos, registros_MFC_SV, registros_MFC_PV)
		except:
			#self.read_variablesVistaReactor()
			return ['0','0','0','0','0','0','0','0','0','0','0','0']


	def readVarialesVistaEscalado(self):
		# Read values MFC (mass flow controller), escalado IN
		try:
			comandoModbus_MFC_IN = self.prefijo_lectura + self.registrosMFC1_IN[0] + '0010'
			checksum_MFC_IN = self.checkSumCalculation(comandoModbus_MFC_IN)
			self.s.write(bytes(self.startBit + comandoModbus_MFC_IN + checksum_MFC_IN + '\r\n','UTF-8'))
			variablePID_MFC_IN =  self.s.readline()   # lee serial sv-presentValue

			registros_MFC_IN =  str(variablePID_MFC_IN).split(':')[1]
			registros_MFC_IN = list(registros_MFC_IN)
			registros_MFC_IN = registros_MFC_IN[6::] #Se discriminan los primeros 6 bits (01 direccion, 03 lectura escritura, 0C contador bits)
			for i in range(16):
				registros_MFC = registros_MFC_IN[i*4]+registros_MFC_IN[(i*4) + 1]+registros_MFC_IN[(i*4) + 2]+registros_MFC_IN[(i*4) + 3]
				self.registrosEscalado_IN.append(registros_MFC)
		except:
			self.registrosEscalado_IN = ['3','3','3','3','3','3','3','3','3','3','3','3','3','3','3','3']

				# Read values MFC (mass flow controller), escalado OUT
		try:
			comandoModbus_MFC_OUT = self.prefijo_lectura + self.registrosMFC1_OUT[0] + '0010'
			checksum_MFC_OUT = self.checkSumCalculation(comandoModbus_MFC_OUT)
			self.s.write(bytes(self.startBit + comandoModbus_MFC_OUT + checksum_MFC_OUT + '\r\n','UTF-8'))
			variablePID_MFC_OUT =  self.s.readline()   # lee serial sv-presentValue

			registros_MFC_OUT =  str(variablePID_MFC_OUT).split(':')[1]
			registros_MFC_OUT = list(registros_MFC_OUT)
			registros_MFC_OUT = registros_MFC_OUT[6::] #Se discriminan los primeros 6 bits (01 direccion, 03 lectura escritura, 0C contador bits)
			for i in range(16):
				registros_MFC = registros_MFC_OUT[i*4]+registros_MFC_OUT[(i*4) + 1]+registros_MFC_OUT[(i*4) + 2]+registros_MFC_OUT[(i*4) + 3]
				self.registrosEscalado_OUT.append(registros_MFC)
		except:
			self.registrosEscalado_OUT = ['3','3','3','3','3','3','3','3','3','3','3','3','3','3','3','3']
		
		return (self.registrosEscalado_IN, self.registrosEscalado_OUT)
	###################################################
	### Hornos Escritura de datos, vista ESCALADO
	###################################################		
	def writeValues_Escalado(self, valorPID, MFC, IN_OUT, X_Y):
			
			# SI LA VARIABLE DE ENTRADA SELECCIONADA FUE IN
			if (MFC=='MFC1' and IN_OUT =='IN'):
			        vectorRegistros = self.registrosMFC1_IN
			if (MFC=='MFC2' and IN_OUT =='IN'):
			        vectorRegistros = self.registrosMFC2_IN			     
			if (MFC=='MFC3' and IN_OUT =='IN'):
			        vectorRegistros = self.registrosMFC3_IN	
			if (MFC=='MFC4' and IN_OUT =='IN'):
			        vectorRegistros = self.registrosMFC4_IN	

			# SI LA VARIABLE DE ENTRADA SELECCIONADA FUE OUT
			if (MFC=='MFC1' and IN_OUT =='OUT'):
			        vectorRegistros = self.registrosMFC1_OUT
			if (MFC=='MFC2' and IN_OUT =='OUT'):
			        vectorRegistros = self.registrosMFC2_OUT			     
			if (MFC=='MFC3' and IN_OUT =='OUT'):
			        vectorRegistros = self.registrosMFC3_OUT
			if (MFC=='MFC4' and IN_OUT =='OUT'):
			        vectorRegistros = self.registrosMFC4_OUT

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

	def checkSumCalculation(self,vectorModbus):
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
