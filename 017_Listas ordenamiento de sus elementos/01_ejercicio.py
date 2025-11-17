"""
Otro algoritmo muy común que debe conocer y entender un programador es el ordenamiento de una lista de datos.


El ordenamiento de una lista se logra intercambiando las componentes de manera que:
lista[0] <= lista[1] <= lista[2] etc.

El contenido de la componente lista[0] sea menor o igual al contenido de la componente lista[1] y así sucesivamente.
Si se cumple lo dicho anteriormente decimos que la lista está ordenado de menor a mayor. Igualmente podemos ordenar una lista de mayor a menor.

Tengamos en cuenta que la estructura de datos lista en Python es mutable, eso significa que podemos modificar sus elementos por otros.

Se puede ordenar tanto listas con componentes de tipo int, float como cadena de caracteres. En este último caso el ordenamiento es alfabético.

Problema 1:
Se debe crear y cargar una lista donde almacenar 5 sueldos. Desplazar el valor mayor de la lista a la última posición.

La primera aproximación para llegar en el próximo problema al ordenamiento completo de una lista tiene por objetivo analizar los intercambios de elementos dentro de la lista y dejar el mayor en la última posición.

El algoritmo consiste en comparar si la primera componente es mayor a la segunda, en caso que la condición sea verdadera, intercambiamos los contenidos de las componentes.

Vamos a suponer que se ingresan los siguientes valores por teclado:

1200
750
820
550
490
En este ejemplo: ¿es 1200 mayor a 750? La respuesta es verdadera, por lo tanto intercambiamos el contenido de la componente 0 con el de la componente 1.
Luego comparamos el contenido de la componente 1 con el de la componente 2: ¿Es 1200 mayor a 820?
La respuesta es verdadera entonces intercambiamos.
Si hay 5 componentes hay que hacer 4 comparaciones, por eso el for se repite 4 veces.
Generalizando: si la lista tiene N componentes hay que hacer N-1 comparaciones.

Cuando		x = 0		x = 1		x  = 2		x = 3
		
		    750		    750		    750		    750
		    1200		820		    820		    820
		    820		    1200		550		    550
		    550		    550		    1200		490
		    490		    490		    490		    1200
"""

"""
Podemos ver cómo el valor más grande de la lista desciende a la última componente. Empleamos una variable auxiliar (aux) para el proceso de intercambio:


"""
sueldos=[]
for x in range(5):
    valor=int(input("Ingrese sueldo:"))
    sueldos.append(valor)

print("Lista sin ordenar")
print(sueldos)

for x in range(4):
    if sueldos[x]>sueldos[x+1]:
        aux=sueldos[x]
        sueldos[x]=sueldos[x+1]
        sueldos[x+1]=aux

print("Lista con el último elemento ordenado")
print(sueldos)

"""
Al salir del for el contenido de la lista es la siguiente:

750
820
550
490
1200
Analizando el algoritmo podemos comprobar que el elemento mayor de la lista se ubica ahora en el último lugar.
Podemos volver a ejecutar el programa y veremos que siempre el elemento mayor queda al final.

Pero con un único for no se ordena una lista. Solamente está ordenado el último elemento de la lista.
"""