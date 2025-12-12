"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Crear y cargar por teclado en el bloque principal del programa una lista de 5 enteros. Implementar una función que imprima el mayor y el menor valor de la lista.
"""
def mayor(lista):
    mayor=lista[0]
    for x in range (1,len(lista)):
        if mayor<lista[x]:
            mayor= lista[x]
    return mayor
def menor(lista):
    menor=lista[0]
    for x in range (1,len(lista)):
    
        if menor>lista[x]:
            menor=lista[x]
    
    return menor

lista=[]
for x in range(5):
    x=int(input("ingrese el numero de la lista: "))
    lista.append(x)
print("la lista es: ",lista)
menor=menor(lista)
mayor=mayor(lista)

print(f"el mayor valor es: {mayor}")
print(f"el menor valor es: {menor}")
             