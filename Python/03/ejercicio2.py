peso = float(input('Favor indicar tu peso: ')) # solicitando por pantalla el peso.
estatura = float(input('Favor indicar tu estatura (en metros ej 1.62): ')) # solicitando por pantalla la estatura.
imc = (peso/estatura)
imc = "%.2f" % imc # dando formato de dos decimales al número decimal
imc = str(imc)     # pasando de float a string, para poderlo imprimir en pantalla

print ("Su IMC es : " + imc)
