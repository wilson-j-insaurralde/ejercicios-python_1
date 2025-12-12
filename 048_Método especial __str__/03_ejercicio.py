"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Desarrollar un programa que implemente una clase llamada Jugador.
Definir como atributos su nombre y puntaje.
Codificar el método especial __str__ que retorne el nombre y si es principiante (menos de 1000 puntos) o experto (1000 o más puntos)
"""
class jugador:
    def __init__(self,nombre,puntaje):
        self.nombre=nombre
        self.puntaje=puntaje
    def __str__(self):
        cadena=str(self.nombre)+","
        if self.puntaje>1000:
            cadena=cadena+"experto"
        else:
            cadena=cadena+"principiante"
        return cadena
    
jugador1=jugador("Juan",750)
jugador2=jugador("Ana",1200)
print(jugador1)
print(jugador2)