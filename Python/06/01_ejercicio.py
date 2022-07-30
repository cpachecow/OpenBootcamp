# Ejercicio 1, clase POO: 

class Vehiculo():

    color = "Azul"
    ruedas = 4
    puertas = 4

class Coche(Vehiculo):

    velocidad = "300 km/h"
    cilindrada = "3.5"


a = Coche()
print("Las características de mi Coche:")
print("Color:", a.color)
print("Ruedas:", a.ruedas)
print("Velocidad:", a.velocidad)
print("Puertas:", a.puertas)
