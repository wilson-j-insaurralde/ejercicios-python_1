"""
Desarrollar un programa que cargue los lados de un triángulo e implemente los siguientes métodos: inicializar los atributos, imprimir el valor del lado mayor y otro método que muestre si es equilátero o no. El nombre de la clase llamarla Triangulo.
"""
class triangulo():
    def carga(self):
        self.lado1=int(input("ingrese el primer lado: "))
        self.lado2=int(input("ingrese el segundo lado: "))
        self.lado3=int(input("ingrese el tercer lado: "))
    def ladomayor(self):
        if self.lado1>self.lado2 and self.lado1>self.lado3:
            print("el lado mayor es: ",self.lado1)
        else: 
                if self.lado2>self.lado3:
                     print("el lado mayor es: ",self.lado2)
                else:
                     print("el lado mayor es:", self.lado3)
    def equilatero(self):
         if self.lado1==self.lado2==self.lado3:
              print("el triangulo es equilatero")
         else: 
              print("el triangulo no es equilatero.")

triangulo1=triangulo()
triangulo1.carga()
triangulo1.equilatero()
triangulo1.ladomayor()            