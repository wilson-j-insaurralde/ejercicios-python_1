"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. Una segunda función debe recibir una lista y mostrar todos los valores mayores a 10. Desde el bloque principal del programa llamar a ambas funciones.
"""
def carga ():
    lista=[]
    for x in range (5):
        li=int(input("ingrese el numero: "))
        lista.append(li)
        print(lista)
    return lista

def mayor(lista):
    mayor=[]
    for x in range(len(lista)):
        if lista[x]>10:
            mayor.append(lista[x])
    print(f"los meros mayores a 10: ",mayor)

lista=carga()
mayor(lista)