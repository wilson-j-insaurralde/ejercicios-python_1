"""
Plantear una clase Rectangulo. Definir dos atributos (ladomenor y ladomayor). Redefinir el operador == de tal forma que tengan en cuenta la superficie del rectángulo. Lo mismo hacer con todos los otros operadores relacionales.
"""
class Rectangulo:
    def __init__(self,ladomenor,ladomayor):
        self.ladomenor=ladomenor
        self.ladomayor=ladomayor
    
    def Retornar_superficie(self):
        superficie=self.ladomenor*self.ladomayor
        return superficie
    
    def __eq__(self, objeto2):
        if self.Retornar_superficie()==objeto2.Retornar_superficie():
           return True
        else: 
            return False
    def __ne__(self, objeto2):
        if self.Retornar_superficie()!=objeto2.Retornar_superficie():
            return True
        else:
            return False
    def __gt__(self,objeto2):
        if self.Retornar_superficie()>objeto2.Retornar_superficie():
            return True
        else:
            return False
    def __ge__(self,objeto2):
        if self.Retornar_superficie()>=objeto2.Retornar_superficie():
            return True
        else:
            return False
    def __lt__(self,objeto2):
        if self.Retornar_superficie()<objeto2.Retornar_superficie():
            return True
        else:
            return False
    def __le__(self,objeto2):
        if self.Retornar_superficie()<=objeto2.Retornar_superficie():
            return True
        else:
            return False

rectangulo1=Rectangulo(5,10)
rectangulo2=Rectangulo(5,10)
if rectangulo1==rectangulo2:
    print("Los rectangulos tienen la misma superficie")
else:
    print("Los rectangulos no tienen la misma superficie")
