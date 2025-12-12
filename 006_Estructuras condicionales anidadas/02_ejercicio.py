"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

#Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos.

num1=int(input("ingrese el primer numero: "))

num2=int(input("ingrese el segundo numero: "))
num3=int(input("ingrese el tercer numero: "))

if (num1>num2):
    if (num1>num3):
        print (f"el numero {num1} es el mayor.")
    else: print (f"el numero {num3} es el mayor.")
else: 
    if (num2>num3):
        print (f"el numero {num2} es el mayor.")
    else:
        print (f"el numero {num3} es el mayor.")

    
