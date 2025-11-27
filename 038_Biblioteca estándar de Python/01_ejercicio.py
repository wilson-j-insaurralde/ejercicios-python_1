"""
Confeccionar un programa que simule tirar dos dados y luego muestre los valores que salieron. Imprimir un mensaje que ganó si la suma de los mismos es igual a 7.
"""
import random
dado1=random.randint(1,6)
dado2=random.randint(1,6)

print(dado1,dado2,sep=" --- ")
suma=dado2+dado1
if suma==7:
    print ("gano")
else: print("perdio")

