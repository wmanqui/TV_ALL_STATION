'''
En este archivo se realiza la definicion de funciones que se utilizan para trabajar con
el dispositivo Wireless Uart
'''
import time
import serial                           #Modulo necesario para trabajar con puertos seriales
from configparser import ConfigParser   #Modulo necesario para trabajar con archivos de configuracion
from wireless_uart import*
from ca310 import*

#Lectura de archivo de inicializacion
config_file = ConfigParser()
config_file.read('config.ini')

def uart_mt5800_head(delay_ms):
    wu.write(b'\x81\x82\x83\x82\x81')
    time.sleep(delay_ms/1000)

def uart_mtk9675_head(delay_ms):
    wu.write(b'\x03\x69\x6E\x70\x75\x74\x20\x6B\x65\x79\x65\x76\x65\x6E\x74\x20\x32\x30\x39\x0A')
    time.sleep(delay_ms/1000)

def uart_enter_factory():
    #wu.reset_input_buffer()
    wu.write(b'\x6E\x51\x86\x03\xFE\xE1\xA0\x00\x01\x04')
    #codigo de respuesta del tv anulado en forma momentanea
    '''
    tv = wu.readline()
    if tv != b'':
        print("tv_factory_mode: ok")
    else:
        print("tv_factory_mode: failed")
    '''


def uart_exit_factory_mode(delay_ms):
    wu.write(b'\x6E\x51\x86\x03\xFE\xE1\xA0\x00\x00\x05')
    time.sleep(delay_ms/1000)

def uart_set_burnin_mode(On_Off):
    #wu.reset_input_buffer()
    if (On_Off == 1):
        wu.write(b'\x6E\x51\x86\x03\xFE\xE1\xA2\x00\x01\x06')
    elif (On_Off == 0):
        wu.write(b'\x6E\x51\x86\x03\xFE\xE1\xA2\x00\x00\x07')
    #codigo de respuesta del tv anulado en forma momentanea
    ''' 
        tv = wu.readline()
        if tv != b'':
            print("set burnin mode: ok")
        else:
            print("set burnin mode: failed")
            input()
    #time.sleep(delay_ms / 1000)
    '''

def uart_change_hdmi():
    #wu.reset_input_buffer()
    wu.write(b'\x6E\x51\x86\x03\xFE\x60\x00\x23\x02\x05')
    #codigo de respuesta del tv anulado en forma momentanea
    '''
    tv = wu.readline()
    if tv != b'':
        print("change_hdmi: ok")
    else:
        print("change_hdmi: failed")
        input()
    #time.sleep(delay_ms/1000)
    '''



#Comandos para trabajar en estacion de ajuste de blanco:

def uart_open_internal_pattern_mode():
    #wu.reset_input_buffer()
    wu.write(b'\x6E\x51\x86\x03\xFE\xE1\xA8\x00\x01\x0C')
    #codigo de respuesta del tv anulado en forma momentanea
    '''
    tv = wu.readline()
    if tv != b'':
        print("open_internal_pattern_mode: ok")
    else:
        print("open_internal_pattern_mode: failed")
        input()
    #time.sleep(delay_ms/1000)
    '''

def uart_80_white_pattern():
    #wu.reset_input_buffer()
    wu.write(b'\x6E\x51\x87\x03\xFE\x74\x05\x00\x03\x32\x05')
    #codigo de respuesta del tv anulado en forma momentanea
    '''
    tv = wu.readline()
    if tv != b'':
        print("uart_80_white_pattern: ok")
    else:
        print("ouart_80_white_pattern: failed")
        input()
    #time.sleep(delay_ms/1000)
    '''

def uart_white_pattern_off(delay_ms):
    wu.write(b'\x6E\x51\x86\x03\xFE\xE1\xA8\x00\x00\x0D')
    time.sleep(delay_ms/1000)

def uart_set_warm_color_temp_2k21(delay_ms):
    wu.write(b'\x6E\x51\x86\x03\xFE\x14\x05\x23\x01\x77')
    time.sleep(delay_ms/1000)

def uart_close_internal_pattern_mode_2k21(delay_ms):
    wu.write(b'\x6E\x51\x86\x03\xFE\xE1\xA8\x00\x00\x0D')
    time.sleep(delay_ms/1000)

def uart_set_normal_color_temp_2k21(delay_ms):
    wu.write(b'\x6E\x51\x86\x03\xFE\x14\x05\x23\x01\x77')
    time.sleep(delay_ms/1000)

def uart_set_cool_color_temp_2k21(delay_ms):
    wu.write(b'\x6E\x51\x86\x03\xFE\x14\x0A\x23\x01\x78')
    time.sleep(delay_ms/1000)

def uart_save_warm_temperature_data_2k21(delay_ms):
    wu.write(b'\x6E\x51\x86\x03\xFE\x14\x05\x23\x00\x76')
    time.sleep(delay_ms/1000)

def uart_save_normal_temperature_data_2k21(delay_ms):
    wu.write(b'\x6E\x51\x86\x03\xFE\x14\x06\x23\x00\x75')
    time.sleep(delay_ms/1000)

def uart_save_cool_temperature_data_2k21(delay_ms):
    wu.write(b'\x6E\x51\x86\x03\xFE\x14\x0A\x23\x00\x79')
    time.sleep(delay_ms/1000)

