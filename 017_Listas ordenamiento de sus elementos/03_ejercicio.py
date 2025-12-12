"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""Crear una lista y almacenar los nombres de 5 países. Ordenar alfabéticamente la lista e imprimirla."""

paises=[]
for x in range (5):
    pa=input("ingrese el nombre del pais: ")
    paises.append(pa)

aux=0
for k in range (1,4):
    for x in range(1,4):
        if paises[x]>paises[x+1]:
            aux=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux

print("Listado de paises")
print(paises)
