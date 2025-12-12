"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Confeccionar un programa que contenga las siguientes funciones:
1) Carga de una lista de 5 nombres.
2) Ordenar alfabéticamente la lista.
3) Imprimir la lista de nombres
"""
def carga():
    lista=[]
    seguir="s"
    while seguir=="s":
        nom=input("ingrese el nombre: ")
        lista.append(nom)
        seguir=input("desea ingresar otro nombre?[s/n]")
    return lista

def ordenar(lista):
    aux=0
    pepe=len(lista)
    for x in range(pepe-1):
        for k in range (pepe-1):
            if lista[k]>lista[k+1]:
                aux=lista[k]
                lista[k]=lista[k+1]
                lista[k+1]=aux

lista=carga()
print(lista)
ordenar(lista)
print(lista)
            
