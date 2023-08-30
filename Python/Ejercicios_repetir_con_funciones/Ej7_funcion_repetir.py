"""Diseña un algoritmo que permita leer dos números enteros positivos y luego 
determine el máximo común divisor de dichos números."""

def pedir_numero(mensaje):
    numero = int(input(mensaje))
    return numero

def calcular_mcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

def main():
    numero1 = pedir_numero("Ingresa el primer número: ")
    numero2 = pedir_numero("Ingresa el segundo número: ")
    
    mcd = calcular_mcd(numero1, numero2)
    
    print("El máximo común divisor de", numero1, "y", numero2, "es:", mcd)

#####################codigoprincipal###############
main()
