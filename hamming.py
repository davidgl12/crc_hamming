import numpy as np
from functools import reduce

def estandarizarLongitud(bits):
    nueva = ""
    if(len(bits) == 5):
        nueva = bits[2:]
        nueva = "0b0" + nueva
    elif(len(bits) == 4):
        nueva = bits[2:]
        nueva = "0b00" + nueva
    elif(len(bits) == 3):
        nueva = bits[2:]
        nueva = "0b000" + nueva
    else:
        return bits
    return nueva


#crea 16 bits aleatorios
bits = np.random.randint(0, 2, 16)

print("Los datos que se van a trabajar son: ", bits)
#los pone en una lista con un index para cada valor
lista = enumerate(bits)

#Okey, esto es algo complicado pero sumamente bello:
#Primero itera los índices (i) y los bits (bit) de la lista, pero
#sólamente devuelve los índices (i) correspondientes a las posiciones en
#las que se encuentra un 1, sigues conmigo? bien
#Entonces, para cada una de estar posiciones i, se les aplica un xor
# y al final es lo que devuelve la función, chido, no?
localizador = reduce(lambda x, y: x ^ y, [i for i, bit in lista if bit])
localizador = bin(localizador)

#La representacion binaria de nuestra variable localizador nos va a decir
#que bits de paridad tenemos que invertir para poder convertir nuestro bloque
#original de datos binarios en un bloque de datos hamming, el cual nos puede 0b1010
#ayudar a detectar errores y en donde se encuentran
localizador = estandarizarLongitud(localizador)
if(localizador[2] == "1"):
    bits[8] = not bits[8]
if(localizador[3] == "1"):
    bits[4] = not bits[4]
if(localizador[4] == "1"):
    bits[2] = not bits[2]
if(localizador[5] == "1"):
    bits[1] = not bits[1]

#En este punto, bits ya se convirtió a un bloque de código hamming de 11 bits, ahora si hacemos
#la misma operación de arriba, debería de dar cero o la posición en donde se encuentra el error:
localizador = reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bits) if bit])
print(localizador)
print( "Efectivamente, no hay errores" if localizador == 0 else "Esto no se supone que debe de pasar")
print("A continuación, se va a alterar un bit en un lugar aleatorio de los datos y el código hamming nos dirá donde está")

rand = np.random.randint(0,len(bits))
bits[rand] = not bits[rand]
print("Error lanzado, buscando posición del bit...")

localizador = reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bits) if bit])
print("El error está en la posición ", localizador, " cambiando el bit en esa posición...")
bits[localizador] = not bits[localizador]

localizador = reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(bits) if bit])
print( "Se corrigió el error" if localizador == 0 else "Esto no se supone que debe de pasar")