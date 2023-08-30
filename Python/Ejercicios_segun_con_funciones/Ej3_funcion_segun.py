#Desarrollar un algoritmo que pida dos números, y se debe elegir 4 opciones para operarlos, sumar, restar, dividir, y multiplicar, depende la que se elija. 

def menu_operaciones():
    print("\t ###\tMENU\t### \t")
    print("(1) Para sumar")
    print("(2) Para restar")
    print("(3) Para multiplicar")
    print("(4) Para dividir")
    opcion=int(input("Seleccione una de las opciones segun su necesidad:"))
    opcion_que_tomo(opcion)
    return opcion
def pedir_datos_suma():
    num1=int(input("Digite el primer dato: "))
    num2=int(input("Digite el segundo dato: "))
    resultado_suma=suma(num1,num2)
    print(resultado_suma)
def pedir_datos_resta():
    num1=int(input("Digite el primer dato: "))
    num2=int(input("Digite el segundo dato: "))
    resultado_resta=resta(num1,num2)
    print(resultado_resta)
def pedir_datos_multiplicacion():
    num1=int(input("Digite el primer dato: "))
    num2=int(input("Digite el segundo dato: "))
    resultado_multiplicacion=multiplicacion(num1,num2)
    print(resultado_multiplicacion)
def pedir_datos_division():
    num1=int(input("Digite el primer dato: "))
    num2=int(input("Digite el segundo dato: "))
    resultado_division=division(num1,num2)
    print(resultado_division)
def suma(n1,n2):
    sum=n1+n2  
    return sum
def resta(n1,n2):
    res=n1-n2  
    return res
def multiplicacion(n1,n2):
    mult=n1*n2  
    return mult
def division(n1,n2):
    div=n1/n2  
    return div
def opcion_que_tomo(opc):    
    if opc>0 and opc<5:
        match opc:
            case 1:
                
                return pedir_datos_suma()
                
            case 2:
                return pedir_datos_resta()
                
            case 3:
                return pedir_datos_multiplicacion()
                
            case 4:
                return pedir_datos_division()
                
    else:
        print("Opcion incorrecta")
                
######################codigoPrincipal#################################
menu_operaciones()                