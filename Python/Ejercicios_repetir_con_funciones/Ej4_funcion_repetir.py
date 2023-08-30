"""Crea un programa que pida al usuario un código de usuario y una contraseña. 
Deberá repetirse hasta que el código sea "1" y la contraseña sea "1234"."""

def pedir_codigo():
    codigo = input("Ingrese el código de usuario: ")
    return codigo

def pedir_contraseña():
    contraseña = input("Ingrese la contraseña: ")
    return contraseña

def validar_acceso(codigo, contraseña):
    return codigo == "1" and contraseña == "1234"

def main():
    while True:
        codigo_ingresado = pedir_codigo()
        contraseña_ingresada = pedir_contraseña()
        
        if validar_acceso(codigo_ingresado, contraseña_ingresada):
            print("¡Acceso concedido! Bienvenido.")
            break
        else:
            print("Acceso denegado. Intente nuevamente.")
######################codigoPrincipal#################################
main()
