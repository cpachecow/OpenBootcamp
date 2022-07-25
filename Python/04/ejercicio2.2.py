# Tarea2: Escribe un programa capaz de mostrar todos
#         los números impares desde un número de inicio y otro final.
#
#         Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8,
#         el programa debe imprimir por consola: [3, 5, 7]


num1 = 1
num2 = 20
impar = []

for num in range(num1, num2):
    if(num % 2 != 0): # verificación numero impar
        impar.append(num)
        # print(num1, "es impar")
        
print("\nLos impares entre,",num1,"y",num2,":\n\n",impar)

    
    
