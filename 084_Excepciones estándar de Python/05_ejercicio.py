"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Realizar la carga de dos números por teclado e imprimir la división del primero respecto al segundo. Capturar cualquier tipo de excepción que se dispare.
"""

try:
    valor1=int(input("ingrese el primer valor: "))
    valor2=int(input("ingrese el segundo valor: "))
    division=valor1/valor2
    print("el valor de la division es: ",division)

except:
    print("se produjo un error en la operacion.")