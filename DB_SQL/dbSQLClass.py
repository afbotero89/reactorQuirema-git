#Listar puertos mac, ls /dev/tty.*
#Check sum modbus protocolo (FF-suma-1), FF es 2^8 ---> complemento  a 2 
import sys
sys.path.append("../modbusComunication")
import modbusClass
import sqlite3

class DataBaseQueries:
	def __init__(self):
		self.conn = sqlite3.connect('parametrosPID.db', check_same_thread=False, timeout=10)
		self.c = self.conn.cursor()
        #Id equipo quiere decir el elemento que selecciono el usuario(Horno 1, 2, 3 o 4, o mantas)
		self.c.execute('''CREATE TABLE IF NOT EXISTS parametros (idEquipo text, tiempoMuestreo text, gananciaProporcional text, gananciaIntegral text, gananciaDerivativa text, direccionControl text, RangoToleranciaError text, LimiteSuperiorIntegral text, valorIntegralAcumulado text, PVAnterior text, limiteSuperiorSalida text, limiteInferiorSalida text, limiteInferiorIntegral text, setValue text, presentValue text)''')
		self.c.execute('''CREATE TABLE IF NOT EXISTS parametrosReactor (idReactor text, SV text, PV text, R text, X text)''')
        
        # Inserta valores iniciales para 4 hornos
		self.instanciaModbus = modbusClass.modbus()

		self.variablesPIDPLC_horno1 = self.instanciaModbus.readRegisterHorno1('horno1')
		self.variablesPIDPLC_horno2 = self.instanciaModbus.readRegisterHorno1('horno2')
		self.variablesPIDPLC_horno3 = self.instanciaModbus.readRegisterHorno1('horno3')
		self.variablesPIDPLC_horno4 = self.instanciaModbus.readRegisterHorno1('horno4')

		#Verifica que los campos ya esten creados, sino es asi los crea con los valores leidos desde el plc
		camposCreados = False
		for row in self.c.execute("SELECT * FROM parametros WHERE `idEquipo`='%s'" % (1)):
		    if(len(row) > 0):
		    	camposCreados = True
		    else:
		    	camposCreados = False

		if camposCreados == False:
			# Inserta valores iniciales para tabla de parametros PID		
			self.c.execute("INSERT INTO parametros VALUES ('1','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (str(self.variablesPIDPLC_horno1[0]),str(self.variablesPIDPLC_horno1[1]),str(self.variablesPIDPLC_horno1[2]),str(self.variablesPIDPLC_horno1[3]),str(self.variablesPIDPLC_horno1[4]),str(self.variablesPIDPLC_horno1[5]),str(self.variablesPIDPLC_horno1[6]),str(self.variablesPIDPLC_horno1[7]),str(self.variablesPIDPLC_horno1[8]),str(self.variablesPIDPLC_horno1[9]),str(self.variablesPIDPLC_horno1[10]),str(self.variablesPIDPLC_horno1[11]),str(self.variablesPIDPLC_horno1[12]),str(self.variablesPIDPLC_horno1[13])))
			self.c.execute("INSERT INTO parametros VALUES ('2','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (str(self.variablesPIDPLC_horno2[0]),str(self.variablesPIDPLC_horno2[1]),str(self.variablesPIDPLC_horno2[2]),str(self.variablesPIDPLC_horno2[3]),str(self.variablesPIDPLC_horno2[4]),str(self.variablesPIDPLC_horno2[5]),str(self.variablesPIDPLC_horno2[6]),str(self.variablesPIDPLC_horno2[7]),str(self.variablesPIDPLC_horno2[8]),str(self.variablesPIDPLC_horno2[9]),str(self.variablesPIDPLC_horno2[10]),str(self.variablesPIDPLC_horno2[11]),str(self.variablesPIDPLC_horno2[12]),str(self.variablesPIDPLC_horno2[13])))
			self.c.execute("INSERT INTO parametros VALUES ('3','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (str(self.variablesPIDPLC_horno3[0]),str(self.variablesPIDPLC_horno3[1]),str(self.variablesPIDPLC_horno3[2]),str(self.variablesPIDPLC_horno3[3]),str(self.variablesPIDPLC_horno3[4]),str(self.variablesPIDPLC_horno3[5]),str(self.variablesPIDPLC_horno3[6]),str(self.variablesPIDPLC_horno3[7]),str(self.variablesPIDPLC_horno3[8]),str(self.variablesPIDPLC_horno3[9]),str(self.variablesPIDPLC_horno3[10]),str(self.variablesPIDPLC_horno3[11]),str(self.variablesPIDPLC_horno3[12]),str(self.variablesPIDPLC_horno3[13])))
			self.c.execute("INSERT INTO parametros VALUES ('4','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (str(self.variablesPIDPLC_horno4[0]),str(self.variablesPIDPLC_horno4[1]),str(self.variablesPIDPLC_horno4[2]),str(self.variablesPIDPLC_horno4[3]),str(self.variablesPIDPLC_horno4[4]),str(self.variablesPIDPLC_horno4[5]),str(self.variablesPIDPLC_horno4[6]),str(self.variablesPIDPLC_horno4[7]),str(self.variablesPIDPLC_horno4[8]),str(self.variablesPIDPLC_horno4[9]),str(self.variablesPIDPLC_horno4[10]),str(self.variablesPIDPLC_horno4[11]),str(self.variablesPIDPLC_horno4[12]),str(self.variablesPIDPLC_horno4[13])))
			
			# Inserta valores iniciales para parametros de hornos (setValue, presentValue, rampa, X)
			self.c.execute("INSERT INTO parametrosReactor VALUES ('1','%s','%s','%s','%s')" % ('-','-','-','-'))
			self.c.execute("INSERT INTO parametrosReactor VALUES ('2','%s','%s','%s','%s')" % ('-','-','-','-'))
			self.c.execute("INSERT INTO parametrosReactor VALUES ('3','%s','%s','%s','%s')" % ('-','-','-','-'))
			self.c.execute("INSERT INTO parametrosReactor VALUES ('4','%s','%s','%s','%s')" % ('-','-','-','-'))
		else:
			pass
		self.conn.commit()

	# Valores PID del reactor: lectura - escritura
	def update_PID_Data(self, newValue, variablePID, horno_manta_seleccionada):		
		id_elemento = 1
		if horno_manta_seleccionada == 'horno1':
		    id_elemento = 1
		elif horno_manta_seleccionada == 'horno2':
		    id_elemento = 2
		elif horno_manta_seleccionada == 'horno3':
		    id_elemento = 3
		elif horno_manta_seleccionada == 'horno4':
		    id_elemento = 4

		sqlSentence = "UPDATE `parametros` SET" + " " + str(variablePID) + "= '%s' WHERE `idEquipo`='%s'" % (newValue,str(id_elemento))
		self.c.execute(sqlSentence)
		self.conn.commit() 

	def get_PID_Data(self, horno_manta_seleccionada):
	    id_elemento = 1
	    if horno_manta_seleccionada == 'horno1':
	        id_elemento = 1
	    elif horno_manta_seleccionada == 'horno2':
	        id_elemento = 2
	    elif horno_manta_seleccionada == 'horno3':
	        id_elemento = 3
	    elif horno_manta_seleccionada == 'horno4':
	        id_elemento = 4 
	    for row in self.c.execute("SELECT * FROM parametros WHERE `idEquipo`='%s'" % (id_elemento)):
	        row = row
	    return row

	# Lectura escritura reactor hornos: Set value (SV), present value (PV), rampa (R), x: por definir (X)
	def update_variables_Hornos(self, newValue, variable, horno_seleccionado):
		id_elemento = 1
		if horno_seleccionado == 'horno1':
		    id_elemento = 1
		elif horno_seleccionado == 'horno2':
		    id_elemento = 2
		elif horno_seleccionado == 'horno3':
		    id_elemento = 3
		elif horno_seleccionado == 'horno4':
		    id_elemento = 4

		sqlSentence = "UPDATE `parametrosReactor` SET" + " " + str(variable) + "= '%s' WHERE `idReactor`='%s'" % (newValue,str(id_elemento))
		self.c.execute(sqlSentence)
		self.conn.commit() 

	def get_hornos_Data(self):
		for row1 in self.c.execute("SELECT * FROM parametrosReactor WHERE `idReactor`='%s'" % (1)):
		    datosHorno1 = row1
		for row2 in self.c.execute("SELECT * FROM parametrosReactor WHERE `idReactor`='%s'" % (2)):
		    datosHorno2 = row2
		for row3 in self.c.execute("SELECT * FROM parametrosReactor WHERE `idReactor`='%s'" % (3)):
		    datosHorno3 = row3
		for row4 in self.c.execute("SELECT * FROM parametrosReactor WHERE `idReactor`='%s'" % (4)):
		    datosHorno4 = row4
		return (row1, row2, row3, row4)



