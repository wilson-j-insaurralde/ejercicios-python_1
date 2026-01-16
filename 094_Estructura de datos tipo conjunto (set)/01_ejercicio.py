"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Creación de un conjunto por asignación
Para crear un conjunto por asignación debemos indicar sus elementos encerrados entre llaves y separados por coma.

conjunto1={1, 5, 10, 20}
print(conjunto1)
Los elementos de un conjunto pueden ser de distinto tipo:

conjunto2={"juan", 20, 6.4, True}
print(conjunto2)
Podemos definir elementos de un conjunto de tipo tupla pero no de tipo lista, diccionario o conjunto:

conjunto3={("juan", 33), ("ana", 44)}
print(conjunto3)
Agregar y eliminar elementos de un conjunto.
Mediante el método add agregamos un elemento a un conjunto, si el valor ya existe luego no se inserta:

lenguajes={"C", "Pascal", "PHP", "Python"}
print(lenguajes) # {"C", "Pascal", "PHP", "Python"}
lenguajes.add("Ruby")
print(lenguajes) # {"C", "Pascal", "PHP", "Python, "Ruby"}
lenguajes.add("PHP")
print(lenguajes) # {"C", "Pascal", "PHP", "Python, "Ruby"}
El conjunto "lenguajes" se crea con 4 elementos. Luego se agrega un quinto elemento:

lenguajes.add("Ruby")
Si intentamos agregar un elemento que ya existe el mismo no se agrega y no genera error:

lenguajes.add("PHP")
Para eliminar un elemento de un conjunto debemos llamar al método "remove":

lenguajes={"C", "Pascal", "PHP", "Python"}
print(lenguajes)
lenguajes.remove("Pascal")
print(lenguajes)
Si el método remove no encuentra el elemento dentro del conjunto genera una excepción de tipo "KeyError".

Si queremos eliminar un elemento del conjunto y que no genere error si no existe debemos hacer uso del método "discard":

lenguajes={"C", "Pascal", "PHP", "Python"}
print(lenguajes)
lenguajes.discard("Kotlin")
print(lenguajes)


Operador de pertenencia 'in'.
Si queremos verificar si un conjunto contiene un determinado valor podemos utilizar el operador 'in':

lenguajes={"C", "Pascal", "PHP", "Python"}
if "PHP" in lenguajes:
    print("El lenguaje PHP se encuentra en el conjunto")
else:    
    print("El lenguaje PHP no se encuentra en el conjunto") 
La estructura condicional if se verifica verdadero debido a que la cadena "PHP" se encuentra contenido en el conjunto "lenguajes".

Operaciones con conjuntos.
Las operaciones básicas con conjuntos son:

Unión
Intersección
Diferencia
Diferencia simétrica
"""

"""
Definir dos conjuntos que almacenen cada uno una serie de lenguajes de programación. Efectuar las cuatro operaciones básicas con dichos conjuntos.
"""

lenguajes1={"C", "Pascal", "PHP", "Python"}
lenguajes2={"C++", "Java", "Python"}
print("Lenguajes estructurados")
print(lenguajes1)
print("Lenguajes orientados a objetos")
print(lenguajes2)
conjunto1=lenguajes1 | lenguajes2
print("Todos los lenguajes (Unión)")
print(conjunto1)
conjunto2=lenguajes1 & lenguajes2
print("Intersección de los dos conjuntos de lenguajes (Intersección)")
print(conjunto2)
conjunto3=lenguajes1 - lenguajes2
print("Diferencia de los dos conjuntos de lenguajes (Diferencia)")
print(conjunto3)
conjunto4=lenguajes1 ^ lenguajes2
print("lenguajes del conjunto lenguajes1 o del conjunto lenguajes2 pero no en ambos (Diferencia simétrica)")
print(conjunto4)
"""
Los operadores de conjuntos son:

|   (unión)
&   (Intersección)
-   (Diferencia)
^   (Diferencia simétrica)

