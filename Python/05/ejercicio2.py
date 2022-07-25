# Funciones
# Ejercicio 2: Escribe una función que pueda decirte si un número
#              (número entero) es primo o no.


def esPrimo(num):

    if(num > 0):
        
        if(num==1): return print("Es primo")
        if(num==2): return print("Es primo")
        
        a = 0

        for n in range (2, num):
              if(num % n == 0):
                  a += 1

        if(a >= 1): return print("No es primo")
        else: return print("Es primo")

    else: return print("Debe ingresar numero mayor a 1")
        
        
numero = esPrimo(int(input("Ingrese Número: ")))