def uart_switch_warm(delay_ms):
    wu.write(b'\x6E\x51\x86\x03\xFE\x14\x05\x00\x01\x54')
    time.sleep(delay_ms/1000)

def uart_switch_normal(delay_ms):
    wu.write(b'\x6E\x51\x86\x03\xFE\x14\x06\x00\x01\x57')
    time.sleep(delay_ms/1000)

def uart_switch_cool(delay_ms):
    wu.write(b'\x6E\x51\x86\x03\xFE\x14\x0A\x00\x01\x5B')
    time.sleep(delay_ms/1000)

def uart_save_warm_rgb(delay_ms):
    wu.write(b'\x6E\x51\x86\x03\xFE\x14\x05\x00\x00\x55')
    time.sleep(delay_ms/1000)

def uart_save_normal_rgb(delay_ms):
    wu.write(b'\x6E\x51\x86\x03\xFE\x14\x06\x00\x01\x57')
    time.sleep(delay_ms/1000)

def uart_save_cool_rgb(delay_ms):
    wu.write(b'\x6E\x51\x86\x03\xFE\x14\x0A\x00\x00\x5A')
    time.sleep(delay_ms/1000)




def uart_set_r_register(r_register,delay_ms):
    r_lbyte = r_register & 0x00FF   #Elimina la parte del alta del byte
    r_hbyte = r_register & 0xFF00   #Deja en 0 la parte baja del byte
    r_hbyte = r_hbyte >> 8          #Realiza desplazamiento para dejar solo el valor del parte alta
    checksum = 0x6E^0x51^0x86^0x03^0xFE^0x16^0x00^r_hbyte^r_lbyte    #Calculo de checksum
    checksum = checksum & 0xFF  #Operacion AND para eliminar el desbordamiento en el calculo de checksum
    r_register_cmd =bytearray([0x6E, 0x51, 0x86, 0x03, 0xFE, 0x16, 0x00, r_hbyte, r_lbyte, checksum])  # Encabezado + System + Data
    wu.write(r_register_cmd)
    time.sleep(delay_ms / 1000)

def uart_set_g_register(g_register,delay_ms):
    g_lbyte = g_register & 0x00FF   #Elimina la parte del alta del byte
    g_hbyte = g_register & 0xFF00   #Deja en 0 la parte baja del byte
    g_hbyte = g_hbyte >> 8          #Realiza desplazamiento para dejar solo el valor del parte alta
    checksum = 0x6E^0x51^0x86^0x03^0xFE^0x18^0x00^g_hbyte^g_lbyte    #Calculo de checksum
    checksum = checksum & 0xFF  #Operacion AND para eliminar el desbordamiento en el calculo de checksum
    g_register_cmd =bytearray([0x6E, 0x51, 0x86, 0x03, 0xFE, 0x18, 0x00, g_hbyte, g_lbyte, checksum])  # Encabezado + System + Data
    wu.write(g_register_cmd)
    time.sleep(delay_ms / 1000)

def uart_set_b_register(b_register,delay_ms):
    b_lbyte = b_register & 0x00FF   #Elimina la parte del alta del byte
    b_hbyte = b_register & 0xFF00   #Deja en 0 la parte baja del byte
    b_hbyte = b_hbyte >> 8          #Realiza desplazamiento para dejar solo el valor del parte alta
    checksum = 0x6E^0x51^0x86^0x03^0xFE^0x1A^0x00^b_hbyte^b_lbyte    #Calculo de checksum
    checksum = checksum & 0xFF  #Operacion AND para eliminar el desbordamiento en el calculo de checksum
    b_register_cmd =bytearray([0x6E, 0x51, 0x86, 0x03, 0xFE, 0x1A, 0x00, b_hbyte, b_lbyte, checksum])  # Encabezado + System + Data
    wu.write(b_register_cmd)
    time.sleep(delay_ms / 1000)



