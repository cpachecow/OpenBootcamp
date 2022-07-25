# Funciones
# Ejercicio 3: Escribe una función que pueda decirte siun año
#              (número entero) es bisiesto o no.

def esBi(num):

    if(num > 0):

        if(num % 4 == 0):
            return print("Año Bisiesto")
        else: return print("Año No Bisiesto")

    else: return print("Debe ingresar numero mayor a 1")
        
        
numero = esBi(int(input("Ingrese Año: ")))




