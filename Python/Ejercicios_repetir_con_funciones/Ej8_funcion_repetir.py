"""Diseña un algoritmo que permita leer dos números enteros positivos y luego 
determine el mínimo común múltiplo de dichos números."""
def pedir_numero(mensaje):
    numero = int(input(mensaje))
    return numero

def calcular_mcm(num1, num2):
    mcm = (num1 * num2) // calcular_mcd(num1, num2)
    return mcm

def calcular_mcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

def main():
    numero1 = pedir_numero("Ingresa el primer número: ")
    numero2 = pedir_numero("Ingresa el segundo número: ")
    
    mcm = calcular_mcm(numero1, numero2)
    
    print("El mínimo común múltiplo de", numero1, "y", numero2, "es:", mcm)

#########################codigoprincipal#############################
main()
