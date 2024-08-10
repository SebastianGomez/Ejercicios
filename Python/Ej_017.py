# Crea una función que reciba un String de cualquier tipo y se encargue de poner 
# en mayúscula la primera letra de cada palabra.
# - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.



string = input("Ingrese un texto: ")


#utilizando operaciones propias de python

def fun1(string):
    print(string.title())


#fun1(string)

def fun2(string):
    texto = string.split()
    #print(texto)
    texto_mayusculas = []
    for letra in texto:
        if len(letra)>0:
            primera_letra = letra[0].upper()
            segunda_letra = letra[1:].lower() 
            texto_mayuscula = primera_letra + segunda_letra
            texto_mayusculas.append(texto_mayuscula)
    #print(texto_mayusculas)
    resultado = ' '.join(texto_mayusculas)
    print(resultado)

fun2(string)
