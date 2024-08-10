"""
Crea un programa se encargue de transformar un número decimal a binario sin 
utilizar funciones propias del lenguaje que lo hagan directamente.
"""
import doctest

def conv_dec (decimal):
    
    """
    Convierte un numero entero decimal a binario
    
    ,12,17,0,129]
    >>> conv_dec(25)
    '11001'
    >>> conv_dec(12)
    '1100'
    >>> conv_dec(0)
    '0'
    >>> conv_dec(129)
    '10000001'

    """
    
    resultado = []
    binario = []
    while decimal >=2:
        resultado.append(decimal%2)
        decimal = decimal//2
    
    resultado.append(decimal)
    
    while resultado:
        temp = resultado.pop()
        binario.append(str(temp)) #str es necesario para poder utilizar join mas adelante
    

    return ''.join(binario)

#help(conv_dec)
#doctest.testmod()

print(conv_dec(12))




