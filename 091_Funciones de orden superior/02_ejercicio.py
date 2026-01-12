"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""


"""
Declarar una clase que almacene el nombre y la edad de una persona. Definir un método que retorne True o False según si la persona es mayor de edad o no. Este método debe recibir como parámetro una función que al llamarla pasando la edad de la persona retornará si es mayor o no de edad.
Tener en cuenta que una persona es mayor de edad en Estados Unidos si tiene 21 o más años y en Argentina si tiene 18 o más años.
"""


class personatuki():
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def es_mayor(self,fn):
        return fn(self.edad)
    
def mayor_estadosunidos(edad):

    if edad>=21:
        return True
    else:
        return False
    
def mayor_argentina(edad):
    if edad>=18:
        return True
    else:
        return False
    
persona1=personatuki("pepe",20)
persona2=personatuki("juancito",20)

if persona1.es_mayor(mayor_argentina):
    print(f"{persona1.nombre} es mayor de edad en argentina")
else:
    print(f"{persona1.nombre} es menor de edad en argentina")

if persona1.es_mayor(mayor_estadosunidos):
    print(f"{persona1.nombre} es mayor de edad en estados unidos")

else:
    print(f"{persona1.nombre} es menor de edad en estados unidos ")
