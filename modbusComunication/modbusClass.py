#Listar puertos mac, ls /dev/tty.*
#Check sum modbus protocolo (FF-suma-1), FF es 2^8 ---> complemento  a 2 
import minimalmodbus
import serial

class modbus:
	def __init__(self):
		try:
			self.instrument = minimalmodbus.Instrument('/dev/ttyUSB0',1,minimalmodbus.MODE_ASCII)
			self.instrument.serial.baudrate = 9600
			self.instrument.serial.bytesize = 7
			self.instrument.serial.parity = serial.PARITY_EVEN
			self.instrument.serial.stopbits = 1
			self.instrument.serial._ASCII_FOOTER = "\r\n"

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

			pidH1=4506
			pidH2=4536
			pidH3=4556
			pidH4=4576

			self.vectorRegistrosHorno1 = [pidH1, pidH1 + 1, pidH1 + 2, pidH1 + 3, pidH1 + 4, pidH1 + 5, pidH1 + 6, pidH1 + 7, pidH1 + 8, pidH1 + 9, pidH1 + 10, pidH1 + 12, 4125, 4124, 4526]
			self.vectorRegistrosHorno2 = [pidH2, pidH2 + 1, pidH2 + 2, pidH2 + 3, pidH2 + 4, pidH2 + 5, pidH2 + 6, pidH2 + 7, pidH2 + 8, pidH2 + 9, pidH2 + 10, pidH2 + 12, 4135, 4134, 4529]
			self.vectorRegistrosHorno3 = [pidH3, pidH3 + 1, pidH3 + 2, pidH3 + 3, pidH3 + 4, pidH3 + 5, pidH3 + 6, pidH3 + 7, pidH3 + 8, pidH3 + 9, pidH3 + 10, pidH3 + 12, 4145, 4144, 4532]
			self.vectorRegistrosHorno4 = [pidH4, pidH4 + 1, pidH4 + 2, pidH4 + 3, pidH4 + 4, pidH4 + 5, pidH4 + 6, pidH4 + 7, pidH4 + 8, pidH4 + 9, pidH4 + 10, pidH4 + 12, 4155, 4154, 4596]
			
		except:
			print("error en la conexion con el plc")

	################################################
	### Hornos lecturas de datos, vista variables PID
	################################################
	def readRegisterHorno1(self, horno_manta_seleccionada):
		print("horno=",horno_manta_seleccionada)
		try:
			
			if (horno_manta_seleccionada=='horno1'):
				vectorRegistros = self.vectorRegistrosHorno1
			elif(horno_manta_seleccionada=='horno2'):
				vectorRegistros = self.vectorRegistrosHorno2
			elif(horno_manta_seleccionada=='horno3'):
				vectorRegistros = self.vectorRegistrosHorno3
			elif(horno_manta_seleccionada=='horno4'):
				vectorRegistros = self.vectorRegistrosHorno4

			tiempoMuestreo = self.instrument.read_register(vectorRegistros[0],1)
			gananciaProporcional = self.instrument.read_register(vectorRegistros[1],1)
			gananciaIntegral = self.instrument.read_register(vectorRegistros[2],1)
			gananciaDerivativa = self.instrument.read_register(vectorRegistros[3],1)
			direccionDeControl = self.instrument.read_register(vectorRegistros[4],1)
			rangoToleranciaError = self.instrument.read_register(vectorRegistros[5],1)
			limiteSuperiorSalida = self.instrument.read_register(vectorRegistros[6],1)
			limiteInferiorSalida = self.instrument.read_register(vectorRegistros[7],1)
			limiteSuperiorIntegral = self.instrument.read_register(vectorRegistros[8],1)
			limiteInferiorIntegral = self.instrument.read_register(vectorRegistros[9],1)
			valorIntegralAcumulado = self.instrument.read_register(vectorRegistros[10],1)
			PVAnterior = self.instrument.read_register(vectorRegistros[11],1)
			setValue = self.instrument.read_register(vectorRegistros[12],1)
			presentValue = self.instrument.read_register(vectorRegistros[13],1)
			GPWMValue = self.instrument.read_register(vectorRegistros[14],1)

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
		



	
	###################################################
	### Hornos Escritura de datos, vista variables PID
	###################################################	
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
			return ('--','--')


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
