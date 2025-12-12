"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Los métodos especiales que podemos implementar son los siguientes:

Para el operador ==:
__eq__(self,objeto2)

Para el operador !=:
__ne__(self,objeto2)

Para el operador >:
__gt__(self,objeto2)

Para el operador >=:
__ge__(self,objeto2)

Para el operador <:
__lt__(self,objeto2)

Para el operador <=:
__le__(self,objeto2)
"""
"""
Crear una clase Persona que tenga como atributo el nombre y la edad.
El operador == retornará verdadero si las dos personas tienen la misma edad, el operador > retornará True si la edad del objeto de la izquierda tiene una edad mayor a la edad del objeto de la derecha del operador >, y así sucesivamente
"""
class Persona: 
    def __init__(self,nombre,edad):
        self.nombre=nombre  
        self.edad=edad
    def __eq__(self, objeto2):
        if self.edad==objeto2.edad:
            return True
        else: 
            return False
    
    def __ne__(self, objeto2):
        
        if self.edad!=objeto2.edad:
            return True
        else:
            return False
    
    def __gt__ (self,objeto2):
        if self.edad>objeto2.edad:
            return True
        else: 
            return False
    def __ge__ (self, objeto2):
        if self.edad>=objeto2.edad:
            return True
        else: 
            return False
        
    def __lt__(self,objeto2):
        if self.edad<objeto2.edad:
            return True
        else: 
            return False
    
    def __le__(self,objeto2):
        if self.edad<=objeto2.edad:
            return True
        else: 
            return False
persona1=Persona('batata',22)
persona2=Persona('batatita',22)

if persona1==persona2:
    print("las dos personas tienen la misma edad. ")
else: 
    print ("no tienen la misma edad.")