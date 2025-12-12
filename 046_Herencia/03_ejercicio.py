"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Declarar una clase Cuenta y dos subclases CajaAhorra y PlazoFijo. Definir los atributos y métodos comunes entre una caja de ahorro y un plazo fijo y agruparlos en la clase Cuenta.
Una caja de ahorro y un plazo fijo tienen un nombre de titular y un monto. Un plazo fijo añade un plazo de imposición en días y una tasa de interés. Hacer que la caja de ahorro no genera intereses.
En el bloque principal del programa definir un objeto de la clase CajaAhorro y otro de la clase PlazoFijo
"""
class cuenta():
    def __init__(self,nombre,monto):
        self.nombre=nombre
        self.monto=monto
    def mostrar_monto(self):
        print("cuenta de: ", self.nombre)
        print("el monto de la caja es: ",self.monto )

class cajadeahorro(cuenta):
    def __init__(self,nombre,monto):
        super().__init__(nombre,monto)
    def imprimir(self):
        print("cuenta de ahorro: ")
        super().mostrar_monto()
class plazofijo(cuenta):
    def __init__(self, nombre, monto,plazo,interes):
        super().__init__(nombre, monto)
        self.plazo=plazo
        self.interes=interes
    def imprimir(self):
        print("cuenta de plazo fijo: ")
        super().mostrar_monto()
        print("Plazo en dias:",self.plazo)
        print("Interes:",self.interes)
        self.ganancia_interes()
    def ganancia_interes(self):
        ganancia=self.monto*self.interes/100
        print("importe del interes: ", ganancia)
    
cajaahorro=cajadeahorro("Juan", 2000)
cajaahorro.imprimir()

plazofijo=plazofijo("Diego", 10000, 30, 0.75)
plazofijo.imprimir()
