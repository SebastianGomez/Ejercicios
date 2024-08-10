"""
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo 
# Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por 
# pantalla.

asignaturas = ["Matematica","Fisica","Quimica","Historia","Lengua"]
print(asignaturas)

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo 
# Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por 
# pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de 
# las asignaturas de la lista.

print("Yo estudio: ")
for i in asignaturas:
    print(f"\t{i}")

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo 
# Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al 
# usuario la nota que ha sacado en cada asignatura, y después las muestre por 
# pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> 
# es cada una des las asignaturas de la lista y <nota> cada una de las 
# correspondientes notas introducidas por el usuario.

notas = []

for i in asignaturas:
    notas.append(int(input(f"Ingrese la nota de {i}: ")))

for i in range(len(asignaturas)):
    print(f"En la materia {asignaturas[i]} sacaste un {notas[i]}")
#se podria hacer mejor con diccionarios

# Escribir un programa que pregunte al usuario los números ganadores de la 
# lotería primitiva, los almacene en una lista y los muestre por pantalla 
# ordenados de menor a mayor.

num_loteria = input("Ingrese los numeros de la loteria: ")

num_ordenados = sorted(num_loteria)

print("".join(num_ordenados))

# Escribir un programa que almacene en una lista los números del 1 al 10 y los 
# muestre por pantalla en orden inverso separados por comas.

num = [1,2,3,4,5,6,7,8,9,10]

for i in reversed(num):
    print(i)

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo 
# Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al 
# usuario la nota que ha sacado en cada asignatura y elimine de la lista las 
# asignaturas aprobadas. Al final el programa debe mostrar por pantalla las 
# asignaturas que el usuario tiene que repetir.

asignaturas = ["Matematica","Fisica","Quimica","Historia","Lengua"]
asignaturas_reprobadas = []
for i in asignaturas:
    
    nota = int(input(f"Ingrese la nota de {i}: "))
    if nota >=7:
        asignaturas_reprobadas.append(i)
    
print(asignaturas_reprobadas)



# Escribir un programa que almacene el abecedario en una lista, elimine de la 
# lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla 
# la lista resultante.

abecedario = "a,b,c,d,e,f,g,h,y,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"

lista = abecedario.split(",")
lista2 = []

for i in range(0,len(lista)):
    if i%3!=0:
        lista2.append(lista[i])

print(lista2)
     


# Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
# y devolver el total de la factura. Si se invoca la función sin pasarle el 
# porcentaje de IVA, deberá aplicar un 21%.

imp_sin_iva = 10000
iva = 50

def factura(imp_sin_iva,iva = 21):
    

    return imp_sin_iva+imp_sin_iva*(iva/100)

print(factura(imp_sin_iva))



# Escribir una función que calcule el área de un círculo y otra que calcule el 
# volumen de un cilindro usando la primera función.

radio = 50
PI = 3.1416
ALTURA = 10


def area_circulo(radio,PI):
    
    return PI*(radio**2)

def volumen_cilindro(ALTURA):
    return area_circulo(radio,PI)*ALTURA

print(area_circulo(radio,PI))
print(volumen_cilindro(ALTURA))



# Escribir una función que reciba una muestra de números en una lista y devuelva 
# su media.

lista = [1,2,3,4,5,6,7,8,9,10]

def media (lista):
    aux_media = 0
    for i in lista:
        aux_media+=i
    
    return aux_media/len(lista)   

print(media(lista))

"""

# Escribir una función que reciba una muestra de números en una lista y devuelva 
# otra lista con sus cuadrados.

lista = [1,2,3,4,5,6,7,8,9,10]

def cuadrados (lista):
    lis_cuadrados = []
    for i in lista:
        lis_cuadrados.append(i**2)
    
    return lis_cuadrados   

print(cuadrados(lista))
