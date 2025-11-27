"""
Desarrollar una clase que represente un Cuadrado y tenga los siguientes métodos: inicializar el valor del lado llegando como parámetro al método __init__ (definir un atributo llamado lado), imprimir su perímetro y su superficie.
"""

class Cuadrado():
    def __init__(self):
        self.lado=int(input("ingrese el lado del cuadrado: "))

    def area(self):
        print("el area es: ",self.lado*self.lado)
    def perimetro(self):
        print("el perimetro es: ",self.lado*4)
    
cuadrado1=Cuadrado()
cuadrado1.area()
cuadrado1.perimetro()