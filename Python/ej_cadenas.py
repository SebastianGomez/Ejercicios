"""

# Escribir un programa que pregunte el nombre del usuario en la consola y un 
# número entero e imprima por pantalla en líneas distintas el nombre del usuario 
# tantas veces como el número introducido.

nombre = input("Ingrese el nombre de usuario: ")
numero = int(input("Inrese un numero: "))

for i in range(numero):
    print(nombre)





# Escribir un programa que pregunte el nombre completo del usuario en la consola 
# y después muestre por pantalla el nombre completo del usuario tres veces, una 
# con todas las letras minúsculas, otra con todas las letras mayúsculas y otra 
# solo con la primera letra del nombre y de los apellidos en mayúscula. 
# El usuario puede introducir su nombre combinando mayúsculas y minúsculas como 
# quiera.

nombre = (input("Ingrese el nombre competo de usuario: ")).lower()

print(nombre)
print(nombre.upper())
print(nombre.title())


# Escribir un programa que pregunte el nombre del usuario en la consola y después 
# de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, 
# donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de 
# letras que tienen el nombre.

nombre = (input("Ingrese el nombre competo de usuario: ")).lower()
n = 0
for letra in nombre:
    if letra == " ":
        n+=1

print(f"El nombre {nombre} tiene {len(nombre)-n} letras")


# Los teléfonos de una empresa tienen el siguiente formato 
# prefijo-número-extension donde el prefijo es el código del país +34, y la 
# extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un 
# programa que pregunte por un número de teléfono con este formato y muestre por 
# pantalla el número de teléfono sin el prefijo y la extensión.

num = input("Ingrese un numero de telefono en formato +34-xxxxxxxxx-xx: ")

print(num[num.find("-")+1:num.rfind("-")])



# Escribir un programa que pida al usuario que introduzca una frase en la 
# consola y muestre por pantalla la frase invertida.

frase = input("Introduzca una frase: ")

frase_inv = frase[::-1]
print(frase_inv)



# Escribir un programa que pregunte el correo electrónico del usuario en la 
# consola y muestre por pantalla otro correo electrónico con el mismo nombre 
# (la parte delante de la arroba @) pero con dominio ceu.es.

correo = input("Ingrese una direccion de correo: ")

correo_nuevo = correo[:correo.find("@")+1] + "ceu.es"

print(correo_nuevo)


# Escribir un programa que pregunte por consola por los productos de una cesta 
# de la compra, separados por comas, y muestre por pantalla cada uno de los 
# productos en una línea distinta.

productos = input("Ingrese una lista de productos separados por coma: ")

print(productos.replace(",","\n"))

"""
# Escribir un programa que pregunte el nombre el un producto, su precio y un 
# número de unidades y muestre por pantalla una cadena con el nombre del 
# producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el 
# número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 
# 2 decimales.}

prducto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio: "))
cantidad = int(input("Ingrese el numero de unidades: "))

print(f"Nombre del producto: {prducto}\tPrecio unitario: {precio:9.2f}")
print(f"Numero de unidades: {cantidad}\tCoste total: {(int(precio)*int(cantidad)):10.2f}")



