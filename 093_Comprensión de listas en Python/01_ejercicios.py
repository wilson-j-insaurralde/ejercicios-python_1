"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Definir una lista con 5 valores enteros, luego a partir de la primer lista generar una segunda lista con los valores elevados al cuadrado.
"""

lista1=[8,5,4,10,2]
lista2=[]

for elemento in lista1:
    lista2.append(elemento*elemento)

print("Lista 1")    
print(lista1)
print("Nueva lista")
print(lista2)

"""Mediante la construcción de comprensión de listas tenemos:"""

lista1=[8,5,4,10,2]
lista2=[elemento*elemento for elemento in lista1]

print("Lista 1")    
print(lista1)
print("Nueva lista")
print(lista2)



