"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""

Confeccionar un programa con las siguientes funciones:
1) Cargar una lista con 5 palabras.
2) Intercambiar la primer palabra con la última.
3) Imprimir la lista
"""
def cargar():
    lista=[]
    for x in range(5):
        palabra=input("ingrese la palabra: ")
        lista.append(palabra)
    return lista
def intercambiar(lista):
    aux=lista[0]
    lista[0]=lista[-1]
    lista[-1]=aux
    print(lista)
lista=cargar()
intercambiar(lista)