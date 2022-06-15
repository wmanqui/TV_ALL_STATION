
import time
import serial

#from arduino import*
from fit6 import*
from wireless_uart import*
#from rc6_command import*
from uart_command import*
from ca310 import*
import numpy as np


#Codigo de PE08: Ajuste de Blanco
samples= 40

#file_rgb = 'rgb_register_50_7406.txt'
#file_rgb = 'rgb_register_55_7406.txt'
#file_rgb = 'rgb_register_75_8516.txt'
#file_rgb = 'rgb_register_65_7906.txt'
file_rgb = 'rgb_register_32_6927.txt'

fdatos = open(file_rgb, 'a')  #Si no existe el archivo con los registros rgb, genera uno
fdatos.close()

with open(file_rgb) as myfile:
    total_lines = sum(1 for line in myfile) #Determina la cantidad de lineas q tiene "rgb_register.txt""

tft_white_check=ca310_measure_L()
while tft_white_check <= 30:
    print("Pantalla sin campo blanco")
    uart_white_initialization_commands_MT9675()
    tft_white_check = ca310_measure_L()
print("Aparato preparado iniciando ajuste")

if total_lines == samples:
    print("AJUSTE POR PROMEDIO")
    set_and_check_white_register(313,329,287,296,276,282,3)
else:
    print("AJUSTE POR CURVA")
    curve_alignment_MT9675(file_rgb)
    average_register(file_rgb)
#uart_close_internal_pattern_mode_2k21(100)










