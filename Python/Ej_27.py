
""" Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
- Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
"""


#figura = input("Ingrese la figura: ")
#tamaño = input("Ingrese el tamaño: ")


def dibujo(figura,tamaño):
    if (figura == "cuadrado"):
        for n in range(0,tamaño):
            print("*"*tamaño)
        
    
    elif (figura == "triangulo"):
        
        for n in range(0,tamaño):
            print(" "*(tamaño) + "*"*n)
        


dibujo("triangulo",7)