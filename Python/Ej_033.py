# Dado un listado de números, encuentra el SEGUNDO más grande


import random

lista = []
for i in range(1,21):
    lista.append(random.randint(1,100))

print(lista)


def segundo(lista):
    
    for i in range(0,len(lista)-1):
        for j in range(0,len(lista)-1-i):
            if lista[j]>lista[j+1]:
                temp = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = temp
    
    return lista[len(lista)-2]

def segundo2(lista):
    lista_ordenada = []
    lista_ordenada = sorted(lista)
    return lista_ordenada[-2]


print(segundo2(lista))

#print(segundo(lista))

