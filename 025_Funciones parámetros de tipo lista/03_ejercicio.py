"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Crear una lista de enteros por asignación. Definir una función que reciba una lista de enteros y un segundo parámetro de tipo entero. Dentro de la función mostrar cada elemento de la lista multiplicado por el valor entero enviado.
lista=[3, 7, 8, 10, 2]
multiplicar(lista,3)
"""

def multiplicar(lista,n):
    multiplicada=[]
    for x in range(len(lista)):
        p=n*lista[x]
        multiplicada.append(p)
    print (multiplicada)
lista=[3, 7, 8, 10, 2]
n=int(input("ingrese el numero por el que desea multiplicar: "))
print("la lista es: ",lista)

print(f"la lista multiplicada por el numero {n} queda: ")
multiplicar(lista,n)