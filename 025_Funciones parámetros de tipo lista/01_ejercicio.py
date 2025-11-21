"""
Definir por asignación una lista de enteros en el bloque principal del programa. Elaborar tres funciones, la primera recibe la lista y retorna la suma de todos sus elementos, la segunda recibe la lista y retorna el mayor valor y la última recibe la lista y retorna el menor.
listavalores=[10, 56, 23, 120, 94]
"""

def suma(lista):
    total=0
    for x in range(len(lista)):
        total=total+lista[x]
    return total
def mayor(lista):
    may=lista[0]
    for x in range(1,len(lista)):
        if may < lista[x]:
            may=lista[x]
    return may
def menor(lista):
    men=lista[0]
    for x in range (1,len(lista)):
        if men>lista[x]:
            men=lista[x]
    return men



listavalores=[10, 56, 23, 120, 94]
print("la lista es: ", listavalores)
sumatotal=suma(listavalores)
mayor= mayor(listavalores)
menor= menor(listavalores)
print(f"la suma total de la lista es: {sumatotal}")
print(F"el mayor valor es: {mayor}")
print(f"el menor valor es: {menor}")