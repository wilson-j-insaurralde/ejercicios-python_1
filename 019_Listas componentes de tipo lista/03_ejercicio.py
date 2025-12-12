"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Crear una lista por asignación. La lista tiene que tener 5 elementos. Cada elemento debe ser una lista, la primera lista tiene que tener un elemento, la segunda dos elementos, la tercera tres elementos y así sucesivamente.
Sumar todos los valores de las listas.
"""
lista=[[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5]]

suma=0
for k in range(len(lista)):
    for x in range(len(lista[k])):
        suma=suma+lista[k][x]
print(suma)

"""
Lo primero que es importante notar que las listas contenidas en las lista principal no tienen porque ser del mismo tamaño.

La forma más sencilla es utilizar dos ciclos repetitivos. El primero se repite tantas veces como elementos tenga la lista principal:

for k in range(len(lista)):
El segundo ciclo nos sirve para recorrer y acceder a cada elemento entero de cada lista:

    for x in range(len(lista[k])):
        suma=suma+lista[k][x]
La cantidad de veces que se repite el for interno depende de la cantidad de elementos que tiene la lista que estamos sumando en ese momento.
"""
