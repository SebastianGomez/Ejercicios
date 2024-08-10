
# Escribe una función que calcule si un número dado es un número de Armstrong
 
#Un numero armstrong es aquel numero que al separar sus dígitos, elevarlos a la 
# cuarta a cada uno y luego sumarlos dan el numero que eran loa dígitos juntos. 
# Ejemplo: 8028



numero = 8208

def armstrong(numero):
    aux = str(numero)
    resultado = 0
    for n in aux:
        aux2 = int(n)
        resultado = aux2**4 + resultado
    if numero == resultado:
        print(f"El numero {numero} es un numero de Armstrong")
    else:
        print(f"El numero {numero} no es un numero de Armstrong")

armstrong(numero)