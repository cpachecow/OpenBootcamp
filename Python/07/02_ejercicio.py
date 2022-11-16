import time


# Ejercicio 2, clase Módulos:

# Crear un script que nos diga si es la hora de ir a casa.
# Tendréis que hacer uso del modulo time. Necesitaréis la fecha
# del sistema y poder comprobar la hora.
# 
# En el caso de que sean más de las 7, se mostrará un mensaje
# y en caso contrario, haréis una operación para calcular el
# tiempo que queda de trabajo.

print("\n*** Ejercicio N°2 - Módulos ***\n")

# print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
# imrimirá ej: Wed, 16 Nov 2022 03:08:08 +0000

hora_actual = time.localtime() 
tiempo_str = time.strftime("%H:%M:%S", hora_actual)
hora_salida = "19:30:00"
hora_ingreso = "08:30:00"

if(tiempo_str > hora_salida):
    print("Es hora de salir del trabajo")
elif(tiempo_str >= hora_ingreso):
    print("te quedan: "&tiempo_str-hora_ingreso&" para salir")
