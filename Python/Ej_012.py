# Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima 
# otras dos cadenas como salida (out1, out2).
# - out1 contendrá todos los caracteres presentes en la str1 pero NO estén 
# presentes en str2.
# - out2 contendrá todos los caracteres presentes en la str2 pero NO estén 
# presentes en str1.

str1 = "la casa por la ventana"
str2 = "amanece mas temprano1"


def funcion(str1,str2):
    out1 = ""
    out2 = ""
    for n in str2:
        if n not in str1:
            if n not in out1:
                out1 = out1 + n
    for n in str1:
        if n not in str2:
            if n not in out2:
                out2 = out2 + n
    print(out1)
    print(out2)

funcion(str1,str2)
