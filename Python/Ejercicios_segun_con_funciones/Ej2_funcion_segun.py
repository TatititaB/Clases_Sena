"""Desarrollar un algoritmo que, dado un Mes del año en Carácter, nos diga cuántos días tiene, y cuántos festivos, teniendo en cuenta el año 2023."""
def pedir_datos():
    meses=input("Digite el mes del que quiere tener informacion al respecto:")
    
    return meses
def funcionalidad_programa(dato_mes):
    if dato_mes=="enero":
        inf="enero consta de 31 dias y tiene 2 festivos"
    elif dato_mes=="febrero":
        inf="Febrero consta de 28 dias y no tine festivos"
    elif dato_mes=="marzo":
        inf="marzo tiene 31 dias y tiene 1 festivos"
    elif dato_mes=="abril":
        inf="abril tiene 30 dias y tiene 4 festivos"
    elif dato_mes=="mayo":
        inf="mayo tiene 31 dias y tiene 2 festivos"
    elif dato_mes=="junio":
        inf="junio tiene 30 dias y tiene 2 festivos"
    elif dato_mes=="julio":
        inf="julio tiene 31 dias y tiene 2 festivos"
    elif dato_mes=="agosto":
        inf="agosto tiene 31 dias y tiene 2 festivos"
    elif dato_mes=="septiembre":
        inf="septiembre tiene 30 dias y no hay festivos"
    elif dato_mes=="octubre":
        inf="octubre tiene 31 dias y tiene 1 festivos"
    elif dato_mes=="noviembre":
        inf="noviembre tiene 30 dias y tiene 2 festivos"
    elif dato_mes=="diciembre":
        inf="diciembre tiene 31 dias y tiene 2 festivos"
    else:
        inf="dato incorrecto"

    return inf
def imprimir_resultado(resultado):
    print(resultado)
######################codigoPrincipal#################################    
meses_del_2023= pedir_datos()
funcione_aqui=funcionalidad_programa(meses_del_2023)
imprimir_resultado(funcione_aqui)