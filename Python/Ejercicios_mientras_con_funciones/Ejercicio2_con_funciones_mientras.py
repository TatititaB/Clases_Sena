#realice un algoritmo para determinar cuánto pagará finalmente una persona por un artículo equis,considerando que tiene un descuento de 20%, y debe pagar 10% de IVA debe mostrar el precio con descuento   y el precio final. El algoritmo debe ejecutarse indefinidamente mientras hasta que el usuario ingrese un numero diferente a cero.

def pedir_datos():
    print("Carrito de tienda, si quieres salir presiona 0")
    numero=int(input("Digite el valor del articulo: "))
    return numero
def descuento(numero):
    descuento=(numero*20)/100
    return descuento
def iva_producto(numero):
    iva=(numero*10)/100
    return iva
def total_valor(valor,descuento,iva):
    total_General=valor+iva-descuento
    print("El total del producto es: ",total_General)    
    return total_General
    
###################Codigo Principal###################
valor=1
while valor!=0:
    valor=pedir_datos()
    descto=descuento(valor)
    iva_prod=iva_producto(valor)
    total_vr=total_valor(valor,descto,iva_prod)
    
print("HAS SALIDO DEL CARRITO")