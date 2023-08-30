"""Realice un algoritmo que permita leer un número positivo. 
Luego indique si es un número perfecto."""
def pedir_numero():
    numero = int(input("Ingresa un número positivo: "))
    return numero

def es_numero_perfecto(numero):
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
    return suma_divisores == numero

def main():
    numero = pedir_numero()
    
    if numero <= 0:
        print("Por favor, ingresa un número positivo.")
    elif es_numero_perfecto(numero):
        print(numero, "es un número perfecto.")
    else:
        print(numero, "no es un número perfecto.")
#######################codigoprincipal########################
main()
