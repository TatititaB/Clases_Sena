"""Crear un algoritmo que muestre una lista con 3 opciones: sumar 1 + 1, 
multiplicar 5 x 5 y salir y finalizar el algoritmo sí y solo sí se elija 
la opción para salir."""
def mostrar_menu():
    print("Opciones:")
    print("1. Sumar 1 + 1")
    print("2. Multiplicar 5 x 5")
    print("3. Salir")

def pedir_opcion():
    opcion = int(input("Elige una opción: "))
    return opcion

def main():
    while True:
        mostrar_menu()
        opcion = pedir_opcion()
        
        if opcion == 1:
            resultado = 1 + 1
            print("El resultado de 1 + 1 es:", resultado)
        elif opcion == 2:
            resultado = 5 * 5
            print("El resultado de 5 x 5 es:", resultado)
        elif opcion == 3:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Elige una opción del menú.")

###################codigoprincipal########################################
main()
