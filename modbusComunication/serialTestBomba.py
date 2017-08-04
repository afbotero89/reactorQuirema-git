#Listar puertos mac, ls /dev/tty.*
#Check sum modbus protocolo (FF-suma-1), FF es 2^8 ---> complemento  a 2 

import serial

s = serial.Serial('/dev/ttyUSB1',38400)

comando = bytes('set units 2\r\n')
s.write(comando)
lectura = s.readline()
lectura1 = s.readline()
print("valor leido", lectura, lectura1)

