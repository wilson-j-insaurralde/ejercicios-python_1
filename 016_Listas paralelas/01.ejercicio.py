"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Podemos decir que dos listas son paralelas cuando hay una relación entre las componentes de igual subíndice (misma posición) de una lista y otra.

listas paralelas
Si tenemos dos listas que ya hemos inicializado con 5 elementos cada una. En una se almacenan los nombres de personas en la otra las edades de dichas personas.
Decimos que la lista nombres es paralela a la lista edades si en la componente 0 de cada lista se almacena información relacionada a una persona (Juan - 12 años)
Es decir hay una relación entre cada componente de las dos listas.

Esta relación la conoce únicamente el programador y se hace para facilitar el desarrollo de algoritmos que procesen los datos almacenados en las estructuras de datos.
"""
"""
Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años)
"""
nombres=[]
edades=[]
for x in range(5):
    nom=input("Ingrese el nombre de la persona:")
    nombres.append(nom)
    ed=int(input("Ingrese la edad de dicha persona:"))
    edades.append(ed)

print("Nombre de las personas mayores de edad:")
for x in range(5):
    if edades[x]>=18:
        print(nombres[x])

"""
Definimos dos listas para almacenar los nombres y las edades de las personas respectivamente:

nombres=[]
edades=[]
Mediante un for cargamos en forma simultanea un elemento de cada lista, es decir un nombre de persona y la edad de dicha persona:

for x in range(5):
    nom=input("Ingrese el nombre de la persona:")
    nombres.append(nom)
    ed=int(input("Ingrese la edad de dicha persona:"))
    edades.append(ed)
Para imprimir los nombres de la personas mayores de edad procedemos a analizar dentro de un for y mediante un if cada una de las edades almacenadas en la lista "edades", en el caso que su valor sea mayor o igual a 18 mostramos el elemento de la lista nombres de la misma posición:

for x in range(5):
    if edades[x]>=18:
        print(nombres[x])
"""