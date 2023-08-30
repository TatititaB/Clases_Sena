#Pedir diez números por teclado y realiza la suma de los diez.

def pedir_numero(indice):
    numero = int(input(f"Digite el {indice} número: "))
    return numero

def pedir_diez_numeros():
    numeros = []
    for i in range(1, 11):
        numero = pedir_numero(i)
        numeros.append(numero)
    return numeros

def calcular_suma(numeros):
    suma = sum(numeros)
    return suma

######################codigoPrincipal#################################
suma = 0
print("Digite 10 números y los sumaré: ")
numeros_ingresados = pedir_diez_numeros()
suma_total = calcular_suma(numeros_ingresados)
print("El resultado de la suma es:", suma_total)
