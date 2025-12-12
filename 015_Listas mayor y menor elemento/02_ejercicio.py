"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Crear y cargar una lista con 5 enteros por teclado. Implementar un algoritmo que identifique el menor valor de la lista y la posición donde se encuentra.
"""
lista=[]
posicion=0


for x in range (5):
    entero=int(input("ingrese el numero entero: "))
    lista.append(entero)
    
menor=lista[0]

for x in range (1,5):
    if lista[x]<menor:
        menor=lista[x]
        posicion=x
print(f"la lista es: {lista}")
print(f"el menor valor es: {menor} y su posicion es: {posicion}")


