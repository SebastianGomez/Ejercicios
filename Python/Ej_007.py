"""
Crea un programa que invierta el orden de una cadena de texto sin usar funciones 
propias del lenguaje que lo hagan de forma automática.
Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def invertir_cadena(cadena):
    cadena_invertida = []
    longitud = len(cadena)
    
    for i in range(-1,-longitud-1,-1):
        cadena_invertida.append(cadena[i])
    return ''.join(cadena_invertida)

    
print(invertir_cadena(input("Ingrese la cadena a invertir: ")))

























"""cadena = input("Ingrese una cadena de texto:")
cadena2 = []
def fun1 (cadena):
    longitud = len(cadena)
    for i in range (longitud-1,-1,-1):#(inicio,fin,paso)
        cadena2.append(cadena[i])#agrega al final de la lista
    return ''.join(cadena2)#convierte la lista en cadena


print(fun1(cadena))
"""


