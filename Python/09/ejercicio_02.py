from functools import reduce

numeros = [2,3,4,5,6,7,8,9,19,11, 20, 22]

res = filter(lambda x: x % 2 != 0, numeros)

def suma(t, v):
    return t+v

a = reduce(suma, res)

print(a)
