"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""
"""Realizar la carga de dos números enteros por teclado e imprimir su suma, luego preguntar si quiere seguir sumando valores.
Codificar dos programas uno que capture la excepción de ingreso de datos no numéricos y el otro que no tenga en cuenta el tipo de entrada de datos.

Primero codificaremos sin la captura de excepciones.

"""

while True:
    valor1=int(input("ingrese el primer valor:"))
    valor2=int(input("ingrese el segundo valor:"))
    suma=valor1+valor2
    print("la suma es: ",suma)
    repuesta=input("Desea ingresar otro par de valores?[s/n]")
    if repuesta=="n":
        break


