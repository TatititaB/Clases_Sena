"""Crear un codigo, un diccionario que contiene calificaciones de estudiantes. crea un programa que recorra
el diccionario, calcule el promedio de las califiaciones y determine si cada estudiante aprobo o reprobo (promedio igual o mayor a 60)"""

colegio={'estudiante1':{'nombre':"andres",'nota1':50,'nota2':80,'nota3':90},
         'estudiante2':{'nombre':"natalia",'nota1':30,'nota2':20,'nota3':50}}
#print(colegio)

# def calcularPromedio(col):
    # for i in range (len(col[estd[]])):
    #     for j in range (len(col[i])):
    #         print(j)

def notaFinal(promedio):
    if promedio>=60:
        mensaje="Aprobo"
        
    else:
        mensaje="Reprobo"
    
    return mensaje

def pedirDato():
    estudiante="estudiante"+input("Ingrese el numero del estudiante:")
    nombre=input("digite nombre: " )
    nota1=int(input("digite nota1: "))
    nota2=int(input("digite nota2: "))
    nota3=int(input("digite nota3: "))
    
    aux={estudiante:{'nombre':nombre,'nota1':nota1,'nota2':nota2,'nota3':nota3}}
    return aux
def actualizar(aux,colegio):
    colegio.update(aux)
    return colegio

    
#############################CODIGO PRINCIPAL#####################################
# while True:
#     opc=int(input("Ingrese\n 1 si desea agregar estudiantes \n 2 para finalizar: "))
#     if opc==1:
        
#         # auxdicc=pedirDato()
#         # aux=actualizar(auxdicc,colegio)
#         # colegio=aux
#         # print(colegio)
#         prom=0
#         for key in colegio.keys():
#             for key2 in (colegio[key]):
#                 if key2!="nombre":
#                     # prom+=int(colegio[key[key2]])
#                 # print(prom)

    #else:
     #   break