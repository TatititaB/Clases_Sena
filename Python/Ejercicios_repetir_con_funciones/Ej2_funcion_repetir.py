"""Crear un algoritmo que valide que un usuario ingrese 
un número positivo (mayor que cero)."""

def pedir_numero():
    numero = int(input("Ingresa un número: "))
    return numero

def validar_numero_positivo(numero):
    return numero > 0

def main():
    while True:
        numero_ingresado = pedir_numero()
        if validar_numero_positivo(numero_ingresado):
            print("Número válido. ¡Gracias!")
            break
        else:
            print("Número inválido. Ingresa un número positivo.")
######################codigoPrincipal#################################
main()