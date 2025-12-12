"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Se debe crear y cargar una lista donde almacenar 5 sueldos. Ordenar de menor a mayor la lista.

Ahora bien como vimos en el problema anterior con los 4 elementos que nos quedan podemos hacer el mismo proceso visto anteriormente, con lo cual quedará ordenado otro elemento de la lista. Este proceso lo repetiremos hasta que quede ordenado por completo la lista.

Como debemos repetir el mismo algoritmo podemos englobar todo el bloque en otra estructura repetitiva.

Realicemos una prueba del siguiente algoritmo:

Cuando k = 0
		x = 0		x = 1		x = 2		x = 3
		750		    750		    750	    	750
		1200		820		    820	    	820
		820		    1200		550	    	550
		550		    550		    1200		490
		490		    490		    490		    1200
		
Cuando k = 1
		x = 0		x = 1		x = 2		x = 3
		750		    750		    750	    	750	
		820		    550	    	550	    	550
		550	    	820		    490 		490
		490	    	490	    	820	    	820
		1200		1200		1200		1200

Cuando k = 2
		x = 0		x = 1		x  = 2		x = 3
		550	    	550	    	550	    	550
		750	    	490	    	490	    	490
		490	    	750	    	750	    	750
		820	    	820		    820	    	820
		1200		1200		1200		1200


Cuando k = 3
		x = 0		x = 1		x  = 2		x = 3
		490		    490		    490		    490
		550		    550		    550		    550
		750		    750		    750		    750
		820		    820		    820		    820
		1200		1200		1200		1200
"""
sueldos=[]
for x in range(5):
    valor=int(input("Ingrese sueldo:"))
    sueldos.append(valor)

print("Lista sin ordenar")
print(sueldos)

for k in range(4):
    for x in range(4):
        if sueldos[x]>sueldos[x+1]:
            aux=sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux

print("Lista ordenada")
print(sueldos)
"""
¿Porque repetimos 4 veces el for externo?
Como sabemos cada vez que se repite en forma completa el for interno queda ordenada una componente de la lista. A primera vista diríamos que deberíamos repetir el for externo la cantidad de componentes de la lista, en este ejemplo la lista sueldos tiene 5 componentes.

Si observamos, cuando quedan dos elementos por ordenar, al ordenar uno de ellos queda el otro automáticamente ordenado (podemos imaginar que si tenemos una lista con 2 elementos no se requiere el for externo, porque este debería repetirse una única vez)

ordenamiento de la lista completa

Una última consideración a este ALGORITMO de ordenamiento es que los elementos que se van ordenando continuamos comparándolos.

Ejemplo: En la primera ejecución del for interno el valor 1200 queda ubicado en la posición 4 de la lista. En la segunda ejecución comparamos si el 820 es mayor a 1200, lo cual seguramente será falso.
Podemos concluir que la primera vez debemos hacer para este ejemplo 4 comparaciones, en la segunda ejecución del for interno debemos hacer 3 comparaciones y en general debemos ir reduciendo en uno la cantidad de comparaciones.
Si bien el algoritmo planteado funciona, un algoritmo más eficiente, que se deriva del anterior es el plantear un for interno con la siguiente estructura:

for k in range(4):
    for x in range(4-k):
        if sueldos[x]>sueldos[x+1]:
            aux=sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux
Es decir restarle el valor del contador del for externo.
"""