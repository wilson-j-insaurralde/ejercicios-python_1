"""
Plantear una clase Persona que contenga dos atributos: nombre y edad. Definir como responsabilidades la carga por teclado y su impresión.
En el bloque principal del programa definir un objeto de la clase persona y llamar a sus métodos.

Declarar una segunda clase llamada Empleado que herede de la clase Persona y agregue un atributo sueldo y muestre si debe pagar impuestos (sueldo superior a 3000)
También en el bloque principal del programa crear un objeto de la clase Empleado.
"""

class persona:
    def __init__(self):
        self.nombre=input("ingrese su nombre: ")
        self.edad=int(input("ingrese su edad: "))
    def imprimir(self):
        print("su nombre es: ",self.nombre)
        print("su edad es: ", self.edad)
class empleado(persona):
    def __init__(self):
        super().__init__() 
        self.sueldo=float(input("ingrese el sueldo: "))
    
    def imprimir(self): 
        super().imprimir()
        print("su sueldo es: ", self.sueldo)
    def paga_impuestos(self):
        if self.sueldo>3000:
            print("el empleado debe pagar impuestos: ")
        else:
            print ("no paga impuestos")
persona1=persona()
persona1.imprimir()
print("________________________")
empleado1=empleado()
empleado1.imprimir()
empleado1.paga_impuestos()

