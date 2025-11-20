"""
En el concepto anterior vimos que fácilmente podemos definir por asignación una lista cuyas componentes sean también listas:

lista=[[1,2,3], [7,4], [9,2]]
En muchas situaciones debemos crear una nueva lista ingresando los datos por teclado o por operaciones del mismo programa.
"""
"""
Crear y cargar una lista con los nombres de tres alumnos. Cada alumno tiene dos notas, almacenar las notas en una lista paralela. Cada componente de la lista paralela debe ser también una lista con las dos notas. Imprimir luego cada nombre y sus dos notas.

Si cargáramos los datos por asignación sería algo parecido a esto:

alumnos=["juan", "ana", "luis"]
notas=[[10,8], [6,5], [2,8]]
En la componente 0 de la lista alumnos tenemos almacenado el nombre "juan" y como son listas paralelas en la componente 0 de la lista notas tenemos almacenado una lista con las dos notas 10 y 8.

Nuestro objetivo como lo pide el problema es cargar los datos por teclado.
"""
nombres=[]
notas=[]
for x in range(3):
    nom=input("Ingrese el nombre del alumno:")
    nombres.append(nom)
    no1=int(input("Ingrese la primer nota:"))
    no2=int(input("Ingrese la segunda nota:"))
    notas.append([no1,no2])

for x in range(3):
    print(nombres[x],notas[x][0],notas[x][1])

"""
La creación de las dos listas no difiere una de otra:

nombres=[]
notas=[]
En la estructura repetitiva for procedemos a cargar un nombre y agregarlo a la lista en forma similar como lo hemos hecho en conceptos anteriores:

for x in range(3):
    nom=input("Ingrese el nombre del alumno:")
    nombres.append(nom)
Lo nuevo se presenta cuando queremos añadir elementos a la lista notas, lo hacemos con el mismo método append pero le pasamos como parámetro una lista con dos elementos:

    no1=int(input("Ingrese la primer nota:"))
    no2=int(input("Ingrese la segunda nota:"))
    notas.append([no1,no2])
Cuando imprimimos el nombre lo accedemos por un solo subíndice, pero para acceder a cada una de las notas debemos indicar dos subíndices, el primer subíndice es con respecto a que elemento accedemos de la lista principal y el segundo subíndice hace referencia a la lista contenida en dicha componente:

for x in range(3):
    print(nombres[x],notas[x][0],notas[x][1])
"""