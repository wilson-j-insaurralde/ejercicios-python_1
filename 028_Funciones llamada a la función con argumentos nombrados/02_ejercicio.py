"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Cargar una lista de 10 enteros, luego mostrarlos por pantalla a cada elemento separados por una coma.
"""
def cargar():
    lista=[]
    for x in range (10):
        li=int(input("ingresar el numero: "))
        lista.append(li)
    return [lista]

def imprimir(lista):
    for x in range (len(lista)):
        if x==(len(lista)-1):
            print(lista[x])
        else:
            print(lista[x],end=",")

lista=cargar()
imprimir(lista)