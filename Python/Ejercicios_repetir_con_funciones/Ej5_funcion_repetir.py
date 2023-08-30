""" Haz un programa que permita calcular la suma de pares de números. 
Pedirá dos números al usuario y mostrará su suma, volviendo a repetir 
hasta que ambos números introducidos sean 0."""

def pedir_numero(mensaje):
    numero = int(input(mensaje))
    return numero

def sumar_numeros(num1, num2):
    suma = num1 + num2
    return suma

def main():
    while True:
        numero1 = pedir_numero("Ingresa el primer número (0 para salir): ")
        numero2 = pedir_numero("Ingresa el segundo número (0 para salir): ")
        
        if numero1 == 0 and numero2 == 0:
            print("¡Hasta luego!")
            break
        
        suma = sumar_numeros(numero1, numero2)
        print("La suma de los números es:", suma)

###########################codigoprincipal######################
main()
