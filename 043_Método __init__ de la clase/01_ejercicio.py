"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
def __init__([parámetros]):
        [algoritmo]
"""
"""
Confeccionar una clase que represente un empleado. Definir como atributos su nombre y su sueldo. En el método __init__ cargar los atributos por teclado y luego en otro método imprimir sus datos y por último uno que imprima un mensaje si debe pagar impuestos (si el sueldo supera a 3000)
"""
class empleado():
    def __init__(self):
        self.nombre=input("ingrese el nombre del empleado: ")
        self.sueldo=float(input("ingrese el sueldo del empleado: "))

    def imprmirdatos(self):
        print("nombre del empleado: ",self.nombre)
        print("sueldo del empleado: ",self.sueldo)
    def impuestos(self):
        if self.sueldo>3000:
            print(f"el empledo {self.nombre} debe pagar impuestos. ")

        else: 
            print(f"el empleado {self.nombre} no debe pagar impuestos.")

empleado1=empleado()
empleado1.imprmirdatos()
empleado1.impuestos()