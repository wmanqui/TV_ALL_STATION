'''
En este archivo se realiza la definicion de funciones para trabajar con FIT-6
Ultima Modificion: 29-03-22
    -v1.1: Se modifico la funcion que activa los bits de salida
'''
import time

import serial                           #Modulo necesario para trabajar con puertos seriales
from configparser import ConfigParser   #Modulo necesario para trabajar con archivos de configuracion

#Lectura de archivo de inicializacion
config_file = ConfigParser()
config_file.read('config.ini')

# Configuracion de puerto serial de Fit-6
fit6 = serial.Serial(
    port=config_file.get('fit6_port_config','port'),
    baudrate=config_file.get('fit6_port_config','baudrate'),
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,
    timeout=1)

def fit6_test_connection():		#Permite verificar que hay comunicacion con el fit-6.
    fit6.write(b'\x02\x49\x00\x49')
    fit6_buffer_in=fit6.readline()
    if (fit6_buffer_in == b'\x00\x00'):
        #print("...Succefull connection with Fit-6")
        return("Connection Successful")
    else:
        #print("...Connection Failed with Fit-6")
        return("Connection Failed")

########################################################
#Funcion: fit6_logic_out(bit,level,retest):                                                                             	#
#Setea los bits de salida del fit-6.                                                                                		#
#Los argumentos son:bit(0-3),level(0,1),retest(cantidad de reintentos del comando)      	#
########################################################

def fit6_logic_out(bit,level,retest):
    while(retest>=1):
        if(bit==0 and level ==1):
            fit6.write(b'\x02\x42\x02\x00\x01\x45')
        if(bit==0 and level == 0):
            fit6.write(b'\x02\x42\x02\x00\x00\x44')
        if(bit==1 and level == 1):
            fit6.write(b'\x02\x42\x02\x01\x01\x46')
        if(bit==1 and level == 0):
            fit6.write(b'\x02\x42\x02\x01\x00\x45')
        if(bit==2 and level == 1):
            fit6.write(b'\x02\x42\x02\x02\x01\x47')
        if(bit==2 and level == 0):
            fit6.write(b'\x02\x42\x02\x02\x00\x46')
        if(bit==3 and level == 1):
            fit6.write(b'\x02\x42\x02\x03\x01\x48')
        if(bit==3 and level == 0):
            fit6.write(b'\x02\x42\x02\x03\x00\x47')

        fit6_buffer_in=fit6.readline()
        if (fit6_buffer_in == b'\x00'):
            bit_status="ok"
            retest=0
        else:
            bit_status="error"
            retest-=1
    return bit_status



########################################################
#Funcion: fit6_read_input():                         		                                                    	#
#Lee los bis de entrada del dispositivo fit-6.                                                               		#
#																		      	#
########################################################


def fit6_read_input():
    fit6.write(b'\x02\x49\x00\x49')
    fit6_buffer_in=fit6.readline()
    if (fit6_buffer_in == b'\x00\x00'):
        print("...all_input: OFF")
    elif(fit6_buffer_in == b'\x00\x01'):
        print("...Input_0: ON")
    elif (fit6_buffer_in == b'\x00\x02'):
        print("...Input_1: ON")
    elif (fit6_buffer_in == b'\x00\x03'):
        print("...Input_0: ON")
        print("...Input_1: ON")
    elif (fit6_buffer_in == b'\x00\x04'):
        print("...Input_2: ON")
    elif (fit6_buffer_in == b'\x00\x05'):
        print("...Input_0: ON")
        print("...Input_2: ON")
    elif (fit6_buffer_in == b'\x00\x06'):
        print("...Input_1: ON")
        print("...Input_2: ON")
    elif (fit6_buffer_in == b'\x00\x07'):
        print("...Input_0: ON")
        print("...Input_1: ON")
        print("...Input_2: ON")
    elif (fit6_buffer_in == b'\x00\x08'):
        print("...Input_3: ON")
    elif (fit6_buffer_in == b'\x00\t'):
        print("...Input_0: ON")
        print("...Input_3: ON")
    elif (fit6_buffer_in == b'\x00\n'):
        print("...Input_1: ON")
        print("...Input_3: ON")
    elif (fit6_buffer_in == b'\x00\x0b'):
        print("...Input_0: ON")
        print("...Input_1: ON")
        print("...Input_3: ON")
    elif (fit6_buffer_in == b'\x00\x0c'):
        print("...Input_2: ON")
        print("...Input_3: ON")
    elif (fit6_buffer_in == b'\x00\r'):
        print("...Input_0: ON")
        print("...Input_2: ON")
        print("...Input_3: ON")
    elif (fit6_buffer_in == b'\x00\x0e'):
        print("...Input_1: ON")
        print("...Input_2: ON")
        print("...Input_3: ON")
    elif (fit6_buffer_in == b'\x00\x0f'):
        print("...Input_0: ON")
        print("...Input_1: ON")
        print("...Input_2: ON")
        print("...Input_3: ON")




########################################################
#Funcion: fit6_read_input():                         		                                                    	#
#Lee los bis de entrada del dispositivo fit-6.                                                               		#
#																		      	#
########################################################
def fit6_send_RC6_command(system,data):
    checksum = 0x52 + 0x04 + 0x40 + 0x16 + system + data    #Calculo de checksum
    checksum = checksum & 0xFF  #Operacion AND para eliminar el desbordamiento en el calculo de checksum
    rc6_cmd =bytearray([0x02, 0x52, 0x04, 0x40, 0x16, system, data,checksum])  # Encabezado + System + Data
    fit6.write(rc6_cmd)
    fit6_buffer_in = fit6.readline()
    if (fit6_buffer_in == b'\x00'):
        print("...RC6 command received")
    else:
        print("...command error")