"""
"""En lugar de utilizar los operadores de conjuntos podemos llamar a sus métodos y obtener el mismo resultado:"""

lenguajes1={"C", "Pascal", "PHP", "Python"}
lenguajes2={"C++", "Java", "Python"}
print("Lenguajes estructurados")
print(lenguajes1)
print("Lenguajes orientados a objetos")
print(lenguajes2)
x=lenguajes1.union(lenguajes2)
print("Todos los lenguajes")
print(x)
x=lenguajes1.intersection(lenguajes2)
print("Intersección de los dos conjuntos de lenguajes")
print(x)
x=lenguajes1.difference(lenguajes2)
print("Diferencia de los dos conjuntos de lenguajes")
print(x)
x=lenguajes1.symmetric_difference(lenguajes2)
print("lenguajes del conjunto lenguajes1 o del conjunto lenguajes2 pero no en ambos")
print(x)

"""
Conjuntos disjuntos.
Dos conjuntos son disjuntos si no tienen elementos en común entre ellos. Su intersección es el conjunto vacío.

La clase set dispone del método 'isdisjoint' que retorna True si los conjuntos no tienen elementos en común:

dias_feriados={"sábado","domingo"}
dias_laborables={"lunes", "martes", "miércoles","jueves","viernes"};
if dias_laborables.isdisjoint(dias_feriados):
    print("dias_laborables no tiene elementos en común con dias_feriados")
Estos dos conjuntos no tiene elementos en común, luego el if se verifica verdadero.

Igualdad de conjuntos, subconjuntos y superconjuntos.
En Python podemos utilizar los operadores:

conjunto1==conjunto2
conjunto1!=conjunto2
conjunto1<conjunto2 (si el conjunto1 es un subconjunto de conjunto2)
conjunto1<=conjunto2 (si el conjunto1 es un subconjunto o es igual que conjunto2)
conjunto1>conjunto2 (si el conjunto1 es un superconjunto de conjunto2)
conjunto1>=conjunto2 (si el conjunto1 es un superconjunto o es igual que conjunto2)
Algunos ejemplos empleando estos operadores:

"""

dias_semana={"lunes", "martes", "miércoles","jueves","viernes","sábado","domingo"}
dias_feriados={"sábado","domingo"}
dias_laborables={"lunes", "martes", "miércoles","jueves","viernes"}
if dias_feriados<dias_semana:
    print("dias_feriados es un subconjunto de dias_semana")
if dias_feriados!=dias_laborables:
    print("dias_feriados es distinto a dias_laborables")    
if dias_semana>dias_laborables:
    print("dias_semana es un superconjunto de dias_laborables")    

"""
Acotaciones.
Para conocer la cantidad de elementos de un conjunto disponemos de la función 'len':

lenguajes={"C", "Pascal", "PHP", "Python"}
print(len(lenguajes)) # imprime un 4
Para crear un conjunto vacío debemos llamar a la función 'set':

lenguajes=set()
lenguajes.add("C")
lenguajes.add("Pascal")
lenguajes.add("PHP")
lenguajes.add("Python")
print(len(lenguajes)) # imprime un 4
Es importante recordar que en Python las llaves abiertas y cerradas crean un diccionario y no un conjunto:

productos={}
productos["manzanas"]=39
productos["peras"]=32
productos["lechuga"]=17
print(productos)
Un uso común de los conjuntos es eliminar los valores repetidos de listas y tuplas:

edades=[23, 21, 25, 21, 23]
print(edades)
conjunto=set(edades)
print(conjunto) # 25, 21, 23
Se crea un conjunto llamando a set y pasando como parámetro una lista, luego el conjunto no almacena los valores repetidos de la lista.

Podemos iterar un conjunto mediante la estructura repetitiva for:

dias={"lunes", "martes", "miércoles"}
for dia in dias:
    print(dia)
Conjuntos congelados 'frozenset'
Hay otra clase llamada 'frozenset' que permite crear conjuntos inmutables, es decir que no se le pueden agregar o eliminar elementos una vez creado.

"""