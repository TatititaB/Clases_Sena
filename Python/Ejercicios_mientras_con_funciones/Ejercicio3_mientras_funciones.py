#Pedir números por teclado hasta que se ingrese un numero negativo, 
#al final debe mostrar los números positivos introducidos sin contar el negativo

#funcion para pedir datos
def pedir_datos():
    numero=int(input("Digita un numero: "))
    return numero

def comprobacion():
    #vector para guardar los numeros
    numeros_positivos_contados=[]
    while True:
        dato=pedir_datos()
        if dato<0:
            break
        numeros_positivos_contados.append(dato)
    return numeros_positivos_contados
    
def imprimir_resultados(dato_robusto):
    print("los numeros digitados son: ")
    for num in dato_robusto:
        print(num)

########################codigo principal########################
dato=comprobacion()
imprimir_resultados(dato)