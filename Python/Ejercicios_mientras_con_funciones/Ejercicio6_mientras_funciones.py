#Crea un programa que pida al usuario una contraseña, de forma repetitiva mientras 
#que no introduzca "1234". Cuando finalmente escriba la contraseña correcta, 
#se le dirá "Bienvenido" y terminará el programa.

def pedir_contraseña():
    contraseña = input("Introduce la contraseña: ")
    return contraseña

def verificar_contraseña(contraseña):
    return contraseña == "1234"

def main():
    while True:
        contraseña_ingresada = pedir_contraseña()
        if verificar_contraseña(contraseña_ingresada):
            print("¡Bienvenido!")
            break

##################codigoPrincipal#########################
main()
