#Listar puertos mac, ls /dev/tty.*
#Check sum modbus protocolo (FF-suma-1), FF es 2^8 ---> complemento  a 2 
import sys
sys.path.append("../modbusComunication")
import modbusClass
import sqlite3

class DataBaseQueries:
	def __init__(self):
		self.conn = sqlite3.connect('alarmas.db', check_same_thread=False, timeout=10)
		self.c = self.conn.cursor()
        #Id equipo quiere decir el elemento que selecciono el usuario(Horno 1, 2, 3 o 4, o mantas)
		self.c.execute('''CREATE TABLE IF NOT EXISTS alarmasActuales (id text, tempMantas text, tempHorno1 text, tempHorno2 text, tempHorno3 text, tempHorno4 text)''')
        
		#Verifica que los campos ya esten creados, sino es asi los crea con los valores leidos desde el plc
		camposCreados = False
		for row in self.c.execute("SELECT * FROM alarmasActuales WHERE `id`='%s'" % (1)):
		    if(len(row) > 0):
		    	camposCreados = True
		    else:
		    	camposCreados = False

		if camposCreados == False:
			# Inserta valores iniciales para tabla de alarmas (id, mantas, horno1, horno2, horno3, horno4)		
			self.c.execute("INSERT INTO alarmasActuales VALUES ('1','%s','%s','%s','%s','%s')" % ('-','-','-','-','-'))

		else:
			pass
		self.conn.commit()

	# Modifica alarma
	def update_alarma(self, newValue, alamaSeleccionada):		

		sqlSentence = "UPDATE `alarmasActuales` SET" + " " + str(alamaSeleccionada) + "= '%s' WHERE `id`='1'" % (newValue)
		self.c.execute(sqlSentence)
		self.conn.commit() 

	def get_PID_Data(self):
	    for row in self.c.execute("SELECT * FROM alarmasActuales WHERE `id`='1'"):
	        row = row
	    return row




