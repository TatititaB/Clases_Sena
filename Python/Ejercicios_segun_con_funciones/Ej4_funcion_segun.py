#Crea un programa donde se solicite al usuario que introduzca el tipo de bomba para una máquina, pudiendo introducir valores enteros comprendidos entre 0 y 4. 
# Según el valor introducido por el usuario debe mostrarse el siguiente resultado usando un condicional switch: 
#a) Si el tipo de bomba es 0, mostrar un mensaje por consola indicando “No hay establecido un valor definido para el tipo de bomba”. 
#b) Si el tipo de bomba es 1, mostrar un mensaje por consola indicando “La bomba es una bomba de agua”. 
#c) Si el tipo de bomba es 2, mostrar un mensaje por consola indicando “La bomba es una bomba de gasolina”. 
#d) Si el tipo de bomba es 3, mostrar un mensaje por consola indicando “La bomba es una bomba de hormigón”.
#e) Si el tipo de bomba es 4, mostrar un mensaje por consola indicando “La bomba es una bomba de pasta alimenticia”. 
#f) Si no se cumple ninguno de los valores anteriores mostrar el mensaje “No existe un valor válido para tipo de bomba

def menu():
    print("\t ###\tBombas\t### \t")
    print("Seleccione uno de los tipos de bomba para maquina: y escoja un numero del 1 al 4 ")
    opcion=int(input("opcion que escojas te la dire:"))
    opcion_que_tomo(opcion)
    return opcion

def opcion_que_tomo(opc):
    
    if opc>=0 and opc<5:
        match opc:
            case 0:
                
                return "No hay establecido un valor definido para el tipo de bomba"
            case 1:
                return "La bomba es una bomba de agua"
                
            case 2:
                return "La bomba es una bomba de gasolina"
                
            case 3:
                return "La bomba es una bomba de hormigón"
                
            case 4:
                return "La bomba es una bomba de pasta alimenticia"
  
                
    else:
        return "No existe un valor válido para tipo de bomba"
def imprimir(resultado):
    print(resultado)
######################codigoPrincipal#################################
este_es=menu()
aqui=opcion_que_tomo(este_es)
imprimir(aqui)