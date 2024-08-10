"""
# Escribir una función que aplique un descuento a un precio y otra que aplique 
# el IVA a un precio. Escribir una tercera función que reciba un diccionario con 
# los precios y porcentajes de una cesta de la compra, y una de las funciones 
# anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a 
# los productos de la cesta y devolver el precio final de la cesta.

precio = 1000
desc = 15
iva = 21
def descuento (precio,desc):
    
    return  precio - desc*precio/100
    


def impuesto(precio,iva):
    
    return precio + precio*iva/100



compra = {"Producto":"Pelota","Precio":1000,"Descuento":f"{desc}%","Impuestos":f"{iva}%","Precio final":int}

def factura(compra):
    
    total = impuesto(descuento(precio,desc),iva)
    
    compra["Precio final"] = total

    return compra

print(factura(compra))

"""


