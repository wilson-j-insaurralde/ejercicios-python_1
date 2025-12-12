"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Realizar un programa que contenga las siguientes funciones:
1) Carga de una lista de 10 enteros.
2) Recibir una lista y retornar otra con la primer mitad (se sabe que siempre llega una lista con una cantidad par de elementos)
3) Imprimir una lista.
"""
def carga ():
    enteroslista=[]
    for x in range (10):
        n=int(input("ingrese el numero entero: "))
        enteroslista.append(n)
    return enteroslista
def dividirlistapar(lista):
    lista1=[]
    lista2=[]
    longitud=(len(lista)//2)
    lista1=lista[:longitud]
    lista2=lista[longitud:]
    return lista1,lista2

lista=carga()
lista1,lista2=dividirlistapar(lista)
print(lista)
print(lista1)
print(lista2)