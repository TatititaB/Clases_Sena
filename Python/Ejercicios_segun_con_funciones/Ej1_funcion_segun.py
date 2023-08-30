#Desarrollar un algoritmo que, dado un número; indique su equivalente en el día de la semana.

def pedir_dato():
    num=int(input("Digite un numero del 1 al 7 para darte un resultado "))
    
    return num
def saber_dia_semana(dato_semana):
    
    if dato_semana>0 and dato_semana<8:
        match dato_semana:
            case 1:
                x="Dia Lunes"
            case 2:
                x="Dia Martes"
            case 3:
                x="Dia miercoles"
            case 4:
                x="Dia Jueves"
            case 5:
                x="Dia Viernes"
            case 6:
                x="Dia Sabado"
            case 7:
                x="Dia Domingo"
                
    else:
        x="numero incorrecto"
        
    return x
def imprimir(resultado_final):
    print(resultado_final)
    
######################codigoPrincipal#################################   
digito=pedir_dato()
saber=saber_dia_semana(digito)
imprimir(saber)