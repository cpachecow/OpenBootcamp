# Tarea2: Escribe un programa capaz de mostrar todos
#         los números impares desde un número de inicio y otro final.
#
#         Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8,
#         el programa debe imprimir por consola: 
#         [3, 5, 7]edad = int(input('Favor indicar tu edad: '))


num1 = int(input('Ingresa número inicial:'))
num2 = int(input('Ingresa número final:'))
i = 1
impar = []

if (num1 > num2):
    print("Error 1: El número inicial debe ser mayor al número final")
    i = 0

elif (num1 == num2):
    print("Error 2: Los números deben ser distintos")
    i = 0


while (num1 < num2) and (i!=0):

    if(num1 % 2 != 0):
        impar.append(num1)
        # print(num1, "es impar")
    num1 += 1
    
if(i != 0):
    print("\nLos impares son:\n\n",impar)
