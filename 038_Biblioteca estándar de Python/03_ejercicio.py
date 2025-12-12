"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Confeccionar un programa que genere un número aleatorio entre 1 y 100 y no se muestre.
El operador debe tratar de adivinar el número ingresado.
Cada vez que ingrese un número mostrar un mensaje "Gano" si es igual al generado o "El número aleatorio es mayor" o "El número aleatorio es menor".
Mostrar cuando gana el jugador cuantos intentos necesitó.
"""
import random

numero=random.randint(1,100)
ingre=-1

while ingre!=numero:
    ingre=int(input("ingrese el numero: "))
    if numero==ingre:
        print("ganoo")
    else:   
        if numero>ingre:
            print("el numero ingresado es menor")
        else:
            print("el numero ingresado es mayor")
    
