"""
# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 
# 10 veces.

palabra = input("Ingrese una palabra: ")
for i in range(10):
    print(palabra)


# Escribir un programa que pregunte al usuario su edad y muestre por pantalla 
# todos los años que ha cumplido (desde 1 hasta su edad).

edad = int(input("Ingrese su edad: "))

for i in range(1,edad+1):
    print(i)

# Escribir un programa que pida al usuario un número entero positivo y muestre 
# por pantalla todos los números impares desde 1 hasta ese número separados por 
# comas.

numero = int(input("Ingrese un numero entero positivo: "))

for i in range(1,numero+1,2):
    print(i)


# Escribir un programa que pida al usuario un número entero positivo y muestre 
# por pantalla la cuenta atrás desde ese número hasta cero separados por comas

num = int(input("Ingrese un numero positivo: "))

while num>=0:
    print(num,end=",")
    num-=1


# Escribir un programa que pregunte al usuario una cantidad a invertir, el 
# interés anual y el número de años, y muestre por pantalla el capital obtenido 
# en la inversión cada año que dura la inversión

inversion = int(input("Ingrese la cantidad a invertir: "))
interes = int(input("Ingrese el interes anual: "))
anios = int(input("Ingrese la cantidad de años a invertir: "))

for i in range (1,anios+1):
    inversion +=inversion*(interes/100)
    print(f"Año: {i}   Ganancia: {inversion}")


# Escribir un programa que pida al usuario un número entero y muestre por 
# pantalla un triángulo rectángulo, de altura el número introducido.

triangulo = int(input("Ingrese la altura del triangulo: "))

for i in range(1,triangulo+1):
    print("*"*i)


# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 
# al 10.

for i in range(1,11):
    print(i*10)

"""

# Escribir un programa que pida al usuario un número entero y muestre por 
# pantalla un triángulo rectángulo como el de más abajo.

# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

triangulo = int(input("Ingrese la altura del triangulo: "))

for i in range(1,triangulo+1):
    print("*"*i)
terminar
