"""
Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan 
de forma automática.
Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

cadena = input("Ingrese una cadena de texto:")
cadena2 = []
def fun1 (cadena):
    longitud = len(cadena)
    for i in range (longitud-1,-1,-1):
        cadena2.append(cadena[i])
    return ''.join(cadena2)


print(fun1(cadena))



