"""
Estructura condicional compuesta.
Cuando se presenta la elección tenemos la opción de realizar una actividad u otra. Es decir tenemos actividades por el verdadero y por el falso de la condición. Lo más importante que hay que tener en cuenta que se realizan las actividades de la rama del verdadero o las del falso, NUNCA se realizan las actividades de las dos ramas.
En una estructura condicional compuesta tenemos actividades tanto por la rama del verdadero como por la rama del falso.
"""

#Problema:
#Realizar un programa que solicite ingresar dos números distintos y muestre por pantalla el mayor de ellos.
"""
Se hace la entrada de num1 y num2 por teclado. Para saber cual variable tiene un valor mayor preguntamos si el contenido de num1 es mayor (>) que el contenido de num2, si la respuesta es verdadera vamos por la rama de la derecha e imprimimos num1, en caso que la condición sea falsa vamos por la rama de la izquierda (Falsa) e imprimimos num2.
Como podemos observar nunca se imprimen num1 y num2 simultáneamente.

Estamos en presencia de una ESTRUCTURA CONDICIONAL COMPUESTA ya que tenemos actividades por la rama del verdadero y del falso.
"""
num1=int(input("Ingrese primer valor:"))
num2=int(input("ingrese segundo valor:"))
print("El valor mayor es")
if num1>num2:
    print(num1)
else:
    print(num2)
"""
Cotejemos el diagrama de flujo y la codificación y observemos que el primer bloque después del if representa la rama del verdadero y el segundo bloque después de la palabra clave else representa la rama del falso.

Ejecutamos el programa, si hubo errores sintácticos corrijamos y carguemos dos valores, como por ejemplo:

Ingrese el primer valor: 10
Ingrese el segundo valor: 4
El valor mayor es
10
Si ingresamos los valores 10 y 4 la condición del if retorna verdadero y ejecuta el primer bloque.
Un programa se controla y corrige probando todos sus posibles resultados.
Ejecutemos nuevamente el programa e ingresemos:

Ingrese el primer valor: 10
Ingrese el segundo valor: 54
El valor mayor es
54
Cuando a un programa le corregimos todos los errores sintácticos y lógicos ha terminado nuestra tarea y podemos entregar el mismo al USUARIO que nos lo solicitó.
"""
"""
Operadores
En una condición deben disponerse únicamente variables, valores constantes y operadores relacionales.

Operadores Relacionales:
== Igualdad

!= Desigualdad

< menor

<= menor o igual

> mayor

>= mayor o igual
Operadores Matemáticos
+ suma
- resta
* multiplicación
/ división de flotantes
// división de enteros
% resto de una división
** exponenciación
Hay que tener en cuenta que al disponer una condición debemos seleccionar que operador relacional se adapta a la pregunta.

Ejemplos:

	Se ingresa un número multiplicarlo por 10 si es distinto a 0.   (!=)
	Se ingresan dos números mostrar una advertencia si son iguales.  (==)
Los problemas que se pueden presentar son infinitos y la correcta elección del operador solo se alcanza con la práctica intensiva en la resolución de problemas.
"""

