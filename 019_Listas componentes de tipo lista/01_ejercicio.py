"""
Hasta ahora hemos trabajado con listas cuyos componentes son de tipo:

enteros
flotantes
cadenas de caracteres
Ejemplo

notas=[8, 6, 8]
alturas=[1.73, 1.55, 1.92]
dias=["lunes", "martes", "miércoles"]
Pero lo que la hace tan flexible a esta estructura de datos es que podemos almacenar componentes de tipo LISTA.

notas=[[4,5], [6,9], [7,3]]
En la línea anterior hemos definido una lista de tres elementos de tipo lista, el primer elemento de la lista es otra lista de dos elementos de tipo entero. De forma similar los otros dos elementos de la lista notas son listas de dos elementos de tipo entero.
"""

"""
Crear una lista por asignación. La lista tiene que tener cuatro elementos. Cada elemento debe ser una lista de 3 enteros.
Imprimir sus elementos accediendo de diferentes modos.
"""

lista=[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

# imprimimos la lista completa
print(lista)
print("---------")
# imprimimos la primer componente
print(lista[0])
print("---------")
# imprimimos la primer componente de la lista contenida
# en la primer componente de la lista principal
print(lista[0][0])
print("---------")
# imprimimos con un for la lista contenida en la primer componente
for x in range(len(lista[0])):
    print(lista[0][x])
print("---------")               
# imprimimos cada elemento entero de cada lista contenida en la lista
for k in range(len(lista)):
    for x in range(len(lista[k])):
        print(lista[k][x])

"""
Al principio puede complicarse trabajar con listas de listas pero a medida que practiquemos esta estructura de datos veremos que podemos desarrollar algoritmos más complejos.

Para definir y crear por asignación una lista de listas tenemos:

lista=[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
Queda claro que el primer elemento de lista es:

[1,2,3]
El segundo elemento de la variable lista es (y así sucesivamente):

[4,5,6]
La función print si le pasamos como parámetro el nombre de la lista nos muestra la lista completa por pantalla:

print(lista)
Aparece:

[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
Cuando pasamos a la función print el primer elemento de la lista:

print(lista[0])
Nos muestra la lista contenida en la primer componente de la lista principal:

[1, 2, 3]
Si queremos acceder al primer entero almacenado en la lista contenida en la primer componente de la lista principal:

print(lista[0][0])
Nos muestra:

1
Para acceder mediante un for a todos los elementos de la lista contenida en la primer componente de la lista principal debemos codificar:

for x in range(len(lista[0])):
    print(lista[0][x])
Recordemos que la función len retorna la cantidad de elementos que contiene una lista. En este caso le pasamos como parámetro lista[0] que hace referencia a la primer componente de la lista principal.

El resultado de len(lista[0]) es un 3 que es la cantidad de elementos que tiene la lista contenida en la primer componente de la lista principal.

Cada ciclo del for accedemos a: lista[0][0] cuando x vale 0, lista[0][1] cuando x vale 1 y lista[0][2] cuando x vale 2.

Mediante este ciclo podemos acceder a cada elemento y procesarlo.

Por último con el ciclo anidado k podemos acceder a cada elemento de la lista principal y mediante el for interno acceder a cada elemento entero de las listas contenidas en la lista principal:

for k in range(len(lista)):
    for x in range(len(lista[k])):
        print(lista[k][x])
"""