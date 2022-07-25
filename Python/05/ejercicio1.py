# Funciones
# Ejercicio 1: Escribe una función que calcule el área de un triángulo,
# recibiendo la altura y la base como parámetros y otra función
# que calcule el área de un círculo recibiendo el radio del mismo.

def areaT(base, altura):
    return (base * altura)/2

def areaC(radio):
    return (3.14 * (radio**2))

triangulo = areaT(3,5)
circulo = areaC(5)

print("El aŕea del tríangulo es:",triangulo)
print("El aŕea del circulo es:",circulo)
