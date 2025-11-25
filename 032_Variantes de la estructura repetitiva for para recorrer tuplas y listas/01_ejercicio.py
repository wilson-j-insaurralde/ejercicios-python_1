"""
Confeccionar un programa que permita la carga de una lista de 5 enteros por teclado.
Luego en otras funciones:
1) Imprimirla en forma completa.
2) Obtener y mostrar el mayor.
3) Mostrar la suma de todas sus componentes.
Utilizar la nueva sintaxis de for vista en este concepto.
"""
"""
lista=[2, 3, 50, 7, 9]

for elemento in lista:
    print(elemento)
    """

def carga():
    list=[]
    for x in range(5):
        lito=int(input("ingrese un valor entero: "))
        list.append(lito)
    return list

def imprimir(lista):
    print("lista completa: ")
    for elemento in lista:
        print(elemento)

def mayor(lista):
    mayor=lista[0]
    for elemento in lista:
        if elemento>mayor:
            mayor=elemento
    
    print(f"el mayor es: {mayor}")

def suma(lista):
    suma=0
    for elemento in lista:
        suma=suma+elemento
    
    print(f"la suma total de la lista es: {suma}")

lista=carga()
imprimir(lista)
mayor(lista)
suma(lista)