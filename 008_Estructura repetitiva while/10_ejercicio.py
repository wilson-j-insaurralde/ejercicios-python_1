"""
Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.
"""

lista1=0
lista2=0
x=0
print("ingrese los valores de la primera lista")
while x<=15:
    valor=int(input("ingrese el valor: "))
    lista1=lista1+valor
    x=x+1

print("ingrese la segunda lista: ")
x=0
valor=0
while x<=15:
    valor=int(input("ingrese el valor: "))
    lista2=lista2+valor
    x=x+1

if lista1==lista2:
    print ("las listas son iguales")

else: 
    if lista1>lista2:  print ("la lista 1 es mayor")
    else:
        print("la lista 2 es mayor.")
    