#Crear un algoritmo que suma n números positivos y cuenta los negativos mientras el numero ingresado sea diferente de cero.
def pedir_datos():
    dato=int(input("Digite un numero: "))
    return dato

def sumar_positivos(dato,suma):
    #acumulador para sumar
    if dato>0:
        suma+=dato
               
    return suma
def contar_negativos(dato,cont):
    #contador de negativos
    if dato<0:
        cont+=1
    return cont
def resultados(sum,cont):
    print("Los resultados son: ",sum," y ",cont)
    
###########################CODIGO PRINCIPAL###########################
suma_positivos=0
conta_negativos=0
numero=1

while numero!=0:
    numero=pedir_datos()
    suma_positivos=sumar_positivos(numero,suma_positivos)
    conta_negativos=contar_negativos(numero,conta_negativos)
resultados(suma_positivos,conta_negativos)
    
    
    
