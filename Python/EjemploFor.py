total=0
print("Digite el rango de numeros que desea sumar")
DatoRango=int(input())
print("********")
for i in range (DatoRango):
    total+=i
    print(f"{i}")
print("la sumatoria total es: "+f"{total}")