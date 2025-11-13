"""
Hasta ahora hemos trabajado con variables que permiten almacenar un único valor:

edad=12
altura=1.79
nombre="juan"
En Python existe un tipo de variable que permite almacenar una colección de datos y luego acceder por medio de un subíndice (similar a los string)

Creación de la lista por asignación
Para crear una lista por asignación debemos indicar sus elementos encerrados entre corchetes y separados por coma.

lista1=[10, 5, 3]                       # lista de enteros
lista2=[1.78, 2.66, 1.55, 89,4]         # lista de valores float
lista3=["lunes", "martes", "miercoles"] # lista de string
lista4=["juan", 45, 1.92]               # lista con elementos de distinto tipo
Si queremos conocer la cantidad de elementos de una lista podemos llamar a la función len:

lista1=[10, 5, 3]   # lista de enteros
print(len(lista1))  # imprime un 3
"""

#Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.

lista1=[10,7,3,7,2]
suma=0
x=0
while x< len(lista1):
    suma= suma + lista1[x]
    x=x+1
print(f"la suma total es: {suma}")    

"""
Primero definimos una lista por asignación con 5 elementos:

lista=[10,7,3,7,2]
Definimos un acumulador para sumar los elementos de la lista y un contador para indicar que posición de la lista accedemos:

suma=0
x=0
Mediante un ciclo while recorremos y sumamos cada elementos de la lista:

while x<len(lista):
    suma=suma+lista[x]
    x=x+1
Cuando llamamos a la función print pasando como dato una lista luego se muestra en pantalla todos los elementos de la lista entre corchetes y separados por coma tal cual como la definimos:

print("Los elementos de la lista son")
print(lista)
Finalmente mostramos el acumulador:

print("La suma de todos sus elementos es")    
print(suma)    
"""