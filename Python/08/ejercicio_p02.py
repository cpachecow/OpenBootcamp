# Ejercicio N°2
#  Crear un archivo py y dentro crearéis
#  una clase Vehículo, haréis un objeto de ella,
#  lo guardaréis en un archivo y luego lo cargamos.

class Vehiculo: # iniciamos el objeto
    _encendido = None # inciamos una propiedad de clase o variable.
    luces = ""

    def enciende(self): # iniciamos un método o función.
        self._encendido = True
        luces = "Encendidas"

    def apaga(self):
        self._encendido = False
        luces = "Apagadas"

v = Vehiculo()
v.enciende()
# print (v._encendido)
f = open('ejercicio02.txt', 'w+')
f.write("El vehículo tiene motor encendido: "+str(v._encendido))
f.close()

f = open('ejercicio02.txt', 'r')
datos = f.read()
print(datos)
f.close()
