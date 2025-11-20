"""
Crear una lista de 5 enteros y cargarlos por teclado. Borrar los elementos mayores o iguales a 10 y generar una nueva lista con dichos valores.
"""

lista1=[]
for x in range(5):
    num=int(input("ingrese el numero: "))
    lista1.append(num)

print(lista1)

lista2=[]
posicion=0
while posicion<len(lista1):
    if lista1[posicion]>=10:
        lista2.append(lista1[posicion])
        lista1.pop(posicion)
    else: 
        posicion=posicion+1

print(lista1)


print(lista2)