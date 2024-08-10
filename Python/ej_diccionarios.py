# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 
# 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su 
# símbolo o un mensaje de aviso si la divisa no está en el diccionario.


diccionario = {"Euro":"€",
               "Dollar":"$",
               "Yen":"¥",}


consulta = input("Ingrese la divisa a buscar: ")


print(diccionario.get(consulta,"No se encuentra la divisa"))

