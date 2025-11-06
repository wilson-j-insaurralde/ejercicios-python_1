"""Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la suma de los valores ingresados y su promedio."""

"""
En este problema, a semejanza de los anteriores, tenemos un CONTADOR llamado x que nos sirve para contar las vueltas que debe repetir el while.
También aparece el concepto de ACUMULADOR (un acumulador es un tipo especial de variable que se incrementa o disminuye con valores variables durante la ejecución del programa)

Hemos dado el nombre de suma a nuestro acumulador. Cada ciclo que se repita la estructura repetitiva, la variable suma se incrementa con el contenido ingresado en la variable valor.
"""
x=1
suma=0
while x<=10:
    valor=int(input("Ingrese un valor:"))
    suma=suma+valor
    x=x+1
promedio=suma/10
print("La suma de los 10 valores es")
print(suma)
print("El promedio es")
print(promedio)

"""
El resultado del promedio es un valor real es decir con coma. Si queremos que el resultado de la división solo retorne la parte entera del promedio debemos utilizar el operador //:

promedio=suma//10
El interprete de Python sabe que el promedio se calcula al finalizar el while ya que se encuentra codificado en la columna 1. Las tres instrucciones contenidas en el while están indentadas.
"""

