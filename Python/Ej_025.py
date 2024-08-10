# Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
# ¿De cuántas maneras eres capaz de hacerlo?
 

def forma1():
    for n in range(1,101):
        print(n)


def forma2():
    n=0
    while True:
        n=n+1
        print(n)
        if n ==100:
            break
    

def forma3(num:1):
    bandera = True
    while bandera:
        print(numero)
        numero = forma3(numero+1)
        if numero>10:
            bandera=False






forma3(1)
