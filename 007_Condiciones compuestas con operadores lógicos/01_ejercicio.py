"""
Hasta ahora hemos visto los operadores:

relacionales (>, <, >=, <= , ==, !=)
matemáticos (+, -, *, /, //, **, %)
pero nos están faltando otros operadores imprescindibles:

lógicos (and y or)
Estos dos operadores se emplean fundamentalmente en las estructuras condicionales para agrupar varias condiciones simples.

Operador and

Traducido se lo lee como “Y”. Si la Condición 1 es verdadera Y la condición 2 es verdadera luego ejecutar la rama del verdadero.
Cuando vinculamos dos condiciones con el operador “and”, las dos condiciones deben ser verdaderas para que el resultado de la condición compuesta de Verdadero y continúe por la rama del verdadero de la estructura condicional.

La utilización de operadores lógicos permiten en muchos casos plantear algoritmos más cortos y comprensibles.
"""
"""
Confeccionar un programa que lea por teclado tres números enteros distintos y nos muestre el mayor.
"""

"""
Este ejercicio se puede resolver sin operadores lógicos pero el utilizarlos nos permite que sea mas simple la solución.
La primera estructura condicional es una ESTRUCTURA CONDICIONAL COMPUESTA con una CONDICION COMPUESTA.
Podemos leerla de la siguiente forma:
Si el contenido de la variable num1 es mayor al contenido de la variable num2 "Y" si el contenido de la variable num1 es mayor al contenido de la variable num3 entonces la CONDICION COMPUESTA resulta Verdadera.
Si una de las condiciones simples da falso la CONDICION COMPUESTA da Falso y continúa por la rama del falso.
Es decir que se mostrará el contenido de num1 si y sólo si num1 > num2 y num1 > num3.
En caso de ser Falsa la condición, analizamos el contenido de num2 y num3 para ver cual tiene un valor mayor.
En esta segunda estructura condicional no se requieren operadores lógicos al haber una condición simple.
"""
num1=int(input("Ingrese primer valor:"))
num2=int(input("Ingrese segundo valor:"))
num3=int(input("Ingrese tercer valor:"))
print("El mayor de los tres valores es")
if num1>num2 and num1>num3:
    print(num1)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)