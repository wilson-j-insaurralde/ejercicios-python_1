"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Elaborar una función que nos retorne el perímetro de un cuadrado pasando como parámetros el valor de un lado
"""
def perimetro(lad):
    perimetro=lad*4
    return perimetro

def carga ():
    x=int(input("ingrese el lado del cuadrado: "))
    return x

lado=carga()
print("el perimetro del cuadrado es: ",perimetro(lado))
