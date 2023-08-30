"""Escribir un algoritmo que lea un vector con n posiciones, 
y diga cuantos números repetidos existen, dado el caso."""

def leer_vector():
    n = int(input("Ingrese el tamaño del vector: "))
    vector = []
    for i in range(n):
        num = int(input(f"Ingrese el elemento {i + 1}: "))
        vector.append(num)
    return vector

def contar_numeros_repetidos(vector):
    contador = {}
    for num in vector:
        if num in contador:
            contador[num] += 1
        else:
            contador[num] = 1
    repetidos = sum(1 for count in contador.values() if count > 1)
    return repetidos

def main():
    vector = leer_vector()
    numeros_repetidos = contar_numeros_repetidos(vector)
    print(f"Hay {numeros_repetidos} números repetidos en el vector.")

########################codigo principal#############################
main()
