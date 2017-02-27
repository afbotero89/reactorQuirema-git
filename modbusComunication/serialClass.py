#Listar puertos mac, ls /dev/tty.*
#Check sum modbus protocolo (FF-suma-1), FF es 2^8 ---> complemento  a 2 
import serial

class modbus:
	def __init__(self):
		try:
			self.s = serial.Serial('/dev/ttyUSB0',9600)
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
			print("init serial")
		except:
			print("error en la conexion con el plc")

	################################################
	### Hornos lecturas de datos, vista variables PID
	################################################
	def readRegisterHorno1(self, horno_manta_seleccionada):
		print("horno=",horno_manta_seleccionada)
		try:
			if (horno_manta_seleccionada=='horno1'):
				vectorRegistros = self.vectorRegistrosHorno1_Hex
			elif(horno_manta_seleccionada=='horno2'):
				vectorRegistros = self.vectorRegistrosHorno2_Hex
			elif(horno_manta_seleccionada=='horno3'):
				vectorRegistros = self.vectorRegistrosHorno3_Hex
			elif(horno_manta_seleccionada=='horno4'):
				vectorRegistros = self.vectorRegistrosHorno4_Hex

			prefijo = ':0103'
			sufijo = '000150\r\n'
			self.s.write(bytes(prefijo + str(self.vectorRegistros[0].split('x')[1]) + sufijo,'UTF-8'))
			tiempoMuestreo = self.s.read(14)
			self.s.write(bytes(prefijo + str(self.vectorRegistros[1].split('x')[1]) + sufijo,'UTF-8'))
			gananciaProporcional = self.s.read(14)
			self.s.write(bytes(prefijo + str(self.vectorRegistros[2].split('x')[1]) + sufijo,'UTF-8'))
			gananciaIntegral = self.s.read(14)
			self.s.write(bytes(prefijo + str(self.vectorRegistros[3].split('x')[1]) + sufijo,'UTF-8'))
			gananciaDerivativa = self.s.read(14)
			self.s.write(bytes(prefijo + str(self.vectorRegistros[4].split('x')[1]) + sufijo,'UTF-8'))
			direccionDeControl = self.s.read(14)
			self.s.write(bytes(prefijo + str(self.vectorRegistros[5].split('x')[1]) + sufijo,'UTF-8'))
			rangoToleranciaError = self.s.read(14)
			self.s.write(bytes(prefijo + str(self.vectorRegistros[6].split('x')[1]) + sufijo,'UTF-8'))
			limiteSuperiorSalida = self.s.read(14)
			self.s.write(bytes(prefijo + str(self.vectorRegistros[7].split('x')[1]) + sufijo,'UTF-8'))
			limiteInferiorSalida = self.s.read(14)
			self.s.write(bytes(prefijo + str(self.vectorRegistros[8].split('x')[1]) + sufijo,'UTF-8'))
			limiteSuperiorIntegral = self.s.read(14)
			self.s.write(bytes(prefijo + str(self.vectorRegistros[9].split('x')[1]) + sufijo,'UTF-8'))
			limiteInferiorIntegral = self.s.read(14)
			self.s.write(bytes(prefijo + str(self.vectorRegistros[10].split('x')[1]) + sufijo,'UTF-8'))
			valorIntegralAcumulado = self.s.read(14)
			self.s.write(bytes(prefijo + str(self.vectorRegistros[11].split('x')[1]) + sufijo,'UTF-8'))
			PVAnterior = self.s.read(14)
			self.s.write(bytes(prefijo + str(self.vectorRegistros[12].split('x')[1]) + sufijo,'UTF-8'))
			setValue = self.s.read(14)
			self.s.write(bytes(prefijo + str(self.vectorRegistros[13].split('x')[1]) + sufijo,'UTF-8'))
			presentValue = self.s.read(14)
			self.s.write(bytes(prefijo + str(self.vectorRegistros[14].split('x')[1]) + sufijo,'UTF-8'))
			GPWMValue = self.s.read(14)

			return (tiempoMuestreo,
					gananciaProporcional,
					gananciaIntegral,
					gananciaDerivativa,
					direccionDeControl,
					rangoToleranciaError,
					limiteSuperiorSalida,
					limiteInferiorSalida,
					limiteSuperiorIntegral,
					limiteInferiorIntegral,
					valorIntegralAcumulado,
					PVAnterior,
					setValue,
					presentValue,
					GPWMValue)
			
		except:
			
			return ('--','--','--','--','--','--','--','--','--','--','--','--','--','--','--')

	###################################################
	### Hornos Escritura de datos, vista variables PID
	###################################################		
	def writeValuesPID(self, valorPID, variablePID, horno_mantaSeleccionada):

		try:
			print('horno seleccionadoX=',horno_mantaSeleccionada)
			if (horno_mantaSeleccionada=='horno1'):
			        vectorRegistros = self.vectorRegistrosHorno1
			elif(horno_mantaSeleccionada=='horno2'):
			        vectorRegistros = self.vectorRegistrosHorno2
			elif(horno_mantaSeleccionada=='horno3'):
			        vectorRegistros = self.vectorRegistrosHorno3
			elif(horno_mantaSeleccionada=='horno4'):
			        vectorRegistros = self.vectorRegistrosHorno4

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

			self.instrument.write_register(registro,valorPID,1)
		except:
			print("error de escritura")
	
	######################################################
	### Hornos Escritura de datos, vista variables PID ###
	######################################################	
	def read_variablesVistaReactor(self):
		try:
			setValue_Horno1 = self.instrument.read_register(self.vectorRegistrosHorno1[12],1)
			presentValue_Horno1 = self.instrument.read_register(self.vectorRegistrosHorno1[13],1)

			setValue_Horno2 = self.instrument.read_register(self.vectorRegistrosHorno2[12],1)
			presentValue_Horno2 = self.instrument.read_register(self.vectorRegistrosHorno2[13],1)

			setValue_Horno3 = self.instrument.read_register(self.vectorRegistrosHorno3[12],1)
			presentValue_Horno3 = self.instrument.read_register(self.vectorRegistrosHorno3[13],1)

			setValue_Horno4 = self.instrument.read_register(self.vectorRegistrosHorno4[12],1)
			presentValue_Horno4 = self.instrument.read_register(self.vectorRegistrosHorno4[13],1)
		
			#rampa_Horno1 = self.instrument.read_register(self.vectorRegistrosHorno1[13],1)
			#X_Horno1 = self.instrument.read_register(self.vectorRegistrosHorno1[13],1)
			return (setValue_Horno1,
                                presentValue_Horno1,
                                setValue_Horno2,
                                presentValue_Horno2,
                                setValue_Horno3,
                                presentValue_Horno3,
                                setValue_Horno4,
                                presentValue_Horno4)
		except:
			return ('--','--','--','--','--','--','--','--')


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

	def checkSumCalculation(modbusCommand):
		modbusCommand = ':0103119A000150\r\n'
		vectorModbus = list(modbusCommand)[1:len(modbusCommand)-2]
		checkSum = int('FF',16) - (int(vectorModbus[0] + vectorModbus[1],16) + int(vectorModbus[2] + vectorModbus[3],16) + int(vectorModbus[4] + vectorModbus[5],16) + int(vectorModbus[6] + vectorModbus[7],16) + int(vectorModbus[8] + vectorModbus[9],16) + int(vectorModbus[10] + vectorModbus[11],16)) + 1
		return modbusCommand
		print(modbusCommand)
