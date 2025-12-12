"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Almacenar en una lista de 5 elementos tuplas que guarden el nombre de un pais y la cantidad de habitantes.
Definir tres funciones, en la primera cargar la lista, en la segunda imprimirla y en la tercera mostrar el nombre del país con mayor cantidad de habitantes.
"""

def carga():
    paises=[]
    for x in range (5):
        pais=input("ingrese el nombre del pais: ")
        poblacion=int(input("ingrese la cantidad de habitantes: "))
        paises.append((pais,poblacion))
    return paises


def imprimir(paises):
    for x in range (5):
        print(paises[x][0],paises[x][1],sep="--- ")


def mayor_hab(paises):
    mayor=paises[0][1]
    pos=0
    for x in range(1,len(paises)):
        if mayor<paises[x][1]:
            mayor=paises[x][1]
            pos=x
    print("el paises con mayor cantidad de habitantes es: ") 
    print(paises[pos][0],paises[pos][1],sep=" --- ")

pai=carga()
imprimir(pai)
mayor_hab(pai)