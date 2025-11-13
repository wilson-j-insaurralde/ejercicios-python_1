"""
Definir una lista por asignación que almacene en la primer componente el nombre de un alumno y en las dos siguientes sus notas. Imprimir luego el nombre y el promedio de las dos notas.
"""
lista=["ana", 7, 9]
print("Nombre del alumno:")
print(lista[0])
promedio=(lista[1]+lista[2])//2
print("Promedio de sus dos notas:")
print(promedio)

"""
Como vemos en este problema los elementos de una lista pueden ser de distinto tipo, aquí tenemos el primer elemento de tipo string y los dos siguientes de tipo int.

Recordemos que el operador // se utiliza para dividir dos valores y retornar solo la parte entera.
"""