def uart_white_warm_alignment_MT9970A(cordenate_x,cordenate_y,accuracy):
    r_reg_1 = 150                      #Valor del registro r para el primer punto de x Vs b
    g_reg_1 = 150                     #Valor del registro g para el primer punto de x Vs b
    b_reg_1 = 150                      #Valor del registro b para el primer punto de x Vs b
    b_reg_2 = 60                      #Valor del registro b para el segundo punto de x Vs b(si aumenta-aumenta x )
    g_reg_2 = 90                       #Valor del registro g para el segundo punto de x Vs g(si disminuye- aumenta y)
    uart_set_warm_color_temp_2k21(1000)
    uart_set_r_register(r_reg_1,100)
    uart_set_g_register(g_reg_1,100)
    uart_set_b_register(b_reg_1,100)
    y1 = ca310_measure_x()
    x1 = r_reg_1
    uart_set_b_register(b_reg_2, 300)       #Se aumento el delay para evitar la division por zero
    y2= ca310_measure_x()
    x2=b_reg_2
    m = (y2-y1)/(x2-x1)                     #calculo de la pendiente de la recta x Vs b
    b = y2 - (m * x2)                       #calculo de la ordenada al origen de x vs b
    register_B = (cordenate_x-b)/m          #calculo del registro b
    register_B =int(register_B)             #Se convierte el registro b de flotante a entero
    uart_set_b_register(register_B,200)     #Se envia el valor del registro b al tv
    y1 = ca310_measure_y()                   #Valor de la coordenada Y para el primer punto
    x1 = g_reg_1
    uart_set_g_register(g_reg_2, 200)
    y2 = ca310_measure_y()                   #Valor de la coordenada Y para el segundo punto
    x2 = g_reg_2
    m = (y2 - y1) / (x2 - x1)  # calculo de la pendiente de la recta y Vs g
    b = y2 - (m * x2)  # calculo de la ordenada al origen de x vs b
    register_G = (cordenate_y - b) / m  # calculo del registro g
    register_G = int(register_G)
    uart_set_g_register(register_G, 200)  # Se envia el valor del registro b al tv
    read_ca310_p5 = ca310_measure_xy_L()
    print("Warm temp=",read_ca310_p5)
    print("r=",r_reg_1, "g=",register_G, "b=",register_B)
    if (cordenate_x-accuracy) <= read_ca310_p5[0] and read_ca310_p5[0] <= (cordenate_x+accuracy)\
            and (cordenate_y-accuracy) <= read_ca310_p5[1] and read_ca310_p5[1] <= (cordenate_y+accuracy):
       print("Aparato ajustado en temperatura warm")
       uart_save_warm_temperature_data_2k21(300)
    else:
       print("Aparato fuera de especificaciones en temperatura warm")
       input()
    r= str(r_reg_1)
    g= str(register_G)
    b= str(register_B)
    return r,g,b


def uart_white_normal_alignment_MT9970A(cordenate_x,cordenate_y,accuracy):
    r_reg_1 = 150                     #Valor del registro r para el primer punto de x Vs b
    g_reg_1 = 150                      #Valor del registro g para el primer punto de x Vs b
    b_reg_1 = 150                      #Valor del registro b para el primer punto de x Vs b
    b_reg_2 = 110                       #Valor del registro b para el segundo punto de x Vs b
    r_reg_2 = 110                       #Valor del registro r para el segundo punto de x Vs g
    uart_set_normal_color_temp_2k21(200)
    uart_set_r_register(r_reg_1,100)
    uart_set_g_register(g_reg_1,100)
    uart_set_b_register(b_reg_1,100)
    y1 = ca310_measure_y()
    x1 = r_reg_1
    uart_set_b_register(b_reg_2, 100)
    y2=ca310_measure_y()
    x2=b_reg_2
    m = (y2-y1)/(x2-x1)                     #calculo de la pendiente de la recta x Vs b
    b = y2 - (m * x2)                       #calculo de la ordenada al origen de x vs b
    register_B = (cordenate_y-b)/m          #calculo del registro b
    register_B =int(register_B)             #Se convierte el registro b de flotante a entero
    uart_set_b_register(register_B,100)     #Se envia el valor del registro b al tv
    y1 = ca310_measure_x()                  #Valor de la coordenada x para el primer punto
    x1 = r_reg_1
    uart_set_r_register(r_reg_2, 100)
    y2 = ca310_measure_x()                  #Valor de la coordenada Y para el segundo punto
    x2 = r_reg_2
    m = (y2 - y1) / (x2 - x1)  # calculo de la pendiente de la recta y Vs g
    b = y2 - (m * x2)  # calculo de la ordenada al origen de x vs b
    register_R = (cordenate_x - b) / m  # calculo del registro g
    register_R = int(register_R)
    uart_set_r_register(register_R, 100)  # Se envia el valor del registro r al tv
    read_ca310_p5 = ca310_measure_xy_L()  # Se realiza la medicion
    print("Normal temp=",read_ca310_p5)
    print("r=", register_R, "g=", g_reg_1, "b=", register_B)
    if (cordenate_x-accuracy) <= read_ca310_p5[0] and read_ca310_p5[0] <= (cordenate_x+accuracy)\
            and (cordenate_y-accuracy) <= read_ca310_p5[1] and read_ca310_p5[1] <= (cordenate_y+accuracy):
       print("Aparato ajustado en temperatura normal")
       uart_save_normal_temperature_data_2k21(300)
    else:
       print("Aparato fuera de especificaciones en temperatura normal")
       input()
    r= str(register_R)
    g= str(g_reg_1)
    b= str(register_B)
    return r,g,b


