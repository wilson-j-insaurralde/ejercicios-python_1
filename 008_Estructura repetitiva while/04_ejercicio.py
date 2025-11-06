"""
Una planta que fabrica perfiles de hierro posee un lote de n piezas.
Confeccionar un programa que pida ingresar por teclado la cantidad de piezas a procesar y luego ingrese la longitud de cada perfil; sabiendo que la pieza cuya longitud esté comprendida en el rango de 1.20 y 1.30 son aptas. Imprimir por pantalla la cantidad de piezas aptas que hay en el lote.

"""

"""
En este problema hay que cargar inicialmente la cantidad de piezas a ingresar ( n ), seguidamente se cargan n valores de largos de piezas.
Cada vez que ingresamos un largo de pieza (largo) verificamos si es una medida correcta (debe estar entre 1.20 y 1.30 el largo para que sea correcta), en caso de ser correcta la CONTAMOS (incrementamos la variable cantidad en 1)

Al contador cantidad lo inicializamos en cero porque inicialmente no se ha cargado ningún largo de pieza.
Cuando salimos de la estructura repetitiva porque se han cargado n largos de piezas mostramos por pantalla el contador cantidad (que representa la cantidad de piezas aptas)

En este problema tenemos dos CONTADORES:

x 		(Cuenta la cantidad de piezas cargadas hasta el momento)
cantidad	(Cuenta los perfiles de hierro aptos)
"""
cantidad=0
x=1
n=int(input("Cuantas piezas cargara:"))
while x<=n:
    largo=float(input("Ingrese la medida de la pieza:"))
    if largo>=1.2 and largo<=1.3:
        cantidad=cantidad+1
    x=x+1
print("La cantidad de piezas aptas son")
print(cantidad)

"""
Veamos algunas cosas nuevas:

Cuando queremos cargar por teclado un valor con decimales debemos utilizar la función float en lugar de int:

    largo=float(input("Ingrese la medida de la pieza:"))
"""