#Desarrollar un algoritmo que nos muestre un menú de 7 opciones, dependiendo la que realice debe realizar un ejercicio por opción:
#1. Que pida un número del 1 al 5 y diga si es primo o no. 
#2. Que pida u9n número y diga si es par o impar. 
#3. Que pida un número del 1 al 7 y diga el día de la semana correspondiente. 
#4. Que pida un número del 1 al 12 y diga el nombre del mes correspondiente. 
#5. Que pida 3 números y los muestre en pantalla de menor a mayor. 
#6. Que pida 3 números y los muestre en pantalla de mayor a menor. 
#7. Que pida 3 números y los muestre en pantalla de mayor a menor en líneas distintas. En caso de haber números iguales se pintan en la misma línea. 
#8. Que pida una letra y detecte si es una vocal.

def menu_de_opciones():
    print("\t ***MENU***\t")
    print("Selecciona la opcion que mas gustes:")
    print("(1) si quieres saber si un numero es primo o no")
    print("(2) si quieres saber si un numero es par o impar")
    print("(3) dame un numero del 1 al 7 y te digo el dia de la semana que corresponde")
    print("(4) dame un numero del 1 al 12 y te digo el nombre del mes correspondiente")
    print("(5) dame 3 numeros y te los mostrare de menor a mayor")
    print("(6) dame 3 numeros y te los mostrare de mayor a menor")
    print("(7) dame 3 numeros y te los mostrare de mayor a menor en lineas distintas y si hay numeros iguales, estaran en la misma linea")
    print("(8) dame una letra y te dire si es una vocal")
def seleccion():   
    opc=input()
    return opc
def seleccion_opcion(opc):
    #opc=int (seleccion())
    match opc:
        case 1:
            print("Ingrese un numero: ")
            numero1=int(seleccion())
            numero_primo(numero1)
        case 2:
            print("Ingrese un numero: ")
            numero1=int(seleccion())
            numero_par_o_impar(numero1)
        case 3:
            print("Ingrese un numero: ")
            numero1=int(seleccion())
            dia_de_la_semana(numero1)
        case 4:
            print("Ingrese un numero: ")
            numero1=int(seleccion())
            meses_del_amo(numero1)
        case 5:
            print("Ingrese tres numeros: ")
            numero1=int(seleccion())
            numero2=int(seleccion())
            numero3=int(seleccion())
            menor_a_mayor(numero1,numero2,numero3)
        case 6:
            print("Ingrese tres numeros: ")
            numero1=int(seleccion())
            numero2=int(seleccion())
            numero3=int(seleccion())
            mayor_a_menor(numero1,numero2,numero3)
        case 7:
            print("Ingrese tres numeros: ")
            numero1=int(seleccion())
            numero2=int(seleccion())
            numero3=int(seleccion())
            mayor_a_menor_lineas_distintas(numero1,numero2,numero3)
        case 8:
            print("ingrese un valor: ")
            valor=input()
            letra_si_es_vocal(valor)
def numero_primo(num):
    cont=0
    for i in range (1,num):
        if num%i==0:
            cont=cont+1
    if cont<=2:
        print("El numero es primo")
    else:
        print("El numero no es primo")
def numero_par_o_impar(numero):
    if numero%2==0:
        print("El numero es par")
    else:
        print("El numero es impar")
def dia_de_la_semana(numero):
    match numero:
        case 1:
            print("Dia lunes")
        case 2:
            print("Dia martes")
        case 3:
            print("Dia miercoles")
        case 4:
            print("Dia jueves")
        case 5:
            print("Dia viernes")
        case 6:
            print("Dia sabado")
        case 7:
            print("Dia domingo")
        case _:
            print("**Ha seleccionado un valor invalido**")
def meses_del_amo(numero):
    match numero:
        case 1:
            print("Enero")
        case 2:
            print("Febrero")
        case 3:
            print("Marzo")
        case 4:
            print("Abril")
        case 5:
            print("Mayo")
        case 6:
            print("Junio")
        case 7:
            print("Julio")
        case 8:
            print("Agosto")
        case 9:
            print("Septiembre")
        case 10:
            print("Octubre")
        case 11:
            print("Noviembre")
        case 12:
            print("Diciembre")
        case _:
            print("**Ha seleccionado un valor invalido**")
def menor_a_mayor(valor_1,valor_2,valor_3):
    if valor_1>valor_2 and valor_2>valor_3:
        print("Los numeros son: ",valor_3,valor_2,valor_1)
    elif valor_1>valor_3 and valor_3>valor_2:
        print("Los numeros son: ",valor_2,valor_3,valor_1)
    elif valor_2>valor_1 and valor_1>valor_3:
        print("Los numeros son: ",valor_3,valor_1,valor_2)
    elif valor_2>valor_3 and valor_3>valor_1:
        print("Los numeros son: ",valor_1,valor_3,valor_2)
    elif valor_3>valor_1 and valor_1>valor_2:
        print("los numero son: ",valor_2,valor_1,valor_3)
    elif valor_3>valor_2 and valor_2>valor_1:
        print("los valores son: ",valor_1,valor_2,valor_3)
        #AQUI TODOS LOS  VALORES SON IGUALES
    elif valor_1==valor_2 and valor_2==valor_3:
        print("Todos los Valores son iguales no los podemos comparar")
        #AQUI HAY 2 IGUALES Y 1 DIFERENTE
    elif valor_1==valor_2 and valor_2>valor_3:
        print("El primer y segundo valor que digitaste son iguales y en orden de los numeros diferentes seria ",valor_2,valor_3)
    elif valor_2==valor_3 and valor_3>valor_1:
        print("el segundo y tercer valor que digitaste son iguales y en orden de los numeros diferentes seria ",valor_1,valor_3)