def uart_white_cool_alignment_MT9970A(cordenate_x,cordenate_y,accuracy):
    r_reg_1 = 125                      #Valor del registro r para el primer punto de y Vs g
    g_reg_1 = 125                      #Valor del registro g para el primer punto de y Vs g
    b_reg_1 = 125                      #Valor del registro b para el primer punto de y Vs g
    g_reg_2 = 95                       #Valor del registro g para el segundo punto de y Vs g
    r_reg_2 = 92                       #Valor del registro r para el segundo punto de x Vs g
    uart_set_cool_color_temp_2k21(200)
    uart_set_r_register(r_reg_1,100)
    uart_set_g_register(g_reg_1,100)
    uart_set_b_register(b_reg_1,100)
    y1 = ca310_measure_y()
    x1 = g_reg_1
    uart_set_g_register(g_reg_2, 100)
    y2=ca310_measure_y()
    x2=g_reg_2
    m = (y2-y1)/(x2-x1)                     #calculo de la pendiente de la recta y Vs g
    b = y2 - (m * x2)                       #calculo de la ordenada al origen de y vs g
    register_G = (cordenate_y-b)/m          #calculo del registro G
    register_G =int(register_G)             #Se convierte el registro b de flotante a entero
    uart_set_g_register(register_G,100)     #Se envia el valor del registro b al tv
    y1 = ca310_measure_x()                   #Valor de la coordenada x para el primer punto r Vs x
    x1 = r_reg_1
    uart_set_r_register(r_reg_2, 100)
    y2 = ca310_measure_x()                   #Valor de la coordenada Y para el segundo punto
    x2 = r_reg_2
    m = (y2 - y1) / (x2 - x1)  # calculo de la pendiente de la recta y Vs g
    b = y2 - (m * x2)  # calculo de la ordenada al origen de x vs b
    register_R = (cordenate_x - b) / m  # calculo del registro R
    register_R = int(register_R)
    uart_set_r_register(register_R, 100)  # Se envia el valor del registro r al tv
    read_ca310_p5 = ca310_measure_xy_L()  # Se realiza la medicion
    print("Cool temp=",read_ca310_p5)
    print("r=", register_R, "g=", register_G, "b=", b_reg_1)
    if (cordenate_x-accuracy) <= read_ca310_p5[0] and read_ca310_p5[0] <= (cordenate_x+accuracy)\
            and (cordenate_y-accuracy) <= read_ca310_p5[1] and read_ca310_p5[1] <= (cordenate_y+accuracy):
       print("Aparato ajustado en temperatura fria")
       uart_save_cool_temperature_data_2k21(400)
    else:
       print("Aparato fuera de especificaciones en temperatura fria")
       input()
    r= str(register_R)
    g= str(register_G)
    b= str(b_reg_1)
    return r,g,b




def uart_white_warm_alignment_MT9675(cordenate_x,cordenate_y,accuracy):
    r_reg_1 = 1023                      #Valor del registro r para el primer punto de x Vs b
    g_reg_1 = 1023                      #Valor del registro g para el primer punto de x Vs b
    b_reg_1 = 1023                      #Valor del registro b para el primer punto de x Vs b
    b_reg_2 = 600                       #Valor del registro b para el segundo punto de x Vs b
    g_reg_2 = 900                       #Valor del registro g para el segundo punto de x Vs g
    uart_set_warm_color_temp_2k21(200)
    uart_set_r_register(r_reg_1,100)
    uart_set_g_register(g_reg_1,100)
    uart_set_b_register(b_reg_1,100)
    y1 = ca310_measure_x()
    x1 = r_reg_1
    uart_set_b_register(b_reg_2, 300)       #Se aumento el delay para evitar la division por zero
    y2= ca310_measure_x()
    x2=b_reg_2
    m = (y2-y1)/(x2-x1)                     #calculo de la pendiente de la recta x Vs b
    b = y2 - (m * x2)                       #calculo de la ordenada al origen de x vs b
    register_B = (cordenate_x-b)/m          #calculo del registro b
    register_B =int(register_B)             #Se convierte el registro b de flotante a entero
    uart_set_b_register(register_B,200)     #Se envia el valor del registro b al tv
    y1 = ca310_measure_y()                   #Valor de la coordenada Y para el primer punto
    x1 = g_reg_1
    uart_set_g_register(g_reg_2, 200)
    y2 = ca310_measure_y()                   #Valor de la coordenada Y para el segundo punto
    x2 = g_reg_2
    m = (y2 - y1) / (x2 - x1)  # calculo de la pendiente de la recta y Vs g
    b = y2 - (m * x2)  # calculo de la ordenada al origen de x vs b
    register_G = (cordenate_y - b) / m  # calculo del registro g
    register_G = int(register_G)
    uart_set_g_register(register_G, 200)  # Se envia el valor del registro b al tv
    read_ca310_p5 = ca310_measure_xy_L()
    print("Warm temp=",read_ca310_p5)
    print("r=",r_reg_1, "g=",register_G, "b=",register_B)
    if (cordenate_x-accuracy) <= read_ca310_p5[0] and read_ca310_p5[0] <= (cordenate_x+accuracy)\
            and (cordenate_y-accuracy) <= read_ca310_p5[1] and read_ca310_p5[1] <= (cordenate_y+accuracy):
       print("Aparato ajustado en temperatura warm")
       uart_save_warm_temperature_data_2k21(300)
    else:
       print("Aparato fuera de especificaciones en temperatura warm")
       input()
    r= str(r_reg_1)
    g= str(register_G)
    b= str(register_B)
    return r,g,b


