"""
Confeccionar una función que calcule la superficie de un rectángulo y la retorne, la función recibe como parámetros los valores de dos de sus lados:
def retornar_superficie(lado1,lado2):
En el bloque principal del programa cargar los lados de dos rectángulos y luego mostrar cual de los dos tiene una superficie mayor.
"""

def supRectangulo(lado1,lado2):

    superficie=lado1*lado2
    return superficie
print("ingrese los lados del primer retangulo: ")
x1=int(input("ingrese el lado1: "))
y1=int(input("ingrese el lado2: "))
print("ingrese los lados del segundo retangulo: ")
x2=int(input("ingrese el lado1: "))
y2=int(input("ingrese el lado2: "))

sup1=supRectangulo(x1,y1)
sup2=supRectangulo(x2,y2)
if sup1>sup2:
    print(f"el primer rectangulo es el de mayor superficie: {sup1}")
else:
    print(f"el segundo rectangulo es el de mayor superficie: {sup2}")