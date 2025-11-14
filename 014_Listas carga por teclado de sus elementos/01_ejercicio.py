"""
Una lista en Python es una estructura mutable (es decir puede ir cambiando durante la ejecución del programa)

Hemos visto que podemos definir una lista por asignación indicando entre corchetes los valores a almacenar:

lista=[10, 20, 40]
Una lista luego de definida podemos agregarle nuevos elementos a la colección. La primera forma que veremos para que nuestra lista crezca es utilizar el método append que tiene la lista y pasar como parámetro el nuevo elemento:

lista=[10, 20, 30]
print(len(lista))    # imprime un 3
lista.append(100)
print(len(lista))    # imprime un 4
print(lista[0])      # imprime un 10
print(lista[3])      # imprime un 100
Definimos una lista con tres elementos:

lista=[10, 20, 30]
Imprimimos la cantidad de elementos que tiene la lista, en nuestro caso lo definimos con 3:

print(len(lista))    # imprime un 3
Agregamos una nuevo elemento al final de la lista llamando al método append:

lista.append(100)
Si llamamos nuevamente a la función len y le pasamos el nombre de nuestra lista ahora retorna un 4:

print(len(lista))    # imprime un 4
Imprimimos ahora el primer y cuarto elemento de la lista (recordar que se numeran a partir de cero):

print(lista[0])      # imprime un 10
print(lista[3])      # imprime un 100
"""

#Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado y añadirlos a la lista. Imprimir la lista generada

#definimos una lista vacia
lista=[]
#disponemos un ciclo de 5 vueltas
for x in range(5):
    valor=int(input("Ingrese un valor entero:"))
    lista.append(valor)

#imprimimos la lista    
print(lista)

"""
El algoritmo propuesto crea primero una lista vacía (debemos asignar los corchetes de apertura y cerrado sin contenido):

lista=[]
Luego mediante un for (podemos utilizar un while si queremos) solicitamos en forma sucesiva la carga de un entero por teclado y procedemos a agregarlo al final de la lista llamando al método append:

for x in range(5):
    valor=int(input("Ingrese un valor entero:"))
    lista.append(valor)
Finalmente mostramos los elementos de la lista creada:

print(lista)
"""
