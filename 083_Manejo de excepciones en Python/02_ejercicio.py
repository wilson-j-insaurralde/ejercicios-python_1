"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

while True:
    try:
          valor1=int(input("ingrese el primer valor: "))
          valor2=int(input("ingrese el segundo valor: "))
          suma=valor1+valor2
          print("la suma es: ",suma)
          
    except ValueError:
         print("debe ingresar numeros.")

    repuestas=input("Desea ingresar otro par de valores?[s/n]")

    if repuestas=="n":
         break
    
