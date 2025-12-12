"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Desarrollar un programa que cargue una lista con 10 enteros.
Cargar los valores aleatorios con números enteros comprendidos entre 0 y 1000.
Mostrar la lista por pantalla.
Luego mezclar los elementos de la lista y volver a mostrarlo.
"""
import random

def carga():
    lista=[]
    for x in range (10):
        lista.append(random.randint(0,1000))
    return lista

def mesclar(lista):
    random.shuffle(lista)


lista=carga()
print(lista)
mesclar(lista)
print(lista)