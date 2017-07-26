#Listar puertos mac, ls /dev/tty.*
#Check sum modbus protocolo (FF-suma-1), FF es 2^8 ---> complemento  a 2 

import serial

s = serial.Serial('/dev/tty.usbserial-AL013DE4',38400)

comando = bytes('help\r\n','UTF-8')
s.write(comando)
lectura = s.readline()
print("valor leido", lectura)

