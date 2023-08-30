##Crea un programa que genere dos números al azar entre el 0 y el 100, 
#y pida al usuario que calcule e introduzca su suma. 
#Si la respuesta no es correcta, deberá volver a pedirla tantas veces 
#como sea necesario hasta que el usuario acierte.

import random
#importamos la libreria random para generar numeros al azar

def generar_numeros():
    numero1 = random.randint(0, 100)
    numero2 = random.randint(0, 100)
    return numero1, numero2

def pedir_suma():
    #realizamos la suma
    suma = int(input("Introduce la suma de los dos números: "))
    return suma

def main():
    numero1, numero2 = generar_numeros()
    
    while True:
        suma_esperada = numero1 + numero2
        suma_ingresada = pedir_suma()
        
        if suma_ingresada == suma_esperada:
            print("¡Respuesta correcta! ¡Bien hecho!")
            break
        else:
            print("Respuesta incorrecta. Intenta de nuevo.")

################codigo principal####################
main()