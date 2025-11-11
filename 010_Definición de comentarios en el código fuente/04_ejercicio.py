"""
Confeccionar un programa que solicite la carga de 10 valores reales por teclado. Mostrar al final su suma. Definir varias líneas de comentarios indicando el nombre del programa, el programador y la fecha de la última modificación. Utilizar el caracter # para los comentarios.
"""


#Programa: Carga de 10 Numeros
#Programador: Paz Marcos
#Fecha de última modificación: 28/06/2018

suma=0.0
for x in range(10):
    valor=float(input("Ingrese valor:"))
    suma=suma+valor
print("La suma de los 10 numeros es")
print(suma)
