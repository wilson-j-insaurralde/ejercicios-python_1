"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la suma de los valores ingresados y su promedio. Este problema ya lo desarrollamos, lo resolveremos empleando la estructura for para repetir la carga de los diez valores por teclado."""

suma=0

for x in range(10):
    numero=int(input("ingrese el numero: "))
    suma=suma+numero

promedio=suma/10

print (f"la suma de los numeros es: {suma}")
print (f"el promedio es: {promedio}")