def uart_white_normal_alignment_MT9675(cordenate_x,cordenate_y,accuracy):
    r_reg_1 = 1023                      #Valor del registro r para el primer punto de x Vs b
    g_reg_1 = 1023                      #Valor del registro g para el primer punto de x Vs b
    b_reg_1 = 1023                      #Valor del registro b para el primer punto de x Vs b
    b_reg_2 = 600                       #Valor del registro b para el segundo punto de x Vs b
    r_reg_2 = 950                       #Valor del registro r para el segundo punto de x Vs g
    uart_set_normal_color_temp_2k21(200)
    uart_set_r_register(r_reg_1,100)
    uart_set_g_register(g_reg_1,100)
    uart_set_b_register(b_reg_1,100)
    y1 = ca310_measure_y()
    x1 = r_reg_1
    uart_set_b_register(b_reg_2, 100)
    y2=ca310_measure_y()
    x2=b_reg_2
    m = (y2-y1)/(x2-x1)                     #calculo de la pendiente de la recta x Vs b
    b = y2 - (m * x2)                       #calculo de la ordenada al origen de x vs b
    register_B = (cordenate_y-b)/m          #calculo del registro b
    register_B =int(register_B)             #Se convierte el registro b de flotante a entero
    uart_set_b_register(register_B,100)     #Se envia el valor del registro b al tv
    y1 = ca310_measure_x()                  #Valor de la coordenada x para el primer punto
    x1 = r_reg_1
    uart_set_r_register(r_reg_2, 100)
    y2 = ca310_measure_x()                  #Valor de la coordenada Y para el segundo punto
    x2 = r_reg_2
    m = (y2 - y1) / (x2 - x1)  # calculo de la pendiente de la recta y Vs g
    b = y2 - (m * x2)  # calculo de la ordenada al origen de x vs b
    register_R = (cordenate_x - b) / m  # calculo del registro g
    register_R = int(register_R)
    uart_set_r_register(register_R, 100)  # Se envia el valor del registro r al tv
    read_ca310_p5 = ca310_measure_xy_L()  # Se realiza la medicion
    print("Normal temp=",read_ca310_p5)
    print("r=", register_R, "g=", g_reg_1, "b=", register_B)
    if (cordenate_x-accuracy) <= read_ca310_p5[0] and read_ca310_p5[0] <= (cordenate_x+accuracy)\
            and (cordenate_y-accuracy) <= read_ca310_p5[1] and read_ca310_p5[1] <= (cordenate_y+accuracy):
       print("Aparato ajustado en temperatura normal")
       uart_save_normal_temperature_data_2k21(300)
    else:
       print("Aparato fuera de especificaciones en temperatura normal")
       input()
    r= str(register_R)
    g= str(g_reg_1)
    b= str(register_B)
    return r,g,b


def uart_white_cool_alignment_MT9675(cordenate_x,cordenate_y,accuracy):
    r_reg_1 = 1023                      #Valor del registro r para el primer punto de y Vs g
    g_reg_1 = 1023                      #Valor del registro g para el primer punto de y Vs g
    b_reg_1 = 1023                      #Valor del registro b para el primer punto de y Vs g
    g_reg_2 = 950                       #Valor del registro g para el segundo punto de y Vs g
    r_reg_2 = 920                       #Valor del registro r para el segundo punto de x Vs g
    uart_set_cool_color_temp_2k21(200)
    uart_set_r_register(r_reg_1,100)
    uart_set_g_register(g_reg_1,100)
    uart_set_b_register(b_reg_1,100)
    y1 = ca310_measure_y()
    x1 = g_reg_1
    uart_set_g_register(g_reg_2, 100)
    y2=ca310_measure_y()
    x2=g_reg_2
    m = (y2-y1)/(x2-x1)                     #calculo de la pendiente de la recta y Vs g
    b = y2 - (m * x2)                       #calculo de la ordenada al origen de y vs g
    register_G = (cordenate_y-b)/m          #calculo del registro G
    register_G =int(register_G)             #Se convierte el registro b de flotante a entero
    uart_set_g_register(register_G,100)     #Se envia el valor del registro b al tv
    y1 = ca310_measure_x()                   #Valor de la coordenada x para el primer punto r Vs x
    x1 = r_reg_1
    uart_set_r_register(r_reg_2, 100)
    y2 = ca310_measure_x()                   #Valor de la coordenada Y para el segundo punto
    x2 = r_reg_2
    m = (y2 - y1) / (x2 - x1)  # calculo de la pendiente de la recta y Vs g
    b = y2 - (m * x2)  # calculo de la ordenada al origen de x vs b
    register_R = (cordenate_x - b) / m  # calculo del registro R
    register_R = int(register_R)
    uart_set_r_register(register_R, 100)  # Se envia el valor del registro r al tv
    read_ca310_p5 = ca310_measure_xy_L()  # Se realiza la medicion
    print("Cool temp=",read_ca310_p5)
    print("r=", register_R, "g=", register_G, "b=", b_reg_1)
    if (cordenate_x-accuracy) <= read_ca310_p5[0] and read_ca310_p5[0] <= (cordenate_x+accuracy)\
            and (cordenate_y-accuracy) <= read_ca310_p5[1] and read_ca310_p5[1] <= (cordenate_y+accuracy):
       print("Aparato ajustado en temperatura fria")
       uart_save_cool_temperature_data_2k21(400)
    else:
       print("Aparato fuera de especificaciones en temperatura fria")
       input()
    r= str(register_R)
    g= str(register_G)
    b= str(b_reg_1)
    return r,g,b

