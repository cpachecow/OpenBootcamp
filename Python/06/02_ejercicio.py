# Ejercicio 2, clase POO: 

class Alumno():
    nombre = "Pedro Alcayaga"
    nota = None

    def IsAprobado(self, nota):
        self.nota = int(nota)
        
        if(self.nota >= 4):
            print("Estimado fuiste aprobado :)")
        elif(self.nota < 4):
            print("Estimado fuiste reprobado")

a = Alumno()

print(a.nombre)

b = a.IsAprobado(input("Ingresa tu nota: "))





