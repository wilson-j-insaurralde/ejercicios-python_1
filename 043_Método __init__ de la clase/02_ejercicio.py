"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Desarrollar una clase que represente un punto en el plano y tenga los siguientes métodos: inicializar los valores de x e y que llegan como parámetros, imprimir en que cuadrante se encuentra dicho punto (concepto matemático, primer cuadrante si x e y son positivas, si x<0 e y>0 segundo cuadrante, etc.)
"""
class PuntoPlano():
    def __init__(self):
        self.x=int(input("ingrese la cordenada x: "))
        self.y=int(input("ingrese la cordenada y: "))
    
    def cuadrante(self):
        if self.x>0 and self.y>0:
            print("el punto se encuentra en el primer cuadrante")
        else: 
            if self.x<0 and self.y>0:
                print("el punto se encuentra en el segundo cuadrante")
            else: 
                if self.x<0 and self.y<0:
                    print("el punto se encuentra en el tercer cuadrante")
                else:
                    print ("el punto se encuentra en el cuarto cuadrante.")

punto=PuntoPlano()
punto.cuadrante()