def uart_white_initialization_commands_MT9675():
    uart_mtk9675_head(1000)
    uart_enter_factory()
    uart_set_burnin_mode(0)
    uart_change_hdmi()
    uart_open_internal_pattern_mode()
    uart_80_white_pattern()

def uart_white_initialization_commands_MT9970A():
    uart_mt5800_head(1000)
    uart_enter_factory()
    time.sleep(0.5)
    uart_set_burnin_mode(0)
    time.sleep(0.5)
    uart_change_hdmi()
    time.sleep(0.5)
    uart_open_internal_pattern_mode()
    time.sleep(0.5)
    uart_80_white_pattern()



def average_register(file_rgb):
    fdatos = open(file_rgb, 'r') #  Abrimos el fichero "datos.txt" para lectura
    r_warm = []                #  Creamos una lista para la primera columna
    g_warm = []                #  Creamos una lista para la segunda columna
    b_warm = []                #  Creamos una lista para la tercera columna
    r_normal = []              #  Creamos una lista para la cuarta columna
    g_normal = []              #  Creamos una lista para la quinta columna
    b_normal = []              #  Creamos una lista para la sexta columna
    r_cool = []                #  Creamos una lista para la septima columna
    g_cool = []                #  Creamos una lista para la octava columna
    b_cool = []                #  Creamos una lista para la novena columna
    lineas = fdatos.readlines()    #Leemos el fichero línea a línea
    for linea in lineas:
        a, b, c, d, e, f, g, h, i = linea.split()     # Se separa cada línea en dos columnas
        r_warm.append(int(a)) # Añado el elemento a a la lista r_warm
        g_warm.append(int(b)) # Añado el elemento b a la lista g_warm
        b_warm.append(int(c)) # Añado el elemento c a la lista b_warm
        r_normal.append(int(d)) # Añado el elemento d a la lista r_normal
        g_normal.append(int(e)) # Añado el elemento e a la lista g_normal
        b_normal.append(int(f)) # Añado el elemento f a la lista b_normal
        r_cool.append(int(g)) # Añado el elemento g a la lista r_cool
        g_cool.append(int(h)) # Añado el elemento h a la lista g_cool
        b_cool.append(int(i)) # Añado el elemento i a la lista b_cool
    fdatos.close()
    r_warm_average_f = sum(r_warm)/len(r_warm)
    g_warm_average_f = sum(g_warm)/len(g_warm)
    b_warm_average_f = sum(b_warm)/len(b_warm)
    r_normal_average_f = sum(r_normal)/len(r_normal)
    g_normal_average_f = sum(g_normal)/len(g_normal)
    b_normal_average_f = sum(b_normal)/len(b_normal)
    r_cool_average_f = sum(r_cool)/len(r_normal)
    g_cool_average_f = sum(g_cool)/len(g_normal)
    b_cool_average_f = sum(b_cool)/len(b_normal)
    r_warm_average = int(r_warm_average_f)
    g_warm_average = int(g_warm_average_f)
    b_warm_average = int(b_warm_average_f)
    r_normal_average = int(r_normal_average_f)
    g_normal_average = int(g_normal_average_f)
    b_normal_average = int(b_normal_average_f)
    r_cool_average = int(r_cool_average_f)
    g_cool_average = int(g_cool_average_f)
    b_cool_average = int(b_cool_average_f)
    r_warm_average = str(r_warm_average)
    g_warm_average = str(g_warm_average)
    b_warm_average = str(b_warm_average)
    r_normal_average = str(r_normal_average)
    g_normal_average = str(g_normal_average)
    b_normal_average = str(b_normal_average)
    r_cool_average = str(r_cool_average)
    g_cool_average = str(g_cool_average)
    b_cool_average = str(b_cool_average)
    f = open('average_register.txt', 'w')
    f.write(str(r_warm_average)+' '+ str(g_warm_average)+' '+ str(b_warm_average)+' '+r_normal_average+' '+g_normal_average+' '+b_normal_average+
            ' '+r_cool_average+' '+g_cool_average+' '+b_cool_average)
    f.close()


