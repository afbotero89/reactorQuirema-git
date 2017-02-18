#Listar puertos mac, ls /dev/tty.*
#Check sum modbus protocolo (FF-suma-1), FF es 2^8 ---> complemento  a 2 
import minimalmodbus
import serial
instrument = minimalmodbus.Instrument('/dev/ttyUSB0',1,minimalmodbus.MODE_ASCII)
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 7
instrument.serial.parity = serial.PARITY_EVEN
instrument.serial.stopbits = 1

#value = instrument.read_register(6281,1)
pidH1=4506
numeroDeDecimales = 0
tiempoMuestreo = instrument.read_register(pidH1,numeroDeDecimales)
gananciaProporcional = instrument.read_register(pidH1 + 1,numeroDeDecimales)
gananciaIntegral = instrument.read_register(pidH1 + 2,numeroDeDecimales)
gananciaDerivativa = instrument.read_register(pidH1 + 3,numeroDeDecimales)
direccionDeControl = instrument.read_register(pidH1 + 4,numeroDeDecimales)
rangoToleranciaError = instrument.read_register(pidH1 + 5,numeroDeDecimales)
limiteSuperiorSalida = instrument.read_register(pidH1 + 6,numeroDeDecimales)
limiteInferiorSalida = instrument.read_register(pidH1 + 7,numeroDeDecimales)
limiteSuperiorIntegral = instrument.read_register(pidH1 + 8,numeroDeDecimales)
limiteInferiorIntegral = instrument.read_register(pidH1 + 9,numeroDeDecimales)
valorIntegralAcumulado = instrument.read_register(pidH1 + 10,numeroDeDecimales)
pvAnterior = instrument.read_register(pidH1 + 12,numeroDeDecimales)
setValue = instrument.read_register(4124,numeroDeDecimales)
presentValue = instrument.read_register(4125,numeroDeDecimales)
gpwm = instrument.read_register(4526,numeroDeDecimales)
#print(value)
#instrument.write_register(1556,25,1)
#value = instrument.read_register(4096,1)
#instrument.serial.
#7bits
#bauterate=9600
#bytesize = 7 
#stopbits = 1

#print(instrument)
print(tiempoMuestreo,gananciaProporcional,gananciaIntegral,gananciaDerivativa,direccionDeControl,rangoToleranciaError, limiteSuperiorSalida, limiteInferiorSalida,limiteSuperiorIntegral,limiteInferiorIntegral,valorIntegralAcumulado,pvAnterior,setValue,presentValue,gpwm)
# (valores iniciales 400 573 1280 65456 4 0 4000 0 0 0 8704 1028 223 0 4000)
