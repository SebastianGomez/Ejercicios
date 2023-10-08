"""Crea una única función (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
"""

poligono = input ("Elija el poligono a calcular: ")
base = int(input ("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))

  
def area (poligono,base,altura):
    if poligono == "triangulo":
        print ("El área del triangulo es:",base*altura/2)
    elif poligono == "cuadrado":
        print ("El área del cuadrado es:",base*altura)
    elif poligono == "rectangulo":
        print ("El área del rectangulo es:",base*altura)
    else:
        print("el poligono ingresado es incorrecto")

area (poligono,base,altura)

"""mejoras posibles:
    * que detecte si el poligono es incorrecto antes de pedir mas datos
    * que de un mensaje de error si la base o la altura ingresadas no son un numero
"""


