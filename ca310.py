'''
En este archivo se realiza la definicion de funciones que se utilizan para trabajar con
el colorimetro ca-210/ca-310


Observaciones:
-Agregar en el archivo de congiguracion la seleccion de canal


'''
import time

import serial                           #Modulo necesario para trabajar con puertos seriales
from configparser import ConfigParser   #Modulo necesario para trabajar con archivos de configuracion

#Lectura de archivo de inicializacion
config_file = ConfigParser()
config_file.read('config.ini')

#Configuracion de puerto serial del colorimetro
ca310 = serial.Serial(
    port=config_file.get('ca310_port_config','port'),
    baudrate=config_file.get('ca310_port_config','baudrate'),
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_TWO,bytesize=serial.SEVENBITS,
    timeout=1)

#b'ER10\rER10\r'


#########################################################################################
#Funcion: ca310_initialization()                                                        #
#Esta funcion realiza la iniciañizacion del colorimetro.                                #
#                                                                                       #
#########################################################################################
def ca310_initialization():
    remote_mode_on_off = "COM,1\r"
    remote_mode_on_off = bytearray(remote_mode_on_off, 'utf-8')
    ca310.write(remote_mode_on_off)
    ca310_buffer_in =ca310.readline()
    if (ca310_buffer_in == b'OK00\r'):
        print("...ca310 remote mode enable")

    sync_mode = "SCS,3\r"           #0:NTSC     1:PAl Mode  2:EXT mode  3:RGB Mode - G Fixed
    sync_mode = bytearray(sync_mode, 'utf-8')
    ca310.write(sync_mode)
    ca310_buffer_in = ca310.readline()
    if (ca310_buffer_in == b'OK00\r'):
        print("...set sync mode ok")

    select_probe = "DPR,1\r"
    select_probe = bytearray(select_probe, 'utf-8')
    ca310.write(select_probe)
    ca310_buffer_in = ca310.readline()
    if (ca310_buffer_in == b'OK00\r'):
        print("...set probe ok")

    channel = 1
    select_channel = "MCH," + str(channel) + "\r"
    select_channel = bytearray(select_channel, 'utf-8')
    ca310.write(select_channel)
    ca310_buffer_in = ca310.readline()
    if (ca310_buffer_in == b'OK00\r'):
        print("...set channel ok")

    select_display_mode = "MDS,0\r"    #0:xyLV_mode     1:T delta uv mode       2:RGB mode - G fixed
                                       #4:RGB mode-R Fixed  5:u' v' Lv mode     6:Flicker meas  7:XYZ mode
    select_display_mode = bytearray(select_display_mode, 'utf-8')
    ca310.write(select_display_mode)
    ca310_buffer_in = ca310.readline()
    if (ca310_buffer_in == b'OK00\r'):
        print("...set display mode ok")


#########################################################################################
#Funcion: ca310_start_calibration()                                                     #
#Esta funcion realiza la calibracion a cero del colorimetro.                            #
#                                                                                       #
#########################################################################################
def ca310_start_calibration():
    ca310.write(b"ZRC\r")
    time.sleep(5)
    ca310_buffer_in =ca310.readline()
    if (ca310_buffer_in == b'OK00\r'):
        print("...calibration a cero ok")



#########################################################################################
#Funcion: ca310_start_calibration()                                                     #
#Esta funcion realiza la calibracion a cero del colorimetro.                            #
#                                                                                       #
#########################################################################################
def ca310_check_calibration():
    ca310.write(b"MES\r")
    ca310_buffer_in =ca310.readline()
    str(ca310_buffer_in)
    calibration_status = ca310_buffer_in[0:2]
    if (calibration_status == b'OK'):
        print("...calibration ok")
    elif(calibration_status == b'ER'):
        print("...error in calibration")
        print("...set probe to 0-CAL and press ENTER keyboard")
        input()
        ca310.write(b"COM,1\r")
        time.sleep(0.5)
        ca310.write(b"ZRC\r")
        print("...zero calibration in process")
        time.sleep(4)
        ca310.write(b"MES\r")
        ca310_buffer_in = ca310.readline()
        str(ca310_buffer_in)
        calibration_status = ca310_buffer_in[0:2]
        if (calibration_status == b'OK'):
            print("...calibration ready")
            print("...set probe to MEAS and press ENTER keyboard")
            input()


#########################################################################################
#Funcion: ca310_measure_xy_L():                                                         #
#Esta funcion devuelve un array con la lectura del los valores x,l y L del colorimetro. #
#                                                                                       #
#########################################################################################

def ca310_measure_xy_L():
    x = b''
    while x == b'':
        ca310.write(b"COM,1\r")
        time.sleep(0.1)
        ca310.reset_input_buffer()
        ca310.write(b"MES\r")
        ca310_buffer_in = ca310.read(23)
        x = ca310_buffer_in[8:11]   # Solo deja en el string el volor corresponidiente a la coordenada x
        y = ca310_buffer_in[13:16]  # Solo deja en el string el volor corresponidiente a la coordenada y
        L = ca310_buffer_in[18:23]  # Solo deja en el string el volor corresponidiente a la Luminancia
    return [int(x), int(y), float(L)]

def ca310_measure_x():
    x = b''
    while x == b'':
        ca310.write(b"COM,1\r")
        time.sleep(0.1)
        ca310.reset_input_buffer()
        ca310.write(b"MES\r")
        ca310_buffer_in = ca310.read(12)
        str(ca310_buffer_in)
        x = ca310_buffer_in[8:11]  # Solo deja en el string el volor corresponidiente a la coordenada x
        print("mesuare x=",x)
    return int(x)

def ca310_measure_y():
    y = b''
    while y == b'':
        ca310.write(b"COM,1\r")
        time.sleep(0.1)
        ca310.reset_input_buffer()
        ca310.write(b"MES\r")
        ca310_buffer_in = ca310.read(17)
        y = ca310_buffer_in[13:16]  # Solo deja en el string el volor corresponidiente a la coordenada y
        print("mesuare y=",y)
    return int(y)

def ca310_measure_L():
    L = b''
    while L == b'':
        ca310.write(b"COM,1\r")
        time.sleep(0.1)
        ca310.reset_input_buffer()
        ca310.write(b"MES\r")
        ca310_buffer_in = ca310.read(23)
        str(ca310_buffer_in)
        L = ca310_buffer_in[18:23]  # Solo deja en el string el volor corresponidiente a la Luminancia
        print("mesuare L=",L)
    return float(L)






#########################################################################################
#Funcion: equation_line(y2,y1,x2,x1,coordinate):                                        #
#Se calcula la pendiente y la ordenada del origen de la ecuacion de la recta para       #
#obtener el valor del registro, que se corresponde con la misma.                        #
#########################################################################################
def equation_line(y2,y1,x2,x1,coordinate):
    m = (y2 - y1) / (x2 - x1)
    b = y1 - (m * x1)
    register = (coordinate - b) / m
    register = int(register)
    return register
