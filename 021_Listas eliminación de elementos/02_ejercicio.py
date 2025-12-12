"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Crear una lista y almacenar 10 enteros pedidos por teclado. Eliminar todos los elementos que sean iguales al número entero 5.
"""
lista=[]

for x in range (10):
    li=int(input("ingrese el numero: "))
    lista.append(li)

print (lista)

posicion=0
while posicion<len(lista):
    if lista[posicion]==5:
        lista.pop(posicion)

    else: posicion=posicion+1

print(lista)

"""
Mediante un for cargamos 10 elementos en la lista:

lista=[]
for x in range(10):
    valor=int(input("Ingrese valor:"))
    lista.append(valor)
Como es posible que se eliminen 0, 1, 2 etc. elementos de la lista utilizamos un ciclo while (no podemos usar un for, ya que el contador del mismo no indicará correctamente el subindice a analizar)

Llevamos un contador llamado "posicion" que nos indica que elemento de la lista estamos verificando en el if, en el caso que se debe borrar llamamos al método pop pasando el contador y no incrementamos en uno el contador "posicion" ya que los elementos de la derecha se desplazan una posición a izquierda.
En el caso que no se debe borrar se incrementa en uno el contador "posicion" para analizar el siguiente elemento de la lista en la próxima vuelta del ciclo:

posicion=0
while posicion<len(lista):
    if lista[posicion]==5:
        lista.pop(posicion)
    else:
        posicion=posicion+1
"""
"""
Acotación: otra forma de eliminar elementos de una lista
Para eliminar elementos de una lista también es empleada la función "del" pasando como parámetro la referencia de la componente a eliminar:

lista=[10, 20, 30, 40, 50]

print(lista)

del(lista[0])
del(lista[1])
del(lista[2])

print(lista) # 20 40
"""