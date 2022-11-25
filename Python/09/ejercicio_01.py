c = 1
paises = [] #lista
cant_paises = 3

while c <= cant_paises:

    p=input(f"Ingrese país {c}: ")
    paises.append(p)
    c += 1 

paises = sorted(paises) #ordenando lista
print(paises)
