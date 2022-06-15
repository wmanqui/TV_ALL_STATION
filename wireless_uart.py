'''
En este archivo se realiza la definicion de funciones que se utilizan para trabajar con
el dispositivo Wireless Uart
'''
import time

import serial                           #Modulo necesario para trabajar con puertos seriales
from configparser import ConfigParser   #Modulo necesario para trabajar con archivos de configuracion

#Lectura de archivo de inicializacion
config_file = ConfigParser()
config_file.read('config.ini')

#Configuracion de puerto serial de la Wireless Uart
wu = serial.Serial(
    port=config_file.get('wu_port_config','port'),
    baudrate=config_file.get('wu_port_config','baudrate'),
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,
    timeout=0.1)

#Funcion  que permite cambiar el modo de trabajo de la Wireless Uart para poder leer el Active Label
def wu_switch_output_0():
    wu.write(b'\xAA\xAA')
    #wu.write(b'\x00\x00\x00\x00\x00\x00\x00\x00')
    #wu.close()
    #wu_buffer_in=wu.readline()
    #print(wu_buffer_in)
#Funcion  que permite cambiar el modo de trabajo de la Wireless Uart para poder comunicarse con el TV
def wu_switch_output_1():
    wu.write(b'\x02\x53\x02\x07\x00\x5C')
    wu.close()
#Funcion que peromite detectar la presencia de una Wireless UART
def wu_wait_presence_1():
    #wu.reset_input_buffer()
    wu.write(b'\x02\x45\x01\xAC\xF2')
    #time.sleep(0.3)
    wu_buffer_in=wu.readline()
    print(wu_buffer_in)
    if (wu_buffer_in == b'\x00\xac'):
        print("...WU detected")
        status=True
    else:
        print("...WU not detected")
        status=False
    return status
    wu.close()

#Funcion que permite leer una determinada posicion de memoria de la Wireless UART
def wu_al_read_string(address,lenght):
    checksum = 0x52 + 0x02 + address + lenght                          # Calculo de checksum
    checksum = checksum & 0xFF                                         # Operacion AND para eliminar el desbordamiento en el calculo de checksum
    wu.reset_input_buffer()
    time.sleep(0.1)
    wu_cmd = bytearray([0x02, 0x52, 0x02, address, lenght, checksum])  # Encabezado + Address + Lenght + ChecKsum
    wu.write(wu_cmd)
    wu_buffer_in=wu.readline()
    if (wu_buffer_in == b'\x00ok'):
        wu_status= "tv_ok"
    elif (wu_buffer_in == b'\x0092'):
        wu_status= "tv_con_falla"
    elif (wu_buffer_in == b'\x0097'):
        wu_status= "tv_con_falla_wifi"
    elif (wu_buffer_in == b'\x0098'):
        wu_status= "tabla_vacia"
    else:
        wu_status=wu_buffer_in
    return str(wu_status)
    wu.close()

