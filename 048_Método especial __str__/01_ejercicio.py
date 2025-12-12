"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Definir una clase llamada Punto con dos atributos x e y.
Crearle el método especial __str__ para retornar un string con el formato (x,y).
"""
class punto():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        var= str(self.x)+ "," +str(self.y)
        return (var)
punto1=punto(5,8)
print(punto1)
