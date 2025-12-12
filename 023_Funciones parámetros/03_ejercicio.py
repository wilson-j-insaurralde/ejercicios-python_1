"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Desarrollar un programa que permita ingresar el lado de un cuadrado. Luego preguntar si quiere calcular y mostrar su perímetro o su superficie.
"""
def perimetro(lado1):
    perimetro=lado1*4
    print(f"el perimetro del cuadrado es: {perimetro}")
def area(lado):
    area=lado*lado
    print(f"el area del cuadrado es: {area}")

def carga():
    numero=int(input("ingrese el lado del cuadrado: "))

    pre=input("quiere calcular el area (y/n)? ")

    if pre=='y':
        area(numero)

    pre2=input("quiere calcular el perimetro (y/n)? ")
    
    if pre2 == 'y':

     perimetro(numero)

carga()
