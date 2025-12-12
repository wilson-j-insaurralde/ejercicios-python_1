"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde a Navidad"""


dd=int(input("Ingrese nro de día:"))
mm=int(input("Ingrese nro de mes:"))
aa=int(input("Ingrese nro de año:"))
if mm==12 and dd==25:
    print("La fecha ingresada corresponde a navidad.")