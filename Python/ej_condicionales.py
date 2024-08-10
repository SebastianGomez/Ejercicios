""""
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si 
# es mayor de edad o no.

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("El usuario es mayor de edad")
else:
    print("El usuario es menor de edad")

# Escribir un programa que almacene la cadena de caracteres contraseña en una 
# variable, pregunte al usuario por la contraseña e imprima por pantalla si la 
# contraseña introducida por el usuario coincide con la guardada en la variable 
# sin tener en cuenta mayúsculas y minúsculas.

cont_almacenada = "greta"
while True:
    cont = input("Ingrese la contraseña: ")

    if cont_almacenada == cont.lower():
        print("La contraseña es correcta")
        break
    else: 
        print("Contraseña incorrecta")

# Escribir un programa que pida al usuario dos números y muestre por pantalla su 
# división. Si el divisor es cero el programa debe mostrar un error.

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num2 == 0:
    print("No se puede dividir por 0")
else:
    print(f"{num1}/{num2} : {num1/num2}")

# Escribir un programa que pida al usuario un número entero y muestre por 
# pantalla si es par o impar.

num = int(input("Ingrese un numero: "))

if num == 0 or num%2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")



# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener 
# unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa 
# que pregunte al usuario su edad y sus ingresos mensuales y muestre por 
# pantalla si el usuario tiene que tributar o no.


edad = int(input("Ingrese su edad: "))
ingresos = int(input("Ingrese sus ingresos mensuales: "))

if edad>=16 and ingresos>=1000:
    print("El usuario debe tributar")
else: 
    print("El usuario no debe tributar")

    


# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo 
# y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a 
# la M y los hombres con un nombre posterior a la N y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por 
# pantalla el grupo que le corresponde.

nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (M/F): ").lower()

if (sexo ==  "f" and nombre.lower()<"m") or (sexo ==  "m" and nombre.lower()>"n"):
    print("pertenece al grupo A")
else:
    print("pertenece al grupo B")

"""



    





