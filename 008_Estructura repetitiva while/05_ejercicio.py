"""
Problemas propuestos
Ha llegado la parte fundamental, que es el momento donde uno desarrolla individualmente un algoritmo para la resolución de problemas.

El tiempo a dedicar a esta sección EJERCICIOS PROPUESTOS debe ser mucho mayor que el empleado a la sección de EJERCICIOS RESUELTOS.
La experiencia dice que debemos dedicar el 80% del tiempo a la resolución individual de problemas y el otro 20% al análisis y codificación de problemas ya resueltos por otras personas.
Es de vital importancia para llegar a ser un buen PROGRAMADOR poder resolver problemas en forma individual.
"""

#Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores

x=1
conta1=0
conta2=0
while x<=10:
    nota=int(input("Ingrese nota:"))
    if nota>=7:
        conta1=conta1+1
    else:
        conta2=conta2+1
    x=x+1
print("Cantidad de alumnos con notas mayores o iguales a 7")
print(conta1)
print("Cantidad de alumons con notas menores a 7")
print(conta2)
