"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Python nos permite redefinir los operadores matemáticos cuando planteamos una clase.

Los métodos especiales que debemos implementar son los siguientes:

Para el operador +:

__add__(self,objeto2)
Para el operador -:

__sub__(self,objeto2)
Para el operador *:

__mul__(self,objeto2)
Para el operador //:

__floordiv__(self,objeto2)
Para el operador /:

__truediv__(self,objeto2)
"""
"""
Veamos con un ejemplo la sintaxis para redefinir el operador +.
Crearemos una clase Cliente de un banco y redefiniremos el operador + para que nos retorne la suma de los depósitos de los dos clientes que estamos sumando.
"""
class cliente: 
    def __init__(self,nombre,monto):
        self.monto=monto
        self.nombre=nombre

    def __add__ (self,objeto2):
        s=self.monto+objeto2.monto
        return s 
    
cli1=cliente('Ana',1200)
cli2=cliente('Luis',1500)
print("El total depositado por los dos clientes es")
print(cli1+cli2)