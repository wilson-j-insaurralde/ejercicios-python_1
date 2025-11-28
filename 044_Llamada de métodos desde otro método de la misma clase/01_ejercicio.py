"""
Plantear una clase Operaciones que solicite en el método __init__ la carga de dos enteros e inmediatamente muestre su suma, resta, multiplicación y división. Hacer cada operación en otro método de la clase Operación y llamarlos desde el mismo método __init__
"""

class enterover():
    def __init__(self):
        self.entero1=int(input("ingrese el numero entero: "))
        self.entero2=int(input("ingrese el otro numero entero: "))
        self.suma()
        self.resta()
        self.multiplicacion()
        self.division()

    def suma(self):
        suma=self.entero1+self.entero2
        print(f"su suma es: {suma}")

    def resta(self):
        resta=self.entero1-self.entero2
        print(f"su resta es: {resta}")
    def multiplicacion(self):
        multiplicacion=self.entero1*self.entero2
        print(f"su multiplicacion es: { multiplicacion}")
    def division(self):
        division=self.entero1/self.entero2
        print(f"su division es: {division}")
    

entero=enterover()
