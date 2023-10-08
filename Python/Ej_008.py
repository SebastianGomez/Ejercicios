"""
Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje 
que lo hagan directamente.
"""

numero = int(input("Ingrese un numero:"))

def fun1 (numero):
    binario = []
    while numero > 0:
        binario.append(numero%2) #agrega al final de la lista
        numero = numero//2 #division entera
    binario.reverse() #invierte el orden de la lista
    return ''.join(str(i) for i in binario) #convierte la lista en cadena

print(fun1(numero))
