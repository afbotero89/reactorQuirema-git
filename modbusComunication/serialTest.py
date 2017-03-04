#Listar puertos mac, ls /dev/tty.*
#Check sum modbus protocolo (FF-suma-1), FF es 2^8 ---> complemento  a 2 

import serial

modbusCommand = '01061192004E2'
startBit = ':'
stopbits = '\r\n'

vectorModbus = list(modbusCommand)
print(vectorModbus)
checkSum = int('FF',16) - (int(vectorModbus[0] + vectorModbus[1],16) + int(vectorModbus[2] + vectorModbus[3],16) + int(vectorModbus[4] + vectorModbus[5],16) + int(vectorModbus[6] + vectorModbus[7],16) + int(vectorModbus[8] + vectorModbus[9],16) + int(vectorModbus[10] + vectorModbus[11],16)) + 1
#print('FF',vectorModbus[0] + vectorModbus[1], vectorModbus[2] + vectorModbus[3], vectorModbus[4] + vectorModbus[5], vectorModbus[6] + vectorModbus[7], vectorModbus[8] + vectorModbus[9], vectorModbus[10] + vectorModbus[11])
print(checkSum)
print(hex(checkSum))
checkSum = hex(checkSum).split('x')[1]
#print(checkSum)

#completeModbusCommand = startBit + modbusCommand + checkSum + stopbits
#print(completeModbusCommand)

s = serial.Serial('/dev/tty.SLAB_USBtoUART',9600)
s.bytesize = 7
s.parity = serial.PARITY_EVEN
s.stopbits = 1

#s.write(bytes(':010611C2004E2' + 'FF' + '\r\n','UTF-8'))
#tiempoMuestreo = s.read(11)
#print(tiempoMuestreo)
comando = bytes(':0106119A004FF2\r\n','UTF-8')
s.write(comando)
lectura = s.readline()
print(lectura, comando)
if (lectura==comando):
	print('iguales')