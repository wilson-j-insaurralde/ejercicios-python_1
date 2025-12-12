"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Implementar la clase Operaciones. Se deben cargar dos valores enteros por teclado en el método __init__, calcular su suma, resta, multiplicación y división, cada una en un método, imprimir dichos resultados.
"""
class operaciones():
    def __init__(self):
        self.entero1=int(input("ingrese el numero entero: "))
        self.entero2=int(input("ingrese el otro numero entero: "))

    def suma(self):
        print("su suma es: ",self.entero1+self.entero2)
    def resta(self):
        print("la resta es: ",self.entero1-self.entero2)
    def producto(self):
        print("el producto es: ",self.entero1*self.entero2)
    def devision(self):
        print("la division es: ",self.entero1/self.entero2)
operaciones1=operaciones()
operaciones1.suma()
operaciones1.resta()
operaciones1.producto()
operaciones1.devision()