def mayor_a_menor(valor_1,valor_2,valor_3):
    if valor_1>valor_2 and valor_2>valor_3:
        print("Los numeros son: ",valor_1,valor_2,valor_3)
    elif valor_1>valor_3 and valor_3>valor_2:
        print("Los numeros son: ",valor_1,valor_3,valor_2)
    elif valor_2>valor_1 and valor_1>valor_3:
        print("Los numeros son: ",valor_2,valor_1,valor_3)
    elif valor_2>valor_3 and valor_3>valor_1:
        print("Los numeros son: ",valor_2,valor_3,valor_1)
    elif valor_3>valor_1 and valor_1>valor_2:
        print("los numero son: ",valor_3,valor_1,valor_2)
    elif valor_3>valor_2 and valor_2>valor_1:
        print("los valores son: ",valor_3,valor_2,valor_1)
        #AQUI TODOS LOS  VALORES SON IGUALES
    elif valor_1==valor_2 and valor_2==valor_3:
        print("Todos los Valores son iguales no los podemos comparar")
        #AQUI HAY 2 IGUALES Y 1 DIFERENTE
    elif valor_1==valor_2 and valor_2>valor_3:
        print("El primer y segundo valor que digitaste son iguales y en orden de los numeros diferentes seria ",valor_3,valor_2)
    elif valor_2==valor_3 and valor_3>valor_1:
        print("el segundo y tercer valor que digitaste son iguales y en orden de los numeros diferentes seria ",valor_3,valor_1)
def mayor_a_menor_lineas_distintas(valor_1,valor_2,valor_3):
    
    print("*****************************************")

    if valor_1>valor_2 and valor_2>valor_3:
        print("Los numeros son: ",valor_1)
        print("Los numeros son: ",valor_2)
        print("Los numeros son: ",valor_3)
    elif valor_1>valor_3 and valor_3>valor_2:
        print("Los numeros son: ",valor_1)
        print("Los numeros son: ",valor_3)
        print("Los numeros son: ",valor_2)
    elif valor_2>valor_1 and valor_1>valor_3:
        print("Los numeros son: ",valor_2)
        print("Los numeros son: ",valor_1)
        print("Los numeros son: ",valor_3)
    elif valor_2>valor_3 and valor_3>valor_1:
        print("Los numeros son: ",valor_2)
        print("Los numeros son: ",valor_3)
        print("Los numeros son: ",valor_1)
    elif valor_3>valor_1 and valor_1>valor_2:
        print("Los numeros son: ",valor_3)
        print("Los numeros son: ",valor_1)
        print("Los numeros son: ",valor_2)
    elif valor_3>valor_2 and valor_2>valor_1:
        print("Los numeros son: ",valor_3)
        print("Los numeros son: ",valor_2)
        print("Los numeros son: ",valor_1)
    elif valor_1==valor_2 and valor_2==valor_3:
        print("los valores son: ",valor_1,valor_2,valor_3)
    elif valor_1==valor_2 and valor_2>valor_3:
        print("los valores son: ",valor_1,valor_2)
        print("Los numeros son: ",valor_3)
    elif valor_1==valor_3 and valor_1>valor_2:
        print("los valores son: ",valor_1,valor_3)
        print("Los numeros son: ",valor_2)
    elif valor_2==valor_3 and valor_3>valor_1:
        print("los valores son: ",valor_3,valor_2)
        print("Los numeros son: ",valor_1)
    elif valor_1==valor_2 and valor_2<valor_3:
        print("Los numeros son: ",valor_3)
        print("los valores son: ",valor_1,valor_2)
    elif valor_1==valor_3 and valor_1<valor_2:
        print("Los numeros son: ",valor_2)
        print("los valores son: ",valor_1,valor_3)
    elif valor_2==valor_3 and valor_3<valor_1:
        print("Los numeros son: ",valor_1)
        print("los valores son: ",valor_3,valor_2)
    print("*****************************************")        
def letra_si_es_vocal(valor):
    if valor=="a" or valor=="A" or valor=="e" or valor=="E" or valor=="i" or valor=="I" or valor=="o" or valor=="O" or valor=="u" or valor=="U":
        print("Esta es una vocal: ",valor)
    else:
        print("Es una letra: ",valor)




##################################CODIGO PRINCIPAL######################################
menu_de_opciones()
opc=int(seleccion())
seleccion_opcion(opc)