# Ejemplo uso BD

import sqlite3

#abrir BD
conn = sqlite3.connect('ejemplo.db')

#/home/cpachecow/Downloads/Documents/Pogramacion/OpenBootCamp/Curso Python/11/

cursor = conn.cursor()

apellido = str(input("Ingrese apellido a buscar: "))

rows = cursor.execute(f"SELECT * FROM alumno WHERE apellido = '{apellido}'")

for row in rows:
    print(row)

cursor.close()
#cerrar BD
conn.close()
