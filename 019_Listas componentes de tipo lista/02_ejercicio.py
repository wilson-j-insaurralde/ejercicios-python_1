"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Crear una lista por asignación. La lista tiene que tener 2 elementos. Cada elemento debe ser una lista de 5 enteros.
Calcular y mostrar la suma de cada lista contenida en la lista principal.
"""
lista=[[1,1,1,1,1], [2,2,2,2,2]]

suma1=lista[0][0]+lista[0][1]+lista[0][2]+lista[0][3]+lista[0][4]
print(suma1)
suma2=lista[1][0]+lista[1][1]+lista[1][2]+lista[1][3]+lista[1][4]
print(suma2)
print("----------")

suma1=0
for x in range(len(lista[0])):
    suma1=suma1+lista[0][x]
suma2=0
for x in range(len(lista[1])):
    suma2=suma2+lista[1][x]
print(suma1)
print(suma2)
print("----------")

for k in range(len(lista)):
    suma=0
    for x in range(len(lista[k])):
        suma=suma+lista[k][x]
    print(suma)

    """
    Hemos resuelto el problema de tres formas.

La primer forma es acceder a cada elemento en forma secuencial, esto se resuelve de esta forma si tenemos que acceder a un pequeño número de elementos, es decir si la lista es pequeña:

suma1=lista[0][0]+lista[0][1]+lista[0][2]+lista[0][3]+lista[0][4]
print(suma1)
suma2=lista[1][0]+lista[1][1]+lista[1][2]+lista[1][3]+lista[1][4]
print(suma2)
La segunda forma es utilizar una estructura repetitiva para sumar todos los elementos de una lista (el primer subíndice siempre es 0 y el segundo varía con la variable x):

suma1=0
for x in range(len(lista[0])):
    suma1=suma1+lista[0][x]
suma2=0
for x in range(len(lista[1])):
    suma2=suma2+lista[1][x]
print(suma1)
print(suma2)
La última forma planteada es utilizar una estructura repetitiva anidada que suma cada fila, el for externo (k) se repite 2 veces que es el tamaño de la variable "lista":

for k in range(len(lista)):
    suma=0
    for x in range(len(lista[k])):
        suma=suma+lista[k][x]
    print(suma)
Es importante notar que el acumulador suma lo iniciamos en 0 cada vez que comenzamos a sumar una nueva lista.
    """