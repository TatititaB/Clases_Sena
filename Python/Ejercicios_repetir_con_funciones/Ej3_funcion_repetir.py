""" Crear un algoritmo para validar que un usuario ingrese un número positivo de 5 cifras."""

def pedir_numero():
    numero = int(input("Ingresa un número de 5 cifras: "))
    return numero

def validar_numero_positivo(numero):
    return numero > 0

def validar_cinco_cifras(numero):
    return 10000 <= numero <= 99999

def main():
    while True:
        numero_ingresado = pedir_numero()
        if validar_numero_positivo(numero_ingresado) and validar_cinco_cifras(numero_ingresado):
            print("Número válido. ¡Gracias!")
            break
        else:
            print("Número inválido. Ingresa un número positivo de 5 cifras.")
######################codigoPrincipal#################################
main()