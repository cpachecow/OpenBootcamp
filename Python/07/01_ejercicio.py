import operaciones as op

# Ejercicio 1, clase Módulos:

# Los módulos son simplemente ficheros con la extensión '.py'
# Se puede tener un fichero principal que llame a otros, lo cuales
# van a contener por lo general funciones o clases. Hay que tener OJO
# con que estos archivos secundarios contengan funciones globales, como
# por ejemplo algún print, dado que se ejecutará en el fichero principal.

# Los módulos importados pueden tener variables (en lo posible que no
# cambien).

print("\n*** Modulo Principal main() ***\n")

num1 = float(input("Ingresa primer número: "))
num2 = float(input("Ingresa segúndo número: "))

a = op.suma(num1, num2)
print("\nSuma:",a)

a = op.resta(num1, num2)
print("Resta:",a)

a = op.producto(num1, num2)
print("Producto:",a)

a = op.division(num1, num2)
print("División:",a)

a = op.potencia(num1, num2)
print("Potencia:",a)

a = op.PI
print(a)

a = op.DOLAR
print("Valor Dólar: $",a)
