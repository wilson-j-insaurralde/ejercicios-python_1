"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Realizar un programa que solicite la carga de valores enteros por teclado y los sume. Finalizar la carga al ingresar el valor -1. Dejar como comentario dentro del código fuente el enunciado del problema.
"""

"""
Realizar un programa que solicite la carga de valores enteros por teclado y los sume.
Finalizar la carga al ingresar el valor -1.
"""

suma=0
valor=int(input("Ingrese valor (-1 finaliza):"))     # se carga el primer valor antes del while
while valor!=-1:
    suma=suma+valor
    valor=int(input("Ingrese valor(-1 finaliza):"))  # se cargar todos los otros valores dentro del while
print("La suma de los valores ingresados es")
print(suma)