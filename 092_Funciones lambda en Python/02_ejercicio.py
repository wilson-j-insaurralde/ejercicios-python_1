"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Confeccionar una función de orden superior que reciba una lista que almacena valores enteros y una función con un parámetro entero y que retorne un boolean.

La función debe analizar cada elemento de la lista llamando a la función que recibe como parámetro, si retorna un True se pasa a mostrar el elemento.

En el bloque principal definir una lista de enteros.

Imprimir de la lista:

Los valores múltiplos de 2
Los valores múltiplos de 3 o de 5
Los valores mayores o iguales a 50
Los valores comprendidos entre 1 y 50 o entre 70 y 100.
"""


def imprimir(lista,fn):
    for elemento in lista:
        if fn(elemento):
            print(elemento)

lista1=[9, 20, 70, 60, 19]
print("Valores pares de la lista")
imprimir(lista1, lambda x: x%2==0)
print("Valores múltiplos de 3 o de 5")
imprimir(lista1, lambda x: x%3==0 or x%5==0)
print("Imprimir valores mayores o iguales a 50")
imprimir(lista1, lambda x: x>=50)
print("Imprimir los valores comprendidos entre 1 y 50 o 70 y 100")
imprimir(lista1, lambda x: x>=1 and x<=50 or x>=70 and x<=100)
print("Imprimir la lista completa")
imprimir(lista1, lambda x: True )