def set_and_check_white_register(warm_x,warm_y,normal_x,normal_y,cool_x,cool_y,accuracy):
    fdatos = open('average_register.txt', 'r') #  Abrimos el fichero "datos.txt" para lectura
    r_warm = []                #  Creamos una lista para la primera columna
    g_warm = []                #  Creamos una lista para la segunda columna
    b_warm = []                #  Creamos una lista para la tercera columna
    r_normal = []              #  Creamos una lista para la cuarta columna
    g_normal = []              #  Creamos una lista para la quinta columna
    b_normal = []              #  Creamos una lista para la sexta columna
    r_cool = []                #  Creamos una lista para la septima columna
    g_cool = []                #  Creamos una lista para la octava columna
    b_cool = []                #  Creamos una lista para la novena columna
    lineas = fdatos.readlines()    #Leemos el fichero línea a línea
    for linea in lineas:
        a, b, c, d, e, f, g, h, i = linea.split()     # Se separa cada línea en dos columnas
        r_warm.append(int(a)) # Añado el elemento a a la lista r_warm
        g_warm.append(int(b)) # Añado el elemento b a la lista g_warm
        b_warm.append(int(c)) # Añado el elemento c a la lista b_warm
        r_normal.append(int(d)) # Añado el elemento d a la lista r_normal
        g_normal.append(int(e)) # Añado el elemento e a la lista g_normal
        b_normal.append(int(f)) # Añado el elemento f a la lista b_normal
        r_cool.append(int(g)) # Añado el elemento g a la lista r_cool
        g_cool.append(int(h)) # Añado el elemento h a la lista g_cool
        b_cool.append(int(i)) # Añado el elemento i a la lista b_cool
    fdatos.close()

    uart_set_warm_color_temp_2k21(200)
    uart_set_r_register(r_warm[0],100)
    uart_set_g_register(g_warm[0],100)
    uart_set_b_register(b_warm[0],100)
    read_ca310_warm = ca310_measure_xy_L()  # Se realiza la medicion
    print("Warm temp=",read_ca310_warm)
    if (warm_x-accuracy) <= read_ca310_warm[0] and read_ca310_warm[0] <= (warm_x+accuracy)\
        and (warm_y-accuracy) <= read_ca310_warm[1] and read_ca310_warm[1] <= (warm_y+accuracy):
       print("Aparato ajustado en temperatura warm")
       uart_save_warm_temperature_data_2k21(300)
    else:
       print("Aparato fuera de especificaciones en temperatura warm")
       time.sleep(1)
       uart_white_warm_alignment_Android_2k21(313, 329, 3)
    time.sleep(0.8)
    uart_set_normal_color_temp_2k21(200)
    uart_set_r_register(r_normal[0],100)
    uart_set_g_register(g_normal[0],100)
    uart_set_b_register(b_normal[0],100)
    read_ca310_normal = ca310_measure_xy_L()  # Se realiza la medicion
    print("Normal temp=",read_ca310_normal)
    if (normal_x-accuracy) <= read_ca310_normal[0] and read_ca310_normal[0] <= (normal_x+accuracy)\
            and (normal_y-accuracy) <= read_ca310_normal[1] and read_ca310_normal[1] <= (normal_y+accuracy):
       print("Aparato ajustado en temperatura normal")
       uart_save_normal_temperature_data_2k21(300)
    else:
       print("Aparato fuera de especificaciones en temperatura normal")
       time.sleep(1)
       uart_white_normal_alignment_Android_2k21(287, 296, 3)
    time.sleep(0.8)
    uart_set_cool_color_temp_2k21(200)
    uart_set_r_register(r_cool[0],100)
    uart_set_g_register(g_cool[0],100)
    uart_set_b_register(b_cool[0],100)
    read_ca310_cool = ca310_measure_xy_L()  # Se realiza la medicion
    print("Cool temp=",read_ca310_cool)
    if (cool_x-accuracy) <= read_ca310_cool[0] and read_ca310_cool[0] <= (cool_x+accuracy)\
         and (cool_y-accuracy) <= read_ca310_cool[1] and read_ca310_cool[1] <= (cool_y+accuracy):
       print("Aparato ajustado en temperatura fria")
       uart_save_cool_temperature_data_2k21(400)
    else:
       print("Aparato fuera de especificaciones en temperatura fria")
       time.sleep(1)
       uart_white_cool_alignment_Android_2k21(276, 282, 3)
    time.sleep(0.8)

def curve_alignment_MT9675(file_rgb):
    reg_warm = uart_white_warm_alignment_MT9675(313, 329, 2)
    time.sleep(1)
    reg_normal = uart_white_normal_alignment_MT9675(287, 296, 2)
    time.sleep(1)
    reg_cool = uart_white_cool_alignment_MT9675(276, 282, 2)
    f = open(file_rgb, 'a')
    f.write(reg_warm[0]+' '+reg_warm[1]+' '+reg_warm[2]+' '+reg_normal[0]+' '+reg_normal[1]+' '+reg_normal[2]+
          ' '+reg_cool[0]+' '+reg_cool[1]+' '+reg_cool[2]+'\t\n')
    f.close()

def curve_alignment_MT9970A(file_rgb):
    reg_warm = uart_white_warm_alignment_MT9970A(313, 329, 2)
    time.sleep(1)
    reg_normal = uart_white_normal_alignment_MT9970A(287, 296, 2)
    time.sleep(1)
    reg_cool = uart_white_cool_alignment_MT9970A(276, 282, 2)
    f = open(file_rgb, 'a')
    f.write(reg_warm[0]+' '+reg_warm[1]+' '+reg_warm[2]+' '+reg_normal[0]+' '+reg_normal[1]+' '+reg_normal[2]+
          ' '+reg_cool[0]+' '+reg_cool[1]+' '+reg_cool[2]+'\t\n')
    f.close()




#Comandos para trabajar con señales de RF:

def uart_digital_channel(char_1,char_2,delay_ms):
    checksum = 0x6E^0x51^0x8C^0x03^0xFE^0xF0^0x16^0x02^0x06^0x01^0x02^0x00^char_1^0x00^char_2
    wu_cmd = bytearray([0x6E, 0x51, 0x8C, 0x03, 0xFE, 0xF0, 0x16, 0x02,0x06,0x01,0x02,0x00,char_1,0x00,char_2,checksum])  # Encabezado + System + Data
    wu.write(wu_cmd)
    time.sleep(delay_ms/1000)

