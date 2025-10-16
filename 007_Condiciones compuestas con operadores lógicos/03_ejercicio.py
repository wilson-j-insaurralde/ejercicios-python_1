"""Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde a Navidad"""


dd=int(input("Ingrese nro de día:"))
mm=int(input("Ingrese nro de mes:"))
aa=int(input("Ingrese nro de año:"))
if mm==12 and dd==25:
    print("La fecha ingresada corresponde a navidad.")