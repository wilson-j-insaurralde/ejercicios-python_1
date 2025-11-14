"""
Realizar la carga de valores enteros por teclado, almacenarlos en una lista. Finalizar la carga de enteros al ingresar el cero. Mostrar finalmente el tamaño de la lista.
"""

lista=[]
valor=1
while valor!=0:
    valor=int(input("ingrese el numero entero(ingrese 0 parafinalizar la carga de datos): "))
    
    if valor!=0:
        lista.append(valor)

print(lista)
print("tamaño de la lista: ")    
print(len(lista))