def uart_analogic_channel(char_1,delay_ms):
   # wu.write(b'\x6E\x51\x8C\x03\xFE\xF0\x16\x02\x06\x01\x00\x00\x09\x00\x00\xA4')
    checksum = 0x6E^0x51^0x8C^0x03^0xFE^0xF0^0x16^0x02^0x06^0x01^0x00^0x00^char_1^0x00^0x00
    wu_cmd = bytearray([0x6E, 0x51, 0x8C, 0x03, 0xFE, 0xF0, 0x16, 0x02,0x06,0x01,0x00,0x00,char_1,0x00,0x00,checksum])  # Encabezado + System + Data
    wu.write(wu_cmd)
    time.sleep(delay_ms/1000)

def uart_digital_channel_26_1(delay_ms):
    wu.write(b'\x6E\x51\x8C\x03\xFE\xF0\x16\x02\x06\x01\x02\x00\x1A\x00\x01\xB4')
    time.sleep(delay_ms/1000)

def uart_analogic_channel_9(delay_ms):
    wu.write(b'\x6E\x51\x8C\x03\xFE\xF0\x16\x02\x06\x01\x00\x00\x09\x00\x00\xA4')
    time.sleep(delay_ms/1000)

def uart_set_serial_number(serial_number,delay_ms):
    serial_number = bytes(serial_number, 'utf-8')       # Convierte el numero de serie a bytes
    serial_number_sbyte = serial_number
    serial_number = list(serial_number)                 # Genera el array de bytes
    header = [0x6E,0x51,0x92,0x03,0xFE,0xE8,0x0E]       # Encabezado del comando para cargar elnumero de serie
    tv_command = header + serial_number
    time.sleep(delay_ms/1000)
    checksum=0
    for byte in tv_command:
        checksum=byte ^ checksum                        # Realiza la operacion XOR con cada indice del array para calcular el checksum
    tv_command.append(checksum)                         # Funcion que permite agregar el valor del checksum al final de la cola del array
    tv_command = bytearray(tv_command)                  # Realiza la conversion de array a byte array para ser enviado por el puerto serial
    wu.write(tv_command)
    time.sleep(0.2)
    wu.write(b'\x6E\x51\x86\x01\xFE\xE8\x0E\x00\x00\xA0')   #Envia el comando para leer el numero de serie del tv
    tv_read = wu.read(20)
    tv_sn = tv_read[6:20]
    if tv_sn == serial_number_sbyte:
        print("serial_number:", tv_sn, "ok")
    else:
        print("serial_number:", tv_sn, "failed")

def uart_ctn_check(ctn,delay_ms):
    wu.write(b'\x6E\x51\x86\x01\xFE\xF0\x18\x04\x00\xAA')   #Envia el comando para leer el ctn del tv
    tv_read= wu.read(20)
    tv_ctn = tv_read[3:20]
    if tv_ctn == ctn:
        print("ctn_read:", tv_ctn, "ok")
    else:
        print("ctn_read:", tv_ctn, "failed")
    time.sleep(delay_ms/1000)

def uart_main_sw_check(main_sw,delay_ms):
    wu.write(b'\x6E\x51\x86\x01\xFE\xE4\x13\x00\x00\xB1')   #Envia el comando para leer el main sw del tv
    tv_read= wu.read(28)
    tv_main_sw = tv_read[3:28]

    if tv_main_sw == main_sw:
        print("main_sw_read:", tv_main_sw, "ok")
    else:
        print("main_sw_read:", tv_main_sw,  "failed")
    time.sleep(delay_ms/1000)

def uart_panel_id_check(panel_id,delay_ms):
    wu.write(b'\x6E\x51\x86\x01\xFE\xE1\xA7\x07\x01\x06')   #Envia el comando para leer el main sw del tv
    tv_read= wu.read(28)
    tv_panel_id = tv_read[3:28]
    if tv_panel_id == panel_id:
        print("panel_id_read:", tv_panel_id, "ok")
    else:
        print("panel_id_read:", tv_panel_id, "failed")
    time.sleep(delay_ms/1000)


def uart_check_wireless_strenght(ssci,delay_ms):
    ssci = bytes(ssci, 'utf-8')       # Convierte el numero de serie a bytes
    ssci = list(ssci)                 # Genera el array de bytes
    header = [0x6E,0x51,0x8E,0x03,0xFE,0xF0,0x02,0x04,0x0A,0x07]       # Encabezado del comando para cargar elnumero de serie
    tv_command = header + ssci
    time.sleep(delay_ms/1000)
    checksum=0
    for byte in tv_command:
        checksum=byte ^ checksum                        # Realiza la operacion XOR con cada indice del array para calcular el checksum
    tv_command.append(checksum)                         # Funcion que permite agregar el valor del checksum al final de la cola del array
    tv_command = bytearray(tv_command)                  # Realiza la conversion de array a byte array para ser enviado por el puerto serial
    wu.write(tv_command)
    time.sleep(delay_ms/1000)
    tv_read = wu.read(8)
    tv_read = tv_read[5:8]
    tv_strenght = tv_read[0]
    if tv_strenght >= 180:
        print("signal_strenght:", tv_strenght, "ok")
    else:
        print("signal_strenght::", tv_strenght, "failed")

