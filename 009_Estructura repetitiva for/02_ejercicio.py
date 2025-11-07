"""
Realizar un programa que imprima en pantalla los números del 0 al 100. Este problema lo podemos resolver perfectamente con el ciclo while pero en esta situación lo resolveremos empleando el for.
"""

for x in range (101):
    print(x)

"""
Tenemos primero la palabra clave for y seguidamente el nombre de la variable que almacenará en cada vuelta del for el valor entero que retorna la función range.
La función range retorna la primera vez el valor 0 y se almacena en x, luego el 1 y así sucesivamente hasta que retorna el valor que le pasamos a range menos uno (es decir en nuestro ejemplo al final retorna un 100)

Tengamos en cuenta que este mismo problema resuelto con la estructura while debería ser:

x=0
while x<101:
    print(x)
    x=x+1  
"""

