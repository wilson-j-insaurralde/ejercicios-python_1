"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Solicitar por teclado dos enteros. El primer valor indica la cantidad de elementos que crearemos en la lista. El segundo valor indica la cantidad de elementos que tendrá cada una de las listas internas a la lista principal.
Mostrar la lista y la suma de todos sus elementos.

Por ejemplo si el operador carga un 2 y un 4 significa que debemos crear una lista similar a:

lista=[[1,1,1,1], [1,1,1,1]]

"""

lista=[]
elementos=int(input("Cuantos elementos tendra la lista:"))
sub=int(input("Cuantos elementos tendran las listas internas:"))
for k in range(elementos):
    lista.append([])
    for x in range(sub):
        valor=int(input("Ingrese valor:"))
        lista[k].append(valor)

print(lista)

suma=0
for k in range(len(lista)):
    for x in range(len(lista[k])):
        suma=suma+lista[k][x]

print("La suma de todos sus elementos:",suma) 


"""
Lo primero que hacemos en este problema además de definir la lista es cargar dos enteros por teclado:

lista=[]
elementos=int(input("Cuantos elementos tendra la lista:"))
sub=int(input("Cuantos elementos tendran las listas internas:"))
El primer for se repetirá tantas veces como indica el primer valor ingresado por teclado almacenado en la variable "elementos", cada vuelta de este for se crea un elemento en la "lista" y se carga una lista vacía []:

for k in range(elementos):
    lista.append([])
En el for interior procedemos a cargar tantos valores como lo indicamos en la variable "sub" y los vamos añadiendo en la lista vacía que creamos antes de este for:

    for x in range(sub):
        valor=int(input("Ingrese valor:"))
        lista[k].append(valor)
Finalmente para sumar todos los elementos enteros almacenados en "lista" debemos disponer estructuras repetitivas anidadas:

suma=0
for k in range(len(lista)):
    for x in range(len(lista[k])):
        suma=suma+lista[k][x]
El for de las "k" se repite tantas veces como elementos tenga "lista" y el for de las x se repite tantas veces como elementos tenga la lista en la posición k.
"""