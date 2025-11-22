"""
Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. Una segunda función debe recibir una lista y retornar el mayor y el menor valor de la lista. Desde el bloque principal del programa llamar a ambas funciones e imprimir el mayor y el menor de la lista
"""
def mayor (lista):
    mayor=lista[0]
    for x in range (1,len(lista)):
        if mayor<lista[x]:
            mayor=lista[x]
    return mayor

def menor (lista):
    menor=lista[0]
    for x in range (1,len(lista)):
        if menor>lista[x]:
            menor=lista[x]

    return menor

def carga ():
    lista=[]
    for x in range (5):
        li=int(input("ingrese un numero: "))
        lista.append(li)
    return lista

lista=carga()
print("el mayor valor es: ",mayor(lista) )
print("el menor valor es: ",menor(lista))
