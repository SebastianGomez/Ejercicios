# Crea una función que reciba días, horas, minutos y segundos (como enteros)
 # y retorne su resultado en milisegundos

import unittest

def milisegundos(dias,horas,minutos,segundos):
    return segundos*1000 + minutos*60*1000 + horas*60*60*1000 + dias*24*60*60*1000


print(milisegundos(2,4,30,15))

class test(unittest.TestCase):
    # Test case 1: All inputs are zero
    assert milisegundos(0, 0, 0, 0) == 0

    # Test case 2: Only seconds are non-zero
    assert milisegundos(0, 0, 0, 10) == 10000

    # Test case 3: Only minutes are non-zero
    assert milisegundos(0, 0, 5, 0) == 300000

    # Test case 4: Only hours are non-zero
    assert milisegundos(0, 2, 0, 0) == 7200000

    # Test case 5: Only days are non-zero
    assert milisegundos(3, 0, 0, 0) == 259200000

    # Test case 6: All inputs are non-zero
    assert milisegundos(2, 4, 30, 15) == 189015000

    print("All test cases passed!")

prueba = test()


