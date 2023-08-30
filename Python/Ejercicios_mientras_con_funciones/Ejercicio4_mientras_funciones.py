#Crear un algoritmo donde pedimos dos números por teclado y 
#mostramos todos los números comprendidos entre ambos números.

def pedir_2_numeros():
    print("Digita dos numeros y te muestro los numeros comprendidos entre ambos:")
    dato1=int(input())
    dato2=int(input())
    return dato1,dato2
def calculo(dato1,dato2):
    if dato1<dato2:
        inicio=dato1
        fin=dato2
    else:
        inicio=dato2
        fin=dato1
    print("Estos son los numeros comprendidos entre ambos: ")
    for contador in range(inicio,fin+1):
        print (contador)
    return contador
def main():
    n1,n2=pedir_2_numeros()
    print("\n")
    calculo(n1,n2)
    
########################CODIGOPRINCIPAL###############################
main()