#Listar puertos mac, ls /dev/tty.*
#Check sum modbus protocolo (FF-suma-1), FF es 2^8 ---> complemento  a 2 

import serial

s = serial.Serial('/dev/tty.usbserial-AL013DE4',9600)

comando = bytes('help','UTF-8')
s.write(comando)
lectura = s.read(10)
print(lectura)

