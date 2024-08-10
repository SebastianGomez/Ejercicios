# Escribe una función que calcule y retorne el factorial de un número dado
# de forma recursiva.



def factorial(numero):

    factorial = 1
    i = 1
   
    while i <= numero:
        factorial = factorial*i
        i+=1

    return factorial
        
print(factorial(4))
