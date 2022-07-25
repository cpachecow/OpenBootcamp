# Tarea3: Escribe un programa que sea capaz de mostrar
#         los números del 1 al 100 en orden inverso.

numeros = []

for num in range(1, 101): #(1,101]

    numeros.append(num)

numeros = sorted(numeros, reverse = True)

print("\nNúmeros:\n\n",numeros)

    
    
