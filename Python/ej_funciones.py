"""
# Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez 
# que se la invoque.

def saludo():
    print("¡Hola amiga!")

saludo()

# Escribir una función a la que se le pase una cadena <nombre> y muestre por 
# pantalla el saludo ¡hola <nombre>!.

nombre = input("Ingrese un nombre: ")

def saludo():
    
    print(f"¡Hola {nombre}!")

saludo(nombre)

"""
# Escribir una función que reciba un número entero positivo y devuelva su 
# factorial

num = int(input("Ingrese un numero:"))

def factorial(num):
    fact = 1
    if num == 0:
        return 1
    elif num <0:
        return -1
    else:
        for i in range(1,num+1):
            fact = i*(fact)
        return fact

print(factorial(num))







