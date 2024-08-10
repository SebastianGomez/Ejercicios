#Crea una función que reciba dos array, un booleano y retorne un array.
 #- Si el booleano es verdadero buscará y retornará los elementos comunes de los 
 # dos array.
#- Si el booleano es falso buscará y retornará los elementos no comunes de los 
# dos array.
#- No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

array1 = "sol"
array2 = "sola"

booleano = True


def funcion(array1,array2,booleano):
    temp = ""
    if booleano:
        for n in array1:
            if n in array2:
                if n not in temp:
                    temp = temp + n
        for n in array2:
            if n in array1:
                if n not in temp:
                    temp = temp + n
    else:
        for n in array1:
            if n not in array2:
                if n not in temp:
                    temp = temp + n
        for n in array2:
            if n not in array1:
                if n not in temp:
                    temp = temp + n

    print(temp)


funcion(array1,array2,booleano)