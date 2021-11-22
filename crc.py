#alumni.cs.ucr.edu/~saha/stuff/crc.htm
#https://www.w3schools.com/python/python_ref_string.asp
#https://www.geeksforgeeks.org/type-conversion-python/
#https://www.youtube.com/watch?v=53M_SblKTPY&ab_channel=FocusUs
#https://en.wikipedia.org/wiki/Cyclic_redundancy_check#Mathematics
import numpy as np

def xor(a, b):
 
    result = []
 
    #Hace una operación XOR para cada uno de los bits en a y b
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
 
    return ''.join(result)
 
 
# realiza la división
def mod2div(dividendo, divisor):
 
    # Número de bits a los cuáles se les va a realizar la operación
    # cada vez.
    pick = len(divisor)
 
    # Se parte dividendo para ser del tamaño apropiado
    #para la operación
    tmp = dividendo[0 : pick]
 
    while pick < len(dividendo):
 
        if tmp[0] == '1':
 
            # remplaza dividendo por el resultado de XOR
            tmp = xor(divisor, tmp) + dividendo[pick]
 
        else: # si el bit de hasta la izquierda es '0'
 
            # Si el bit de hasta la izquiera (el que se va a usar)
            # es 0 entonces no podemos hacer la división normal
            # tenemos que hacer que el dividendo sea de puros 0's
            tmp = xor('0'*pick, tmp) + dividendo[pick]
 
        # Se incrementa pick para avanzar
        pick += 1
 
    # El último bit se tiene que hacer de esta forma
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)
 
    checkword = tmp
    return checkword
 
# Codifica el mensaje y le añade el resultado de la
#operación modulo binaria
def codificarDatos(datos, key):
 
    l_key = len(key)
 
    # Appends n-1 zeroes at end of data
    datosConCeros = datos + '0'*(l_key-1)
    resto = mod2div(datosConCeros, key)
 
    # Append remainder in the original data
    resultado = datos + resto
    return resultado 

def decodeData(datos, key):
 
    l_key = len(key)
 
    appended_data = datos + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
 
    return remainder

input_string = input("Ingrese la cadena que quiere codificar: ")

data =(''.join(format(ord(x), 'b') for x in input_string))
print("Cadena ingresada en formato binario :",data)
key = "1001"
 
ans = codificarDatos(data,key)
print("Cadena ingresada codificada mediante CRC :",ans)

print("Resultado (residuo) de decodificar los datos: ",decodeData(ans,key))

print("A continuación se lanzará un error en alguna "+
"posición y se determinará que hay un error al tratar de decodificarla si da "+
"un valor diferente a cero")

rand = np.random.randint(0,len(ans))
ans = ans[0:rand - 1] + '0' if ans[rand] == '1' else '0' + ans[rand + 1: len(ans) - 1]

print("Resultado (residuo) de decodificar los datos: ",decodeData(ans,key))
