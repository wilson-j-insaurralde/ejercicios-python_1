"""
Confeccionar un programa que contenga las siguientes funciones:
1) Carga de una lista y retorno al bloque principal.
2) Fijar en cero todos los elementos de la lista que tengan un valor menor a 10.
3) Imprimir la lista
"""

def carga():
    lista=[]
    seguir="si"
    while seguir=="si":
        nu=int(input("ingrese el numero: "))
        lista.append(nu)

        seguir=input("desea ingresar otro numero?[si/no]")

    return lista
def menores(lista1):
    for x in range(len(lista1)):
        if lista1[x]<10:
            lista1[x]=0

def imprimirlista(lista1):
    for elemento in lista1:
        print(elemento,"-",sep="",end="")
    print("")

lista=carga()
imprimirlista(lista)
menores(lista)
imprimirlista(lista)