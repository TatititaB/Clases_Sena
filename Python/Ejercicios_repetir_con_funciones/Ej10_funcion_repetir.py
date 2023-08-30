"""Realice el diseño de un algoritmo que entregue el término enésimo de la 
serie de Fibonacci (Tomar el número n a partir de cero)"""

def calcular_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]

def pedir_termino():
    n = int(input("Ingresa el término n de la serie de Fibonacci (a partir de 0): "))
    return n

def main():
    termino = pedir_termino()
    resultado = calcular_fibonacci(termino)
    print(f"El término {termino} de la serie de Fibonacci es: {resultado}")

#################codigo principal##################################
main()
