"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Realizar la carga de dos números por teclado e imprimir la división del primero respecto al segundo, capturar las excepciones ZeroDivisionError y ValueError.
"""

try:
    valor1=int(input("ingrese el primer valor: "))
    valor2=int(input("ingrese el segundo valor: "))
    division=valor1/valor2
    print("el resuiltado de la division es: ",division)

except ZeroDivisionError:
    print("no se puede dividir por 0")
except ValueError:
    print("no se puede ingresar letras.")