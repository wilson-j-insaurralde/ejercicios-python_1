"""
Es una actividad muy común la búsqueda del mayor y menor elemento de una lista.
Es necesario que la lista tenga valores del mismo tipo por ejemplo enteros. Pueden ser de tipo cadenas de caracteres y se busque cual es mayor o menor alfabéticamente, pero no podemos buscar el mayor o menor si la lista tiene enteros y cadenas de caracteres al mismo tiempo.
"""

#Crear y cargar una lista con 5 enteros. Implementar un algoritmo que identifique el mayor valor de la lista.

lista=[]
for x in range(5):
    valor=int(input("Ingrese valor:"))
    lista.append(valor)

mayor=lista[0]
for x in range(1,5):
    if lista[x]>mayor:
        mayor=lista[x]

print("Lista completa")
print(lista)
print("Mayor de la lista")
print(mayor)



"""
Primero procedemos a cargar por teclado los 5 valores en la lista:

for x in range(5):
    valor=int(input("Ingrese valor:"))
    lista.append(valor)
Para identificar el mayor de una lista primero tomamos como referencia el primer elemento, considerando a este en principio como el mayor de la lista:

mayor=lista[0]
Seguidamente disponemos un for que se repita 4 veces esto debido a que no debemos controlar el primer elemento de la lista (recordar que la primer vuelta del for x toma el valor 1, luego el 2 y así sucesivamente hasta el 4):

for x in range(1,5):
Dentro del for mediante una estructura condicional verificamos si el elemento de la posición x de la lista es mayor al que hemos considerado hasta este momento como mayor:

    if lista[x]>mayor:
        mayor=lista[x]
Como vemos en las dos líneas anteriores si el if se verifica verdadero actualizamos la variable mayor con el elemento de la lista que estamos analizando.

Cuando finaliza el for procedemos a mostrar el contenido de la variable "mayor" que tiene almacenado el mayor elemento de la lista:

print("Mayor de la lista")
print(mayor)
"""