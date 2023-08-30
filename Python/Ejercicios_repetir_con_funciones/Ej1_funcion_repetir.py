"""Crear un programa que pida al usuario una clave de acceso, y que no 
le permita seguir hasta que la introduzca correctamente"""

def pedir_datos():
    print("Digita tu clave: ")
    dato=int(input())
    correcto(dato)
def correcto(dato):
    clave=1234
    if clave==dato:
        print("Clave Correcta")
    else:
        incorrecto()
def incorrecto():
    print("Esta incorrecto")
    pedir_datos()

##############CodigoPrincipal##############
pedir_datos()

