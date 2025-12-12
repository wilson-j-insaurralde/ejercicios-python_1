"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Se tiene la siguiente lista:
lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 50 del primer elemento de "lista".
Volver a imprimir la lista.
"""
lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]

print (lista)

for x in range(len(lista[0])):
    if lista[0][x]>50:
        lista[0][x]=0
    

print(lista)
    