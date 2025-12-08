"""
Plantear una clase llamada Jugador.
Definir en la clase Jugador los atributos nombre y puntaje, y los métodos __init__, imprimir y pasar_tiempo (que debe reducir en uno la variable de clase).
Declarar dentro de la clase Jugador una variable de clase que indique cuantos minutos falta para el fin de juego (iniciarla con el valor 30)
Definir en el bloque principal dos objetos de la clase Jugador.
Reducir dicha variable hasta llegar a cero.
"""
class jugador():
    tiempo=30
    def __init__(self,nombre,puntaje):
        self.nombre=nombre
        self.puntaje=puntaje
    def imprimir (self):
        print("nombre: ",self.nombre)
        print("puntaje: ", self.puntaje)
    def pasar_minutos(self):
          jugador.tiempo=jugador.tiempo-1
        
jugador1=jugador("Juan",100)
jugador2=jugador("Ana",50)
while jugador.tiempo>0:
    jugador1.imprimir()
    jugador2.imprimir()
    jugador1.pasar_minutos()