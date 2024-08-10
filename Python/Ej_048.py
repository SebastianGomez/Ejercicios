# Crea un función que reciba un texto y retorne la vocal que más veces se repita.
# - Ten cuidado con algunos casos especiales.
# - Si no hay vocales podrá devolver vacío.


def fun(texto):
    a,e,i,o,u = 0,0,0,0,0


    for n in range(0,len(texto)):
        if texto[n] == "a":
            a=a+1
        elif texto[n] == "e":
            e=e+1
        elif texto[n] == "i":
            i=i+1
        elif texto[n] == "o":
            o=o+1
        elif texto[n] == "u":
            u=u+1

    print(f"Hay {a} a, {e} e, {i} i, {o} o, {u} u")

def fun2(texto):
    vocales = "aeiou"
    dic = {}
    for n in vocales:
        if n in texto:
            vocal = texto.count(n)
            dic[n] = vocal
            vocal_max = max(dic,key=dic.get)
    return vocal_max

#fun(input("Ingrese el texto a analizar: "))
print(fun2("el perro sale a pasear"))


